a = [1, 2, 3] 
b = [1, 2, 3]

<<<<<<< Updated upstream
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()


class UIScrollingFrame:
    def __init__(self, x, y, width, height, canvas_height):
        # Frame Properties (Like Roblox Size and Position)
        self.rect = pygame.Rect(x, y, width, height)
        self.canvas_height = max(canvas_height, height)

        # CanvasPosition equivalent (tracks vertical scroll offset)
        self.canvas_y = 0

        # Colors matching Roblox Studio Light/Dark Theme aesthetics
        self.bg_color = (45, 45, 48)  # Dark background
        self.canvas_color = (30, 30, 30)  # Inner canvas content zone
        self.scrollbar_bg = (55, 55, 55)
        self.scrollbar_handle_color = (100, 100, 100)
        self.scrollbar_active_color = (0, 122, 204)  # Roblox Blue Highlight

        # Scrollbar dimensions (ScrollBarThickness = 12)
        self.sb_thickness = 12
        self.sb_rect = pygame.Rect(
            self.rect.right - self.sb_thickness,
            self.rect.y,
            self.sb_thickness,
            self.rect.height,
        )

        # Dragging state variables
        self.is_dragging = False
        self.drag_offset_y = 0

        # Pre-create surfaces for performance optimization
        self.frame_surface = pygame.Surface((width, height))
        self.canvas_surface = pygame.Surface(
            (width - self.sb_thickness, self.canvas_height)
        )

    def update_scrollbar(self):
        """Calculates the dynamic size and position of the scroll bar thumb."""
        visible_ratio = self.rect.height / self.canvas_height
        self.handle_height = max(
            20, int(self.rect.height * visible_ratio)
        )  # Ensure handle is clickable

        # Map canvas position directly to scrollbar screen tracks
        scroll_ratio = (
            self.canvas_y / (self.canvas_height - self.rect.height)
            if (self.canvas_height - self.rect.height) > 0
            else 0
        )
        handle_y = self.rect.y + int(
            scroll_ratio * (self.rect.height - self.handle_height)
        )

        self.handle_rect = pygame.Rect(
            self.rect.right - self.sb_thickness,
            handle_y,
            self.sb_thickness,
            self.handle_height,
        )

    def handle_event(self, event):
        self.update_scrollbar()
        mouse_pos = pygame.mouse.get_pos()

        # 1. Mouse Wheel Input (Roblox-like fluid scroll)
        if event.type == pygame.MOUSEWHEEL and self.rect.collidepoint(mouse_pos):
            self.canvas_y -= event.y * 35  # Adjust scroll sensitivity
            self.clamp_scroll()

        # 2. Left Mouse Click (Start Dragging Track Handle)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.handle_rect.collidepoint(mouse_pos):
                self.is_dragging = True
                self.drag_offset_y = mouse_pos[1] - self.handle_rect.y

        # 3. Left Mouse Release (Stop Dragging Track Handle)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False

        # 4. Active Motion Translation while dragging
        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            # Constrain handle movement boundary limits
            new_handle_y = mouse_pos[1] - self.drag_offset_y
            min_y = self.rect.y
            max_y = self.rect.bottom - self.handle_height
            new_handle_y = max(min_y, min(max_y, new_handle_y))

            # Map tracking movement back to Canvas Position value
            track_length = self.rect.height - self.handle_height
            scroll_ratio = (
                (new_handle_y - min_y) / track_length if track_length > 0 else 0
            )
            self.canvas_y = scroll_ratio * (self.canvas_height - self.rect.height)
            self.clamp_scroll()

    def clamp_scroll(self):
        """Forces the CanvasPosition boundary values to stick within constraints."""
        max_scroll = self.canvas_height - self.rect.height
        self.canvas_y = max(0, min(max_scroll, self.canvas_y))

    def draw(self, dest_surface, content_render_func):
        """
        Renders canvas components inside isolated clipping boundaries.
        content_render_func: a layout function passing the active surface array.
        """
        self.update_scrollbar()

        # Draw base background tracking window
        self.frame_surface.fill(self.bg_color)

        # Clean background canvas before compiling dynamic UI element layers
        self.canvas_surface.fill(self.canvas_color)

        # Fire external programmatic rendering loop to layout content elements
        content_render_func(self.canvas_surface)

        # Enforce Roblox "ClipDescendants" behavior: crop virtual canvas to framing bounds
        # Blit canvas element to frame coordinate offset
        self.frame_surface.blit(self.canvas_surface, (0, -self.canvas_y))

        # Render Scrollbar track gutter background UI line
        pygame.draw.rect(
            self.frame_surface,
            self.scrollbar_bg,
            (
                self.rect.width - self.sb_thickness,
                0,
                self.sb_thickness,
                self.rect.height,
            ),
        )

        # Render dynamic visual indicator track handle
        color = (
            self.scrollbar_active_color
            if self.is_dragging
            else self.scrollbar_handle_color
        )
        pygame.draw.rect(
            self.frame_surface,
            color,
            (
                self.rect.width - self.sb_thickness,
                self.handle_rect.y - self.rect.y,
                self.sb_thickness,
                self.handle_height,
            ),
        )

        # Blit whole unified container structure on main target screen coordinate destination
        dest_surface.blit(self.frame_surface, (self.rect.x, self.rect.y))


# --- Content Generation Loop Demo (Mimicking Roblox UIListLayout Grid) ---
def render_roblox_ui_items(canvas):
    font = pygame.font.SysFont("Arial", 18)
    # Loop generates dummy lists mirroring Inventory/Shop setups
    for i in range(25):
        item_rect = pygame.Rect(15, i * 45 + 15, canvas.get_width() - 30, 35)
        # Alternate item row stripe background track tinting
        row_color = (60, 60, 60) if i % 2 == 0 else (50, 50, 50)
        pygame.draw.rect(canvas, row_color, item_rect, border_radius=4)

        # Generate element text labels
        text = font.render(f"Explorer Item Row #{i + 1:02d}", True, (230, 230, 230))
        canvas.blit(text, (item_rect.x + 10, item_rect.y + 7))


# Instantiate scrolling frame: size 400x350, content canvas depth of 1200px
scroll_frame = UIScrollingFrame(x=200, y=100, width=400, height=350, canvas_height=1200)

# Main App Loop Execution Core Execution
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pass input processing window state engine functions
        scroll_frame.handle_event(event)

    SCREEN.fill((28, 28, 28))  # Master viewport clear block step

    # Draw component grouping package context
    scroll_frame.draw(SCREEN, render_roblox_ui_items)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
=======
print(a + b)
>>>>>>> Stashed changes
