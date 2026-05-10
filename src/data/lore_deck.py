lore_items = {
    "Record": {
        "text": ("The Rise and Fall of Ziggy Stardust and The Spiders From Mars! "
                 "Filch has surely confiscated this..."),
        "prerequisites": ["seen_sirius", "started_level"],
        "tags": ["found_record"]
    },
    "Cigarette box": {
        "text": ("A cigarette box! Damn... I've lost my lighter. "
                 "And surely Sirius doesn't have one, he always loses all his stuff."),
        "prerequisites": ["seen_sirius", "started_level"],
        "tags": ["found_cigarettes"]
    },
    "Lighter": {
        "text": "My glistening Zippo! Now I just gotta find Sirius for smoking company!",
        "prerequisites": ["found_cigarettes"],
        "tags": ["found_lighter"]
    },
    "Advanced Potionsmaking": {
        "text": "This must be Snivellus' property. Smells just as bad. Better throw it away.",
        "prerequisites": ["seen_sirius", "started_level"],
        "tags": ["found_snapes_textbook"]
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
        "end": {
            "text": ("YOU DID IT!!! You really are a special friend Remus. "
                     "Thanks for risking your study rights for me. ;) "
                     "CONGRATULATIONS! YOU WON THE GAME!"),
            "prerequisites": ["found_record", "found_cigarettes", "found_lighter"],
            "tags": ["won"]
        },
        "zippo": {
            "text": ("Ummmmm... Maybe you could go out there once more? "
                     "You know I'm terrible at keeping track of my lighters. Hehe."),
            "prerequisites": ["found_record", "found_cigarettes"],
            "tags": []
        },
        "keep_looking_cigarettes": {
            "text": ("My beloved Ziggy Stardust!! Where did you find it? "
                     "Anyways, we do still need some nicotine in our veins, get out there buddy!"),
            "prerequisites": ["found_record"],
            "tags": []
        },
        "keep_looking_album": {
            "text": ("Oooh you found the Marlboros? I knew I lost a pack the day before yesterday. "
                     "But you still gotta find the record!"),
            "prerequisites": ["found_cigarettes"],
            "tags": []
        },
        "keep_looking": {
            "text": ("Why did you come back? An empty record player doesn't help a lot, "
                     "especially without nicotine... "
                     "Oh but remember to look out for nosy people on the hallways!"),
            "prerequisites": ["started_level"],
            "tags": []
        },
        "intro": {
            "text": ("Hiya Remus! What a rainy day... I know! "
                     "We should listen to David Bowie and smoke a pack of Marlboro together! "
                     "But I've lost both my cigarettes and the LP. "
                     "I know it's curfew already but could you go fetch them for us?"),
            "prerequisites": [],
            "tags": ["started_level"]
        }
    }
}
