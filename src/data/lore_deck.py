lore_items = {
    "Record": {
        "text": "The Rise and Fall of Ziggy Stardust and The Spiders From Mars! What is it doing in Hogwarts?",
        "prerequisites": [],
        "tags": []
    },
    "Cigarette box": {
        "text": "A cigarette box! Damn... I've lost my lighter.",
        "prerequisites": [],
        "tags": ["found_cigarettes"]
    },
    "Lighter": {
        "text": "My glistening Zippo! Now I just gotta find Sirius for smoking company!",
        "prerequisites": ["found_cigarettes"],
        "tags": []
    },
    "Advanced Potionsmaking": {
        "text": "This must be Snivellus' property. Smells just as bad.",
        "prerequisites": [],
        "tags": []
    }
}

friendlys = {
    "Sirius": {
        "prerequisites": [],
        "tags": ["seen_sirius"]
    }
}

dialogue_tree = {
    "Sirius": {
        "intro": {
            "text": "Hiya Remus! What a rainy day... I know! We could listen to David Bowie and smoke a pack of Marlboro together! But I've lost my cigarettes and the LP. I know it's curfew already but could you go fetch them for us?",
            "prerequisites": [],
            "tags": ["started_level"]
        }
    }
}