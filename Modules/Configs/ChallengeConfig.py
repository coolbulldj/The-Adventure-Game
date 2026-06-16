# Challenge data indexed by act (0–3).

Challenges = [
    # Act 1 — Warren protests: security scan the crowd.
    {
        "Location": "Warren District — Protest Checkpoint",
        "Intro": (
            "Solance wants eyes on the protest line. Scan each arrival and type "
            "1 to clear them or 2 to detain for secondary screening."
        ),
        "Type": "security_scan",
        "RequiredCorrect": 4,
        "Targets": [
            {
                "Name": "Mira Cole",
                "Description": "Neighborhood organizer. Protest badge matches public records.",
                "IdNumber": "WC-4421",
                "IsThreat": False,
            },
            {
                "Name": "Unidentified Male",
                "Description": "Keeps visor down. Scanner flags mismatched facial mesh.",
                "IdNumber": "SF-0091 (alias)",
                "IsThreat": True,
            },
            {
                "Name": "Devon Hale",
                "Description": "Union steward. ID checks out. No contraband on scan.",
                "IdNumber": "WC-1180",
                "IsThreat": False,
            },
            {
                "Name": "Courier 12",
                "Description": "Claims press credentials. Badge hologram fails validation.",
                "IdNumber": "MEDIA-???",
                "IsThreat": True,
            },
            {
                "Name": "Priya Nand",
                "Description": "Medic volunteer. Medical registry ID verified.",
                "IdNumber": "MD-7734",
                "IsThreat": False,
            },
            {
                "Name": "Station Officer K-4",
                "Description": "Solance plainclothes. Valid override code on file.",
                "IdNumber": "SL-0004",
                "IsThreat": False,
            },
            {
                "Name": "Unknown Female",
                "Description": "Burner phone detected. ID chip cloned from another citizen.",
                "IdNumber": "WC-4421 (duplicate)",
                "IsThreat": True,
            },
        ],
    },
    # Act 2 — Industrial belt: find the manual, then hack the grid terminal.
    {
        "Location": "Industrial Belt — Strike Perimeter",
        "Intro": (
            "The security manual is somewhere on this line. Ask workers for leads "
            "(type 1–4), then hack the grid terminal with the password you find."
        ),
        "Type": "manual_and_hack",
        "NpcOptions": [
            {
                "Name": "Rina Ortiz",
                "Description": "Line cook on break. Knows rumors, not manuals.",
                "Response": "Manual? Try the old turbine shack. Maintainers hoard that stuff.",
            },
            {
                "Name": "Tomas Vega",
                "Description": "Strike captain. Suspicious of outsiders.",
                "Response": "We don't hand out Solance documents. Move along.",
            },
            {
                "Name": "Elliot Crane",
                "Description": "Retired grid maintainer. Grease-stained coveralls.",
                "Response": (
                    "Found a copy in my locker. Password is GRID-7741 — "
                    "don't fry the whole district with it."
                ),
                "GivesManual": True,
            },
            {
                "Name": "Warehouse Drone",
                "Description": "Automated courier. Repeats manifest numbers.",
                "Response": "Manifest 7741 rerouted. No manual aboard this unit.",
            },
        ],
        "HackPassword": "GRID-7741",
        "HackPrompt": "Grid terminal unlocked. Enter the maintenance password:",
    },
    # Act 3 — Ration line: catch identity fraud.
    {
        "Location": "District 9 — Ration Distribution",
        "Intro": (
            "Shipments stalled. Verify each claimant — type 1 to issue rations "
            "or 2 to deny when the name and ID do not match."
        ),
        "Type": "ration_fraud",
        "RequiredCorrect": 4,
        "Claimants": [
            {
                "StatedName": "Jonas Reed",
                "IdName": "Jonas Reed",
                "IdNumber": "FD-1102",
                "Household": "2 dependents",
                "IsFraud": False,
            },
            {
                "StatedName": "Sarah Kim",
                "IdName": "Marcus Webb",
                "IdNumber": "FD-8834",
                "Household": "claims 4 dependents",
                "IsFraud": True,
            },
            {
                "StatedName": "Elena Voss",
                "IdName": "Elena Voss",
                "IdNumber": "FD-2290",
                "Household": "1 dependent",
                "IsFraud": False,
            },
            {
                "StatedName": "Tomás Herrera",
                "IdName": "Tomás Herrera",
                "IdNumber": "FD-5517",
                "Household": "3 dependents",
                "IsFraud": False,
            },
            {
                "StatedName": "Amy Cho",
                "IdName": "Daniel Cho",
                "IdNumber": "FD-1199",
                "Household": "claims twin registration",
                "IsFraud": True,
            },
            {
                "StatedName": "Officer Halden",
                "IdName": "Officer Halden",
                "IdNumber": "SL-0412",
                "Household": "authorized relief worker",
                "IsFraud": False,
            },
        ],
    },
    # Act 4 — Capital infiltration: reach the broadcast tower and unlock it.
    {
        "Location": "Solance Capital — Outer Ring",
        "Intro": (
            "Reach the central broadcast system before curfew. Pick a safe route "
            "through each district, acquire a keycard, then unlock the tower."
        ),
        "Type": "capital_infiltration",
        "Routes": [
            {
                "Name": "Capitol Square",
                "Prompt": "Crowd surge ahead. Where do you slip through?",
                "Options": [
                    "Market Row — service alleys behind vendor stalls",
                    "Grand Plaza — open ground under searchlights",
                    "River Walk — tourist checkpoints at every bridge",
                ],
                "CorrectIndex": 0,
                "WrongFeedback": "Searchlights sweep the plaza. You back out before you're made.",
            },
            {
                "Name": "Archive District",
                "Prompt": "Records towers block the sky. Next move?",
                "Options": [
                    "Archive Annex — loading dock badges still honored",
                    "Hotel Row — lobby cameras on every floor",
                    "Embassy Circle — diplomatic scans at the gate",
                ],
                "CorrectIndex": 0,
                "WrongFeedback": "Scanners flag your route. You melt back into the side streets.",
            },
            {
                "Name": "Broadcast Quarter",
                "Prompt": "The tower looms ahead. Final approach?",
                "Options": [
                    "Maintenance Tunnels — steam vents mask your heat signature",
                    "Parade Gate — ceremonial guard detail on duty",
                    "Skybridge Lobby — biometric turnstiles armed",
                ],
                "CorrectIndex": 0,
                "WrongFeedback": "Guards tighten the cordon. You'll need another way in.",
            },
        ],
        "KeycardPhase": {
            "Location": "Broadcast Tower — Service Entrance",
            "NpcName": "Desk Sergeant Vale",
            "NpcDescription": "Monitors tunnel access. Expects paperwork for every visitor.",
            "Prompt": "Vale blocks the desk. How do you get a keycard?",
            "Options": [
                "Present falsified maintenance order BCS-2200",
                "Offer a bribe you cannot cover",
                "Rush the checkpoint alone",
            ],
            "CorrectIndex": 0,
            "WrongFeedback": "Vale calls for backup. The entrance seals shut.",
            "SuccessText": (
                "Vale stamps the order. Keycard code BCS-2200 — "
                "tower uplink ready for broadcast override."
            ),
        },
        "UnlockCode": "BCS-2200",
        "UnlockPrompt": "Slip the keycard into the tower lock. Enter the override code:",
    },
]
