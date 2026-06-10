import fashion1 from "../assets/fashion/fashion1.jpeg";
import fashion2 from "../assets/fashion/fashion2.png";
import fashion3 from "../assets/fashion/fashion3.jpg";

import gaming1 from "../assets/gaming/gaming1.jpeg";
import gaming2 from "../assets/gaming/gaming2.jpeg";
import gaming3 from "../assets/gaming/gaming3.avif";


import conference1 from "../assets/conference/conference1.jpeg";
import conference2 from "../assets/conference/conference2.jpeg";
import conference3 from "../assets/conference/conference3.jpeg";

import wedding1 from "../assets/wedding/wedding1.jpeg";
import wedding2 from "../assets/wedding/wedding2.jpeg";
import wedding3 from "../assets/wedding/wedding3.jpeg";

// Startup
import startup1 from "../assets/startup/startup1.jpeg";
import startup2 from "../assets/startup/startup2.jpeg";
import startup3 from "../assets/startup/startup3.jpeg";

// Music Festival
import music1 from "../assets/music/music1.jpeg";
import music2 from "../assets/music/music2.jpeg";
import music3 from "../assets/music/music3.jpeg";

// Hackathon
import hackathon1 from "../assets/hackathon/hackathon1.jpeg";
import hackathon2 from "../assets/hackathon/hackathon2.jpeg";
import hackathon3 from "../assets/hackathon/hackathon3.jpeg";

const createVendor = (
  name,
  category,
  rating,
  status
) => ({

  id:
    crypto.randomUUID(),

  name,

  category,

  rating:
    Number(rating),

  status
});

const eventThemes = {

  gaming: {

    keywords: [

      "gaming tournament",
      "gaming",
      "esports",
      "battle arena",
      "championship",
      "lan event"
    ],

    images: [
      gaming1,
      gaming2,
      gaming3
    ],

    primary: "#7c3aed",

    vibe:
      "Cyberpunk Esports Experience",

   vendors: [

  createVendor(
    "BattleZone Esports",
    "Tournament",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "RGB Stage Works",
    "Lighting",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "UltraNet WiFi",
    "Networking",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Gaming Arena Setup",
    "Infrastructure",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "Stream Masters",
    "Live Streaming",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Pro Security",
    "Security",
    4.7,
    "Confirmed"
  )
],

    insights: [

      "High-speed internet redundancy required",

      "Live streaming setup recommended",

      "RGB lighting synchronization enabled"
    ]
  },

  fashion: {

    keywords: [

      "fashion show",
      "fashion",
      "runway",
      "model",
      "designer"
    ],

      images: [

        fashion1,

        fashion2,

        fashion3

      ],

    primary: "#ec4899",

    vibe:
      "Luxury Fashion Experience",

   vendors: [

  createVendor(
    "Runway Studios",
    "Fashion",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "Elite Model Agency",
    "Models",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Luxury Lighting Pro",
    "Lighting",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Glam Makeup Artists",
    "Makeup",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "Fashion Lens Photography",
    "Photography",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Premium Stage Designers",
    "Runway Setup",
    4.7,
    "Confirmed"
  ),

  createVendor(
    "VIP Event Security",
    "Security",
    4.8,
    "Confirmed"
  )
],

    insights: [

  "VIP front-row seating recommended",

  "Runway spotlight optimization enabled",

  "Backstage model coordination activated",

  "Media coverage area recommended",

  "Fashion photography zones optimized"
]
  },

  conference: {

    keywords: [

      "ai summit",
      "ai conference",
      "technology summit",
      "tech summit",
      "tech conference",
      "conference",
      "corporate event",
      "business expo",
      "expo",
      "seminar",
      "summit",
      "business summit",
      "leadership summit"

    ],

  images: [

    conference1,
    conference2,
    conference3
  ],


    primary: "#2563eb",

    vibe:
      "Corporate Intelligence",

   vendors: [

  createVendor(
    "Elite AV Systems",
    "Audio Visual",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Business Connect",
    "Networking",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Event Registration Pro",
    "Registration",
    4.7,
    "Confirmed"
  ),

  createVendor(
    "Conference Catering",
    "Catering",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Summit Security",
    "Security",
    4.7,
    "Confirmed"
  ),

  createVendor(
    "Tech Stage Solutions",
    "Stage Setup",
    4.9,
    "Confirmed"
  )
],

    insights: [

      "Networking lounge recommended",

      "Presentation backup systems required"
    ]
  },

  startup: {

    keywords: [

      "startup meetup",
      "startup",
      "innovation",
      "pitch event",
      "founder meetup",
      "entrepreneur",
      "startup conference"
    ],

    images: [

      startup1,
      startup2,
      startup3
      
    ],

    primary: "#0f172a",

    vibe:
      "Innovation Hub",

    vendors: [

  createVendor(
    "Pitch Masters",
    "Presentation",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Startup Connect",
    "Networking",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "Investor Relations Hub",
    "Investor Management",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Founders Registration Pro",
    "Registration",
    4.7,
    "Confirmed"
  ),

  createVendor(
    "Innovation AV Systems",
    "Audio Visual",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Startup Catering Services",
    "Catering",
    4.7,
    "Confirmed"
  ),

  createVendor(
    "Pitch Event Photography",
    "Photography",
    4.8,
    "Confirmed"
  )
],

    insights: [

  "Investor networking zone recommended",

  "Pitch-stage lighting optimization enabled",

  "Founder showcase area activated",

  "Startup exhibition booths recommended",

  "Investor-founder matching enabled"
]
  },


 
    wedding: {

  keywords: [

    "wedding",
    "marriage",
    "royal wedding",
    "engagement",
    "reception",
    "bridal",
    "groom",
    "royal gold",
    "wedding ceremony"
  ],

 images: [
  wedding1,
  wedding2,
  wedding3
],

  primary: "#c084fc",

  vibe:
    "Royal Wedding Experience",

  vendors: [

    createVendor(
      "Royal Caterers",
      "Catering",
      4.9,
      "Confirmed"
    ),

    createVendor(
      "Elite Decor Studio",
      "Decoration",
      4.8,
      "Confirmed"
    ),

    createVendor(
      "Grand Palace Venues",
      "Venue",
      4.9,
      "Confirmed"
    ),

    createVendor(
      "Wedding Lens Pro",
      "Photography",
      4.8,
      "Confirmed"
    ),

    createVendor(
      "Secure Events India",
      "Security",
      4.7,
      "Confirmed"
    )
  ],

  insights: [

    "Venue optimized for 500 guests",

    "VIP guest management activated",

    "Premium catering allocation approved",

    "Wedding timeline optimized",

    "Photography coverage fully planned"
  ]
},

  music: {

    keywords: [

      "music festival",
      "concert",
      "dj",
      "live show",
      "live music",
      "music concert",
      "cultural festival"
    ],

    images: [
      music1,
      music2,
      music3
      
      
    ],

    primary: "#7c3aed",

    vibe:
      "Festival Energy",

    vendors: [

  createVendor(
    "BassBoost Audio",
    "Sound",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "Live Stage Works",
    "Stage Setup",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Concert Lighting Pro",
    "Lighting",
    4.9,
    "Confirmed"
  ),

  createVendor(
    "Star Artist Management",
    "Artists",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "Festival Security Force",
    "Security",
    4.7,
    "Confirmed"
  ),

  createVendor(
    "Food Street Catering",
    "Food & Beverage",
    4.8,
    "Confirmed"
  ),

  createVendor(
    "LiveStream Media",
    "Broadcasting",
    4.8,
    "Confirmed"
  )
],

   insights: [

  "Crowd management strategy activated",

  "Premium sound system configured",

  "Concert lighting synchronization enabled",

  "Food court planning completed",

  "Artist backstage arrangements prepared",

  "Live streaming infrastructure enabled",

  "Emergency response team allocated"
]
  },

  hackathon: {

  keywords: [

    "hackathon",
    "coding challenge",
    "developer event",
    "programming contest",
    "coding competition",
    "ai hackathon"

  ],

  images: [

    hackathon1,
    hackathon2,
    hackathon3

  ],

  primary: "#0F172A",

  vibe:
    "Innovation Hackathon",

  vendors: [

    createVendor(
      "Hack Arena",
      "Infrastructure",
      4.9,
      "Confirmed"
    ),

    createVendor(
      "Dev Connect",
      "Networking",
      4.8,
      "Confirmed"
    ),

    createVendor(
      "Cloud Labs",
      "Cloud Services",
      4.9,
      "Confirmed"
    )

  ],

  insights: [

    "Coding zones optimized",

    "Mentorship sessions planned",

    "High speed internet redundancy enabled",

    "Team collaboration spaces allocated",

    "Judging workflow configured"

  ]
},


  default: {

    keywords: [],

    images: [

  "https://images.unsplash.com/photo-1511578314322-379afb476865?q=100&w=2400&auto=format&fit=crop"
],

    primary: "#7c3aed",

    vibe:
      "AI Event Experience",

    vendors: [

      createVendor(
        "Smart Events",
        "Management",
        4.8,
        "Confirmed"
      )
    ],

    insights: [

      "Workflow automation active",

      "AI optimization enabled"
    ]
  }
};


