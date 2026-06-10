// src/utils/eventAIEngine.js

const randomFrom = (arr) =>
  arr[Math.floor(Math.random() * arr.length)];

/* ========================================
   GUEST GENERATOR
======================================== */

export const generateGuests = (
  guestCount,
  eventType
) => {

  let names = [];

  const type =
    eventType.toLowerCase();

  if (
    type.includes("ai") ||
    type.includes("tech") ||
    type.includes("hackathon")
  ) {

    names = [
      "Aarav Mehta",
      "Sophia Chen",
      "Elon Verma",
      "Rahul Kapoor",
      "Ananya Reddy",
      "David Kim",
      "Ishaan Malhotra",
      "Priya Nair",
      "Alex Johnson",
      "Fatima Khan"
    ];

  } else if (
    type.includes("wedding")
  ) {

    names = [
      "Rohan Sharma",
      "Sneha Patel",
      "Arjun Rao",
      "Meera Kapoor",
      "Kabir Singh",
      "Pooja Verma",
      "Aditi Sharma",
      "Vikram Reddy"
    ];

  } else if (
    type.includes("music") ||
    type.includes("concert")
  ) {

    names = [
      "DJ Arjun",
      "Riya Kapoor",
      "Aman Beats",
      "Neha Live",
      "Karan Vox",
      "Sara Blaze"
    ];

  } else {

    names = [
      "Rahul Sharma",
      "Priya Verma",
      "Aman Gupta",
      "Neha Reddy",
      "Ritika Kapoor"
    ];
  }

  return Array.from(
    { length: Math.min(20, guestCount) },
    (_, i) => ({

      id: i + 1,

      name:
        randomFrom(names),

      contact:
        `+91 98${Math.floor(
          10000000 + Math.random() * 90000000
        )}`,

      meal:
        randomFrom([
          "Veg",
          "Non-Veg",
          "Vegan"
        ]),

      status:
        randomFrom([
          "Confirmed",
          "Pending"
        ])
    })
  );
};

/* ========================================
   VENDOR GENERATOR
======================================== */

export const generateVendors = (
  eventType
) => {

  const type =
    eventType.toLowerCase();

  if (
    type.includes("ai") ||
    type.includes("tech") ||
    type.includes("hackathon")
  ) {

    return [

      {
        name: "Tech Arena Solutions",
        category: "Infrastructure",
        rating: 4.9,
        status: "Confirmed"
      },

      {
        name: "UltraNet WiFi",
        category: "Networking",
        rating: 4.8,
        status: "Confirmed"
      },

      {
        name: "FutureStage AV",
        category: "Stage & Audio",
        rating: 4.7,
        status: "Pending"
      },

      {
        name: "CyberSecure Systems",
        category: "Security",
        rating: 4.8,
        status: "Confirmed"
      }
    ];
  }

  if (
    type.includes("wedding")
  ) {

    return [

      {
        name: "Royal Caterers",
        category: "Catering",
        rating: 4.9,
        status: "Confirmed"
      },

      {
        name: "Dream Photography",
        category: "Photography",
        rating: 4.8,
        status: "Confirmed"
      },

      {
        name: "Floral Palace",
        category: "Decoration",
        rating: 4.7,
        status: "Pending"
      }
    ];
  }

  if (
    type.includes("music") ||
    type.includes("concert")
  ) {

    return [

      {
        name: "BassBoost Audio",
        category: "Sound",
        rating: 4.9,
        status: "Confirmed"
      },

      {
        name: "Stage Vision",
        category: "Lighting",
        rating: 4.8,
        status: "Confirmed"
      },

      {
        name: "Live Arena",
        category: "Stage Setup",
        rating: 4.7,
        status: "Pending"
      }
    ];
  }

  return [

    {
      name: "Smart Events",
      category: "Management",
      rating: 4.8,
      status: "Confirmed"
    }
  ];
};

/* ========================================
   TIMELINE GENERATOR
======================================== */

