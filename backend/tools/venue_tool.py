import random


def get_venue_recommendation(
    location,
    guests,
    budget,
    event_type=""
):

    guests = int(guests)
    budget = int(budget)

    event_type = str(
        event_type
    ).lower()

    # =========================
    # EVENT-AWARE VENUES
    # =========================

    if (

        "wedding" in event_type or
        "marriage" in event_type

    ):

        venues = [

            "Royal Wedding Palace",

            "Grand Heritage Resort",

            "Taj Banquet Hall",

            "Imperial Wedding Gardens",

            "Royal Orchid Convention Center"

        ]

    elif (

        "conference" in event_type or
        "startup" in event_type

    ):

        venues = [

            "Innovation Convention Center",

            "Global Business Arena",

            "Tech Expo Convention Hall",

            "Corporate Summit Center",

            "Leadership Conference Hub"

        ]

    elif (

        "gaming" in event_type or
        "tournament" in event_type

    ):

        venues = [

            "National Esports Arena",

            "Cyber Championship Dome",

            "Gaming Expo Center",

            "Ultimate Battle Arena",

            "Pro Gaming Stadium"

        ]

    elif (

        "fashion" in event_type or
        "runway" in event_type

    ):

        venues = [

            "Luxury Fashion Pavilion",

            "Elite Runway Center",

            "Grand Fashion Arena",

            "Designer Showcase Hall",

            "Vogue Exhibition Center"

        ]

    elif (

        "music" in event_type or
        "festival" in event_type

    ):

        venues = [

            "Harmony Music Grounds",

            "Live Nation Arena",

            "Festival Park Stadium",

            "Open Air Concert Valley",

            "Rockstar Event Grounds"

        ]

    elif (

        "hackathon" in event_type

    ):

        venues = [

            "Innovation Tech Hub",

            "Developer Convention Center",

            "CodeSprint Arena",

            "Startup Garage Campus",

            "Future Builders Hub"

        ]

    else:

        venues = [

            "Grand Royal Convention Center",

            "Elite Palace Banquet Hall",

            "Royal Garden Venue",

            "Premium Event Center"

        ]

    # =========================
    # CAPACITY BASED FILTER
    # =========================

    if guests >= 1000:

        venue = venues[0]

    elif guests >= 500:

        venue = random.choice(
            venues[:3]
        )

    else:

        venue = random.choice(
            venues
        )

    # =========================
    # CAPACITY
    # =========================

    capacity = guests + 100

    # =========================
    # VENUE COMPLEXITY
    # =========================

    if capacity >= 5000:

        venue_complexity = (
            "extreme"
        )

    elif capacity >= 1000:

        venue_complexity = (
            "high"
        )

    else:

        venue_complexity = (
            "standard"
        )

    # =========================
    # ESTIMATED COST
    # =========================

    estimated_cost = int(
        budget * 0.35
    )

    # =========================
    # RETURN
    # =========================

    return {

        "venue_name":
            venue,

        "capacity":
            capacity,

        "estimated_cost":
           estimated_cost,

        "location_advantage":
            f"Prime location in {location}",

        "venue_complexity":
            venue_complexity
    }