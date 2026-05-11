import pygame
import pygame.freetype  # Import the freetype module explicitly
import os

# 1. Setup Pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("FreeType Rendering Example")
clock = pygame.time.Clock()

# 2. Define the path to your font file
# Ensure the .ttf file is in the same folder as this script
font_path = os.path.join('.', 'Assets', 'Fonts', 'PressStart2P-Regular.ttf')
print(font_path)
# 3. Initialize the FreeType Font
# 'size' here is in points/pixels
try:
    game_font = pygame.freetype.Font(font_path, size=24)
except OSError:
    print(f"Error: Could not find font at {font_path}")
    pygame.quit()
    exit()

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((30, 30, 30))

    # 4. Render text to the screen
    # Use 'render_to' to draw directly to a surface without creating a temporary one
    game_font.render_to(screen, (100, 180), "HELLO WORLD", (255, 255, 255))
    
    # Alternatively, you can rotate or style the text on the fly
    game_font.render_to(screen, (100, 240), "PIXEL STYLE", (0, 255, 0), rotation=10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
