def calculate_food_plan(
    guests,
    event_type
):

    guests = int(guests)

    event_type = str(
        event_type
    ).lower()

    # =========================
    # CATERING TYPE
    # =========================

    if guests >= 1000:

        catering_type = (
            "Luxury Mega Buffet"
        )

        cost_per_person = 1200

    elif guests >= 500:

        catering_type = (
            "Premium Buffet"
        )

        cost_per_person = 900

    elif guests >= 200:

        catering_type = (
            "Professional Catering"
        )

        cost_per_person = 700

    else:

        catering_type = (
            "Standard Catering"
        )

        cost_per_person = 500

    # =========================
    # EVENT SPECIFIC CUISINE
    # =========================

    if any(
        word in event_type
        for word in [
            "wedding",
            "marriage"
        ]
    ):

        cuisine_style = (
            "Royal Indian"
        )

        beverage_plan = (
            "Mocktails and Fresh Juices"
        )

    elif any(
        word in event_type
        for word in [
            "conference",
            "startup",
            "tech"
        ]
    ):

        cuisine_style = (
            "Modern Fusion"
        )

        beverage_plan = (
            "Coffee Bar and Energy Drinks"
        )

    elif any(
        word in event_type
        for word in [
            "gaming",
            "tournament"
        ]
    ):

        cuisine_style = (
            "Fast Casual"
        )

        beverage_plan = (
            "Soft Drinks and Energy Beverages"
        )

    elif any(
        word in event_type
        for word in [
            "birthday",
            "party"
        ]
    ):

        cuisine_style = (
            "Party Special"
        )

        beverage_plan = (
            "Mocktails and Soft Drinks"
        )

    else:

        cuisine_style = (
            "Multi Cuisine"
        )

        beverage_plan = (
            "Soft Drinks"
        )

    # =========================
    # COST
    # =========================

    estimated_cost = (
        guests *
        cost_per_person
    )

    # =========================
    # OUTPUT
    # =========================

    return {

        "catering_type":
            catering_type,

        "estimated_servings":
            guests,

        "cuisine_style":
            cuisine_style,

        "beverage_plan":
            beverage_plan,

        "estimated_cost":
            estimated_cost,

        "special_menu":
            f"{event_type.title()} Special Menu"
    }