export const generateTimeline = (
  eventType
) => {

  const type =
    eventType.toLowerCase();

  if (
    type.includes("ai") ||
    type.includes("tech") ||
    type.includes("hackathon")
  ) {

    return [

      {
        title:
          "Venue Booking Completed",

        desc:
          "Convention center reserved successfully",

        status:
          "Completed",

        progress:
          100,

        agent:
          "Venue Agent"
      },

      {
        title:
          "Speaker Coordination",

        desc:
          "AI keynote speakers invited",

        status:
          "In Progress",

        progress:
          70,

        agent:
          "Speaker Agent"
      },

      {
        title:
          "Startup Booth Setup",

        desc:
          "Startup booth allocation ongoing",

        status:
          "Pending",

        progress:
          35,

        agent:
          "Booth Agent"
      },

      {
        title:
          "Networking Lounge",

        desc:
          "Investor networking zone pending",

        status:
          "Pending",

        progress:
          20,

        agent:
          "Networking Agent"
      }
    ];
  }

  if (
    type.includes("wedding")
  ) {

    return [

      {
        title:
          "Venue Finalized",

        desc:
          "Luxury wedding venue confirmed",

        status:
          "Completed",

        progress:
          100,

        agent:
          "Venue Agent"
      },

      {
        title:
          "Decoration Planning",

        desc:
          "Luxury floral setup ongoing",

        status:
          "In Progress",

        progress:
          75,

        agent:
          "Decoration Agent"
      },

      {
        title:
          "Catering Finalization",

        desc:
          "Menu tasting pending",

        status:
          "Pending",

        progress:
          40,

        agent:
          "Catering Agent"
      },

      {
        title:
          "Guest Invitation Delivery",

        desc:
          "VIP invitation delivery active",

        status:
          "Pending",

        progress:
          25,

        agent:
          "Guest Agent"
      }
    ];
  }

  if (
    type.includes("music") ||
    type.includes("concert")
  ) {

    return [

      {
        title:
          "Stage Construction",

        desc:
          "Main concert stage completed",

        status:
          "Completed",

        progress:
          100,

        agent:
          "Stage Agent"
      },

      {
        title:
          "Lighting Synchronization",

        desc:
          "Laser and lighting sync active",

        status:
          "In Progress",

        progress:
          68,

        agent:
          "Lighting Agent"
      },

      {
        title:
          "Artist Coordination",

        desc:
          "Performer scheduling ongoing",

        status:
          "Pending",

        progress:
          35,

        agent:
          "Artist Agent"
      }
    ];
  }

  return [

    {
      title:
        "Event Created",

      desc:
        "Event initialized successfully",

      status:
        "Completed",

      progress:
        100,

      agent:
        "Supervisor Agent"
    }
  ];
};

/* ========================================
   WORKFLOW AGENTS
======================================== */

export const generateWorkflowAgents = (
  eventType
) => {

  const type =
    eventType.toLowerCase();

  if (
    type.includes("ai") ||
    type.includes("tech") ||
    type.includes("hackathon")
  ) {

    return [

      {
        name: "Supervisor Agent",
        desc:
          "Managing AI summit orchestration"
      },

      {
        name: "Speaker Agent",
        desc:
          "Handling keynote speaker coordination"
      },

      {
        name: "Networking Agent",
        desc:
          "Optimizing attendee networking"
      },

      {
        name: "Infrastructure Agent",
        desc:
          "Managing stage and internet systems"
      },

      {
        name: "Security Agent",
        desc:
          "Monitoring cybersecurity and access"
      }
    ];
  }

  if (
    type.includes("wedding")
  ) {

    return [

      {
        name: "Supervisor Agent",
        desc:
          "Managing luxury wedding execution"
      },

      {
        name: "Venue Agent",
        desc:
          "Handling venue coordination"
      },

      {
        name: "Decoration Agent",
        desc:
          "Managing floral and stage decor"
      },

      {
        name: "Guest Agent",
        desc:
          "Managing guest hospitality"
      },

      {
        name: "Catering Agent",
        desc:
          "Coordinating food operations"
      }
    ];
  }

  if (
    type.includes("music") ||
    type.includes("concert")
  ) {

    return [

      {
        name: "Supervisor Agent",
        desc:
          "Managing concert execution"
      },

      {
        name: "Stage Agent",
        desc:
          "Handling concert stage operations"
      },

      {
        name: "Lighting Agent",
        desc:
          "Managing live lighting systems"
      },

      {
        name: "Artist Agent",
        desc:
          "Coordinating performers"
      },

      {
        name: "Crowd Agent",
        desc:
          "Managing audience safety"
      }
    ];
  }

  return [

    {
      name: "Supervisor Agent",
      desc:
        "Managing event orchestration"
    },

    {
      name: "Operations Agent",
      desc:
        "Handling event operations"
    }
  ];
};

/* ========================================
   BUDGET GENERATOR
======================================== */

