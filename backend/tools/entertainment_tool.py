def generate_entertainment_plan(
    event_type,
    theme
):

    event_type = str(
        event_type
    ).lower()

    theme = str(
        theme
    ).strip()

    # =========================
    # TECH / STARTUP
    # =========================

    if any(
        word in event_type
        for word in [
            "tech",
            "startup",
            "conference"
        ]
    ):

        return {

            "main_entertainment": [

                "AI Showcase",

                "Startup Pitch Battle",

                "Interactive VR Zone"
            ],

            "guest_engagement":
                "Networking and Innovation Activities",

            "stage_performance":
                "Technology Experience Presentation",

            "estimated_cost":
                180000
        }

    # =========================
    # HACKATHON
    # =========================

    elif any(
        word in event_type
        for word in [
            "hackathon",
            "coding"
        ]
    ):

        return {

            "main_entertainment": [

                "Coding Competition",

                "Gaming Zone",

                "Innovation Challenge"
            ],

            "guest_engagement":
                "Mentor Sessions and Team Challenges",

            "stage_performance":
                "Project Demo Showcase",

            "estimated_cost":
                120000
        }

    # =========================
    # GAMING
    # =========================

    elif any(
        word in event_type
        for word in [
            "gaming",
            "tournament"
        ]
    ):

        return {

            "main_entertainment": [

                "Esports Arena",

                "Streamer Zone",

                "VR Experience"
            ],

            "guest_engagement":
                "Audience Gaming Challenges",

            "stage_performance":
                "Championship Finals Show",

            "estimated_cost":
                250000
        }

    # =========================
    # WEDDING
    # =========================

    elif any(
        word in event_type
        for word in [
            "wedding",
            "marriage"
        ]
    ):

        return {

            "main_entertainment": [

                "Live Orchestra",

                "Couple Entry Show",

                "Dance Performances"
            ],

            "guest_engagement":
                "Family Activities and Celebration Games",

            "stage_performance":
                "Wedding Celebration Performance",

            "estimated_cost":
                350000
        }

    # =========================
    # BIRTHDAY
    # =========================

    elif any(
        word in event_type
        for word in [
            "birthday",
            "party"
        ]
    ):

        return {

            "main_entertainment": [

                "DJ Party",

                "Dance Show",

                "Photo Booth"
            ],

            "guest_engagement":
                "Interactive Party Games",

            "stage_performance":
                "Birthday Celebration Show",

            "estimated_cost":
                90000
        }

    # =========================
    # DEFAULT
    # =========================

    return {

        "main_entertainment": [

            "Live Music",

            "Dance Performance"
        ],

        "guest_engagement":
            "Interactive Activities",

        "stage_performance":
            (
                f"{theme} Theme Performance"
                if theme
                else
                "Professional Stage Performance"
            ),

        "estimated_cost":
            100000
    }