export const getEventTheme = (

  eventType = "",
  eventName = "",
  eventTheme = ""

) => {

  const combinedText = `

    ${eventType}
    ${eventName}
    ${eventTheme}

  `.toLowerCase();

const themeOrder = [

  eventThemes.wedding,
  eventThemes.gaming,
  eventThemes.fashion,
  eventThemes.startup,
  eventThemes.hackathon,
  eventThemes.conference,
  eventThemes.music,
  eventThemes.default
];

  const matchedTheme =

    themeOrder.find(
      (theme) =>

        theme.keywords.some(
          (keyword) =>

            combinedText.includes(
              keyword
            )
        )
    ) ||

    eventThemes.default;

  // DETERMINISTIC IMAGE

 let image =
  matchedTheme.images[
    Math.floor(
      Math.random() *
      matchedTheme.images.length
    )
  ];


  let dynamicInsights = [

  ...(matchedTheme.insights || [])
];

if (
  combinedText.includes("vip")
) {

  dynamicInsights.push(
    "VIP guest handling enabled"
  );
}

if (
  combinedText.includes("luxury")
) {

  dynamicInsights.push(
    "Luxury experience optimization applied"
  );
}

if (
  combinedText.includes("premium")
) {

  dynamicInsights.push(
    "Premium service package recommended"
  );
}

if (
  combinedText.includes("security")
) {

  dynamicInsights.push(
    "Enhanced security monitoring recommended"
  );
}

if (
  combinedText.includes("outdoor")
) {

  dynamicInsights.push(
    "Weather contingency planning activated"
  );
}

return {

  ...matchedTheme,

  image,

  insights:
    [...new Set(dynamicInsights)]
};
};

export default eventThemes;