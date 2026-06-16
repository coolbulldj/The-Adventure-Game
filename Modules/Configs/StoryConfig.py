# Reputation = 0
# CurrentAct = 0

#{
#EventName
#RequiredReputation: number,
#DialogueOpening: [string]
#DialoguePositiveRepOptions: [string], (siding with solance)
#DialogueNegativeRepOptions: [string], (siding with the rebellion)

StoryConfig = [
    #Warren Protests
    [
        {
            "EventName": "WarrenProtests",
            "RequiredReputation": 0, #since this is the first event the player wouldn't have any reputation yet
            "DialogueOpening": "The protests are getting bigger and bigger, the people are angry and they want change.",
            "DialoguePositiveRepOptions": ["I want to listen to solance"],
            "DialogueNegativeRepOptions": ["I want to listen to the rebellion"],
        }
    ],
    #The Industrial Belt Strikes
    [
        {
            "EventName": "IndustrialStrikes",
            "RequiredReputation": -1, #since this is the first event the player wouldn't have any reputation yet
            "DialogueOpening": "The belt has began to strike, the power generators are down and the people are angry and they want change. (repuation - 1)",
            "DialoguePositiveRepOptions": ["I want to listen to solance"],
            "DialogueNegativeRepOptions": ["I want to listen to the rebellion"],
        },
        {
            "EventName": "IndustrialStrikes",
            "RequiredReputation": 1, #since this is the first event the player wouldn't have any reputation yet
            "DialogueOpening": "The belt has began to strike, the power generators are down and the people are angry and they want change. (repuation 1)",
            "DialoguePositiveRepOptions": ["I want to listen to solance"],
            "DialogueNegativeRepOptions": ["I want to listen to the rebellion"],
        }
    ]
]