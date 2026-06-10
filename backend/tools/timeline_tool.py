def generate_timeline_plan(
    event_type
):

    event_type = str(
        event_type
    ).lower()

    # =========================
    # CONFERENCE / STARTUP
    # =========================

    if any(
        word in event_type
        for word in [
            "conference",
            "startup"
        ]
    ):

        return {

            "morning": [

                "Venue Setup",
                "Speaker Check-in",
                "Registration Desk Opening",
                "Guest Registration",
                "Welcome Coffee Session",
                "Opening Ceremony",
                "Keynote Address",
                "Industry Insights Session"
            ],

            "afternoon": [

                "Panel Discussion",
                "AI Innovation Showcase",
                "Networking Session",
                "Lunch Break",
                "Startup Pitch Session",
                "Product Demonstrations",
                "Business Roundtables",
                "Investor Meetings"
            ],

            "evening": [

                "Awards Ceremony",
                "Closing Keynote",
                "VIP Networking",
                "Corporate Dinner",
                "Media Interaction",
                "Event Wrap-up"
            ]
        }

    # =========================
    # HACKATHON
    # =========================

    elif "hackathon" in event_type:

        return {

            "morning": [

                "Venue Setup",
                "Participant Registration",
                "Team Formation",
                "Hackathon Launch",
                "Problem Statement Release",
                "Mentor Introduction"
            ],

            "afternoon": [

                "Coding Sprint",
                "Technical Workshops",
                "Mentor Review Session",
                "Progress Evaluation",
                "Networking Break"
            ],

            "evening": [

                "Final Coding Sprint",
                "Project Submission",
                "Project Demonstrations",
                "Jury Evaluation",
                "Winner Announcement",
                "Closing Ceremony"
            ]
        }

    # =========================
    # GAMING TOURNAMENT
    # =========================

    elif any(
        word in event_type
        for word in [
            "gaming",
            "tournament"
        ]
    ):

        return {

            "morning": [

                "Arena Setup",
                "Player Registration",
                "Gaming PC Setup",
                "Network Testing",
                "Streaming Setup",
                "Opening Ceremony",
                "Group Stage Matches Begin"
            ],

            "afternoon": [

                "Qualifier Matches",
                "Sponsor Showcase",
                "Gaming Zone Activities",
                "Caster Analysis Session",
                "Audience Competitions",
                "Semi Finals"
            ],

            "evening": [

                "Grand Finals",
                "Live Broadcast",
                "Champion Ceremony",
                "Prize Distribution",
                "Media Interviews",
                "Fan Meet & Greet",
                "Closing Show"
            ]
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

            "morning": [

                "Venue Decoration",
                "Stage Setup",
                "Guest Arrival",
                "Bride Preparation",
                "Groom Preparation",
                "Photography Session"
            ],

            "afternoon": [

                "Wedding Ceremony",
                "Family Rituals",
                "Blessing Ceremony",
                "Family Photography",
                "Lunch Service"
            ],

            "evening": [

                "Grand Reception",
                "Couple Entry",
                "Entertainment Program",
                "Dinner Service",
                "Cake Ceremony",
                "Event Closing"
            ]
        }

    # =========================
    # FASHION SHOW
    # =========================

    elif any(
        word in event_type
        for word in [
            "fashion",
            "runway"
        ]
    ):

        return {

           "morning": [
            "Runway Setup",
            "Lighting Test",
            "Photography Setup",
            "Designer Preparation"
        ],

            "afternoon": [
            "Model Check-in",
            "Makeup Session",
            "Brand Showcase",
            "Designer Presentations",
            "Runway Rehearsal",
            "VIP Reception"
        ],

            "evening": [

                "Fashion Show Launch",
                "Runway Presentation",
                "Designer Showcase",
                "Photography Session",
                "Press Interaction",
                "Awards & Closing"
            ]
        }

    # =========================
    # MUSIC FESTIVAL
    # =========================

    elif any(
        word in event_type
        for word in [
            "music",
            "festival"
        ]
    ):

        return {

           "morning": [
            "Final Stage Inspection",
            "Sound System Testing",
            "Lighting System Testing",
            "Vendor Check-in",
            "Security Briefing"
        ],

            "afternoon": [
            "Artist Arrival",
            "Backstage Preparation",
            "Technical Rehearsals",
            "Final Sound Check",
            "Gate Opening Preparation"
        ],

            

            "evening": [

                  "Festival Opening",
                  "DJ Performance",
                  "Main Artist Show",
                  "Headliner Concert",
                  "Fireworks Show",
                  "Late Night Performance",
                  "Crowd Exit Management",
                  "Venue Shutdown"
            ]
        }

    # =========================
    # DEFAULT
    # =========================

    return {

        "morning": [

            "Venue Preparation",
            "Guest Registration",
            "Opening Session"
        ],

        "afternoon": [

            "Main Event Activities",
            "Networking Session"
        ],

        "evening": [

            "Closing Ceremony",
            "Dinner"
        ]
    }