export const generateBudgetPlan = (
  budget,
  eventType
) => {

  const type =
    eventType.toLowerCase();

  let venue = 0;

  let catering = 0;

  let decoration = 0;

  let security = 0;

  let entertainment = 0;

  if (
    type.includes("ai") ||
    type.includes("tech") ||
    type.includes("hackathon")
  ) {

    venue =
      Math.floor(budget * 0.30);

    catering =
      Math.floor(budget * 0.20);

    decoration =
      Math.floor(budget * 0.15);

    security =
      Math.floor(budget * 0.15);

    entertainment =
      Math.floor(budget * 0.20);
  }

  else if (
    type.includes("wedding")
  ) {

    venue =
      Math.floor(budget * 0.35);

    catering =
      Math.floor(budget * 0.30);

    decoration =
      Math.floor(budget * 0.20);

    security =
      Math.floor(budget * 0.05);

    entertainment =
      Math.floor(budget * 0.10);
  }

  else if (
    type.includes("music") ||
    type.includes("concert")
  ) {

    venue =
      Math.floor(budget * 0.25);

    catering =
      Math.floor(budget * 0.15);

    decoration =
      Math.floor(budget * 0.20);

    security =
      Math.floor(budget * 0.15);

    entertainment =
      Math.floor(budget * 0.25);
  }

  else {

    venue =
      Math.floor(budget * 0.30);

    catering =
      Math.floor(budget * 0.25);

    decoration =
      Math.floor(budget * 0.15);

    security =
      Math.floor(budget * 0.10);

    entertainment =
      Math.floor(budget * 0.20);
  }

  return {

    venue_cost:
      venue,

    catering_cost:
      catering,

    decoration_cost:
      decoration,

    security_cost:
      security,

    entertainment_cost:
      entertainment,

    total_estimated_cost:
      budget
  };
};

/* ========================================
   AI INSIGHTS
======================================== */

export const generateInsights = (
  eventType,
  guestCount,
  theme,
  budget = 0
) => {

  const insights = [];

  /* Attendance */

  insights.push(
    `Expected attendance: ${guestCount} guests`
  );

  /* Budget */

  insights.push(
    `Budget allocated: Rs. ${Number(
      budget
    ).toLocaleString()}`
  );

  /* Crowd Risk */

  if (guestCount >= 1500) {

    insights.push(
      "Crowd density risk evaluated as high"
    );

  } else if (guestCount >= 500) {

    insights.push(
      "Moderate crowd management required"
    );

  } else {

    insights.push(
      "Crowd density risk evaluated as low"
    );
  }

  /* Venue Complexity */

  if (guestCount > 2000) {

    insights.push(
      "Venue complexity detected as extreme"
    );

  } else if (guestCount > 1000) {

    insights.push(
      "Venue complexity detected as high"
    );

  } else {

    insights.push(
      "Venue complexity detected as manageable"
    );
  }

  /* Event Specific */

  const type =
    eventType.toLowerCase();

  if (
    type.includes("music") ||
    type.includes("concert")
  ) {

    insights.push(
      "High-capacity sound backup recommended"
    );

    insights.push(
      "Peak audience expected during evening performances"
    );

    insights.push(
      "Emergency evacuation planning strongly recommended"
    );
  }

  if (
    type.includes("wedding")
  ) {

    insights.push(
      "Guest hospitality coordination is critical"
    );

    insights.push(
      "Photography and catering timelines require synchronization"
    );
  }

  if (
    type.includes("ai") ||
    type.includes("tech") ||
    type.includes("hackathon")
  ) {

    insights.push(
      "High-speed internet redundancy recommended"
    );

    insights.push(
      "Smart badge automation can improve networking efficiency"
    );
  }

  /* Theme */

  if (
    theme?.toLowerCase().includes(
      "luxury"
    )
  ) {

    insights.push(
      "Luxury theme may increase decoration logistics"
    );
  }

  return insights;
};

/* ========================================
   MAIN AI ENGINE
======================================== */

export const generateEventAIData = (
  payload
) => {

  return {

    guests_list:
      generateGuests(
        payload.guests,
        payload.event_type
      ),

    vendors:
      generateVendors(
        payload.event_type
      ),

    timeline:
      generateTimeline(
        payload.event_type
      ),

    insights:
      generateInsights(
        payload.event_type,
        payload.guests,
        payload.theme,
        payload.budget
      ),

    workflow_agents:
      generateWorkflowAgents(
        payload.event_type
      ),

    budget_plan:
      generateBudgetPlan(
        payload.budget,
        payload.event_type
      )
  };
};