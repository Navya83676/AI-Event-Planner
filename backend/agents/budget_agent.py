from tools.budget_tool import (
    calculate_budget_split
)


def apply_event_budget_strategy(
    event_type,
    tool_result
):

    event_type = event_type.lower()

    # =========================
    # TECH / STARTUP
    # =========================

    if (
        "tech" in event_type or
        "startup" in event_type or
        "conference" in event_type
    ):

        tool_result["venue_cost"] = int(
            tool_result["venue_cost"] * 1.20
        )

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.50
        )

    # =========================
    # HACKATHON
    # =========================

    elif (
        "hackathon" in event_type or
        "coding" in event_type
    ):

        tool_result["food_cost"] = int(
            tool_result["food_cost"] * 1.30
        )

        tool_result["venue_cost"] = int(
            tool_result["venue_cost"] * 1.10
        )

    # =========================
    # GAMING TOURNAMENT
    # =========================

    elif (
        "gaming" in event_type or
        "tournament" in event_type
    ):

        tool_result["venue_cost"] = int(
            tool_result["venue_cost"] * 1.30
        )

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.60
        )

    # =========================
    # WEDDING
    # =========================

    elif (
        "wedding" in event_type or
        "marriage" in event_type
    ):

        tool_result["food_cost"] = int(
            tool_result["food_cost"] * 1.25
        )

        tool_result["decoration_cost"] = int(
            tool_result["decoration_cost"] * 1.40
        )

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.20
        )

    # =========================
    # FASHION SHOW
    # =========================

    elif (
        "fashion" in event_type or
        "runway" in event_type
    ):

        tool_result["decoration_cost"] = int(
            tool_result["decoration_cost"] * 1.50
        )

    # =========================
    # CULTURAL FESTIVAL
    # =========================

    elif (
        "festival" in event_type or
        "cultural" in event_type
    ):

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.70
        )

        tool_result["food_cost"] = int(
            tool_result["food_cost"] * 1.20
        )

    # =========================
    # PRODUCT LAUNCH
    # =========================

    elif (
        "product" in event_type or
        "launch" in event_type
    ):

        tool_result["venue_cost"] = int(
            tool_result["venue_cost"] * 1.25
        )

    return tool_result


def budget_agent(data):

    # =========================
    # EXECUTION FLOW
    # =========================

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "budget_agent"
    )

    # =========================
    # SHARED MEMORY
    # =========================

    if "shared_memory" not in data:

        data["shared_memory"] = {}

    shared_memory = data.get(
        "shared_memory",
        {}
    )

    venue_complexity = shared_memory.get(
        "venue_complexity",
        "standard"
    )

    needs_security = shared_memory.get(
        "needs_security",
        False
    )

    event_scale = shared_memory.get(
        "event_scale",
        "medium"
    )

    event_type = data.get(
        "event_type",
        ""
    )

    original_budget = int(
        data.get(
            "budget",
            0
        )
    )

    # =========================
    # TOOL EXECUTION
    # =========================

    tool_result = calculate_budget_split(

        budget=original_budget,

        guests=data.get(
            "guests",
            0
        )
    )
    if not isinstance(
        tool_result,
        dict
):

         tool_result = {
             "venue_cost": 0,
             "food_cost": 0,
             "decoration_cost": 0,
             "security_cost": 0,
             "miscellaneous_cost": 0,
             "total_estimated_cost": 0         }

    # =========================
    # EVENT STRATEGY
    # =========================

    tool_result = apply_event_budget_strategy(

        event_type,

        tool_result
    )

    # =========================
    # EVENT OPTIMIZATION
    # =========================

    if venue_complexity == "high":

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.20
        )

    elif venue_complexity == "extreme":

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.50
        )

    if needs_security:

        tool_result["security_cost"] = int(
            tool_result["security_cost"] * 1.20
        )

    if str(event_scale).lower() == "mega":

        tool_result["food_cost"] = int(
            tool_result["food_cost"] * 1.25
        )

    # =========================
    # SAFE NORMALIZATION
    # =========================

    fields = [

        "venue_cost",
        "food_cost",
        "decoration_cost",
        "security_cost",
        "miscellaneous_cost",
        "reserve_cost"
    ]

    for field in fields:

        tool_result[field] = max(

            0,

            int(
                tool_result.get(
                    field,
                    0
                ) or 0
            )
        )

    # =========================
    # TOTAL COST
    # =========================

    total_estimated_cost = (

        tool_result["venue_cost"] +

        tool_result["food_cost"] +

        tool_result["decoration_cost"] +

        tool_result["security_cost"] +

        tool_result["miscellaneous_cost"] +

        tool_result["reserve_cost"]
    )

    # =========================
    # BUDGET NORMALIZATION
    # =========================

    if (
        total_estimated_cost >
        original_budget
    ):

        scale = (
            original_budget /
            total_estimated_cost
        )

        for field in fields:

            tool_result[field] = int(
                tool_result[field] * scale
            )

        total_estimated_cost = (

            tool_result["venue_cost"] +

            tool_result["food_cost"] +

            tool_result["decoration_cost"] +

            tool_result["security_cost"] +

            tool_result["miscellaneous_cost"]
        )

    # =========================
    # FINAL VALUES
    # =========================

    tool_result[
        "total_estimated_cost"
    ] = total_estimated_cost

    remaining_budget = max(
    0,
    original_budget - total_estimated_cost
    )

    tool_result["remaining_budget"] = (
         remaining_budget
    )

    if remaining_budget < 1000:

        tool_result["remaining_budget"] = int(
            original_budget * 0.05
    )

    # =========================
    # FINAL OUTPUT
    # =========================

    data["budget_plan"] = tool_result

    data["budgetPlan"] = tool_result

    data["shared_memory"]["remaining_budget"] = (
        tool_result["remaining_budget"]
)

    return data