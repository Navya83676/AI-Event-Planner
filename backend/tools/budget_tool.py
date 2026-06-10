def calculate_budget_split(
    budget,
    guests
):

    budget = int(
        budget or 0
    )

    guests = int(
        guests or 0
    )

    # =========================
    # BASE ALLOCATION
    # =========================

    venue_cost = int(
        budget * 0.35
    )

    food_cost = int(
        budget * 0.30
    )

    decoration_cost = int(
        budget * 0.15
    )

    # =========================
    # SECURITY SCALING
    # =========================

    if guests >= 3000:

        security_cost = int(
            budget * 0.15
        )

    elif guests >= 1000:

        security_cost = int(
            budget * 0.12
        )

    elif guests >= 500:

        security_cost = int(
            budget * 0.10
        )

    else:

        security_cost = int(
            budget * 0.05
        )

    # =========================
    # CONTINGENCY RESERVE
    # =========================

    reserve_cost = int(
        budget * 0.05
    )

    # =========================
    # MISCELLANEOUS
    # =========================

    miscellaneous_cost = max(

        0,

        budget - (

            venue_cost +

            food_cost +

            decoration_cost +

            security_cost +

            reserve_cost
        )
    )

    # =========================
    # TOTAL COST
    # =========================

    total_estimated_cost = (

        venue_cost +

        food_cost +

        decoration_cost +

        security_cost +

        miscellaneous_cost
    )

    # =========================
    # RETURN
    # =========================

    return {

        "venue_cost":
            venue_cost,

        "food_cost":
            food_cost,

        "decoration_cost":
            decoration_cost,

        "security_cost":
            security_cost,

        "miscellaneous_cost":
            miscellaneous_cost,

        "reserve_cost":
            reserve_cost,

        "total_estimated_cost":
            total_estimated_cost
    }