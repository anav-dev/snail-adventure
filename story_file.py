# story dictionary (with pages number, page text, and user options) to store story data in key-value pairs
snail_story = {
    # story start
    1: {
        'Text' : [
            "On a rock by the docks lives a sea snail",
            "who dreams of seeing the big, wide world, ",
            "a desire her rock-bound friends don't understand.",
        ],
        'Options': [
            ("Take action", 2),
            ("Keep dreaming", 5),
        ],
        'Hint': [
            "Taking action is the first step towards achieving your goals!",
        ]
    },
    # option selected: take action
    2: {
        'Text' : [
            "The Snail writes a `Lift wanted around the world` message using her snail trail.",
            "One moonlit night, a kind humpback whale arrives and offers to take her along on his travels.",
        ],
        'Options': [
            ("Accept offer", 3),
            ("Reject offer", 5),
        ],
        'Hint': [
            "Travelling will always enrich your life!",
        ]
    },
    # option selected: accept offer
    3: {
        'Text' : [
            "Together, they embark on a journey across the oceans, past icebergs, volcanoes, sharks, and penguins.",
            "One sunny summer morning, the whale, confused by the sound of racing speedboats, ",
            "swims into a bay and gets stranded by the retreating tide.",
        ],
        'Options': [
            ("Help", 4),
            ("Do not help", 10), # This options leads to end story
        ],
        'Hint': [
            "Helping friends improve the lives of those around you!",
        ]
    },
    # option selected: help
    4: {
        'Text' : [
            "The snail writes `Save The Whale!` with her trail on a school blackboard to help her friend.",
            "The teacher calls for help, and villagers keep the whale wet until the tide returns.",
            "The snail and the whale then swim away safely.",
        ],
        'Options': [
            ("Come back home", 7),
            ("Keep adventuring", 5),
        ],
        'Hint': [
            "Navigating adventures is so much fun!",
        ]
    },
    # option selected: keep adventuring
    5: {
        'Text' : [
            "One day, a fearsome sea dragon arrives at the docks threatening to harm everyone.",
        ],
        'Options': [
            ("Fight the dragon", 6),
            ("Run away", 10), # This options leads to end story
        ],
        'Hint': [
            "The snail is stronger than you think!",
        ]
    },
    # option selected: fight the dragon
    6: {
        'Text' : [
            "The snail trickes the dragon into believing they have a treasure in a nearby underwater cave",
            "As they venture deeper into caves, the snail using her small size, ",
            "guides the dragon through narrow passages that trap the dragon, ",
            "allowing them to escape and save the docks!",
        ],
        'Options': [
            ("Come back home", 7),
            ("Meet the snail major", 8),
        ],
        'Hint': [
            "The major is renowned for its friendliness!",
        ]
    },
    # option selected: come back home
    7: {
        'Text' : [
            "They return to the snail's home at the dock, ",
            "where the other snails are amazed by their stories.",
        ],
        'Options': [
            ("Go to sleep", 9),
            ("Meet the snail major", 8),
        ],
        'Hint': [
            "The major is renowned for its friendliness!",
        ]
    },
    # option selected: meet the snail major
    8: {
        'Text' : [
            "After their adventure, the mayor of the docks congratulates the snail.",
            "In recognition of her heroic actions, he presents her with ",
            "the prestigious Docks Medal, symbolizing her invaluable bravery.",
        ],
        'Options': [
            ("Go to sleep", 9),
            ("End story ", 10),
        ],
        'Hint': [
            "It's time to get a well-deserved rest!",
        ]
    },
    # option selected: go to sleep
    9: {
        'Text' : [
            "After a long adventure, the snail realizes that ...",
            " anyone, no matter how small you are, "
            "can achieve great things if they put their mind to it! ",
            "so ... ",
            "keep trying things beyond your reach till you succeed, be a snail!",
        ],
        'Options': [
           ("End story ", 10),
        ],
        'Hint': [
            # No hint needed here
        ]
    },
    # options selected: do not help, run away, or end story
    10: {
        'Text' : [
            "And so, this adventure came to an end!",
        ],
        'Options': [
           ("Read again ", 1), # Redirect to first story
           ("Exit program") # Redirect to welcome section
        ],
        'Hint': [
            # No hint needed here
        ]
    },
    

    # story end
}
