import "../styles/guests.css";

import {
  useState,
  useEffect,
  useContext,
  useMemo
} from "react";

import {
  Search,
  Users,
  Clock3,
  CircleCheck,
  Sparkles,
  TrendingUp
} from "lucide-react";

import {
  EventContext
} from "../context/EventContext";

/* =========================
   DATA POOLS
========================= */

const indianFirstNames = [
  "Rahul",
  "Ananya",
  "Arjun",
  "Sneha",
  "Karan",
  "Priya",
  "Rohan",
  "Neha",
  "Aditya",
  "Meera",
  "Vikram",
  "Aisha",
  "Varun",
  "Pooja",
  "Krishna",
  "Sanjana",
  "Ishaan",
  "Nikhil",
  "Tanya",
  "Akash"
];

const lastNames = [
  "Sharma",
  "Reddy",
  "Patel",
  "Rao",
  "Kapoor",
  "Singh",
  "Agarwal",
  "Naidu",
  "Mehta",
  "Yadav"
];


const mealOptions = [
  "Veg",
  "Non-Veg",
  "Vegan"
];

/* =========================
   GUEST GENERATOR
========================= */

const generateSmartGuests = (
  count,
  eventType = ""
) => {

  const type = eventType.toLowerCase();

  const weddingRoles = [
  "Bride Family",
  "Groom Family",
  "Bride Friend",
  "Groom Friend",
  "Relative",
  "VIP Guest",
  "Family Elder",
  "Close Friend",
  "Special Invitee",
  "Wedding Guest"
];

  const conferenceRoles = [
  "Speaker",
  "Attendee",
  "VIP Delegate",
  "Sponsor Representative",
  "Panelist",
  "Organizer",
  "Media",
  "Volunteer",
  "Industry Expert",
  "Guest"
];

  const musicRoles = [
  "VIP Guest",
  "General Attendee",
  "Artist",
  "Performer",
  "Influencer",
  "Media",
  "Sponsor Representative",
  "Festival Crew",
  "Organizer",
  "Special Guest"
];

  const fashionRoles = [
  "Designer",
  "Model",
  "Judge",
  "Celebrity Guest",
  "Fashion Buyer",
  "Media",
  "Organizer",
  "VIP Guest",
  "Brand Representative",
  "Special Invitee"
];

  const hackathonRoles = [
  "Participant",
  "Team Lead",
  "Mentor",
  "Judge",
  "Organizer",
  "Sponsor",
  "Volunteer",
  "Technical Reviewer",
  "Industry Expert",
  "Guest"
];

  const gamingRoles = [
  "Player",
  "Team Captain",
  "Caster",
  "Streamer",
  "Judge",
  "Organizer",
  "Spectator",
  "VIP Guest",
  "Media",
  "Coach"
];

  const weddingCompanies = [
    "Bride Family",
    "Groom Family",
    "Wedding Services",
    "Family Circle"
  ];

  const conferenceCompanies = [
    "Google",
    "Microsoft",
    "OpenAI",
    "Amazon",
    "Meta",
    "Infosys",
    "TCS",
    "Wipro",
    "Zoho",
    "Adobe"
  ];

  const musicCompanies = [
    "Spotify",
    "Sony Music",
    "Universal Music",
    "Radio Mirchi",
    "Red FM",
    "MTV India",
    "Festival Media",
    "Music Nation"
  ];

  const fashionCompanies = [
    "Zara",
    "H&M",
    "Gucci",
    "Prada",
    "Louis Vuitton",
    "Versace",
    "Dior",
    "Fashion TV"
  ];

  const hackathonCompanies = [
    "Google",
    "Microsoft",
    "OpenAI",
    "Amazon",
    "GitHub",
    "Devfolio",
    "Hack2Skill",
    "Infosys",
    "Zoho",
    "TCS"
  ];

  const gamingCompanies = [
    "Nodwin Gaming",
    "ESL India",
    "ASUS ROG",
    "HyperX",
    "MSI",
    "NVIDIA",
    "Intel Gaming",
    "Red Bull Esports"
  ];


  const weddingAccess = [
  "Family Access",
  "VIP Family Access",
  "Stage Access",
  "Guest Access"
];

const conferenceAccess = [
  "Speaker Access",
  "Attendee Access",
  "VIP Access",
  "Organizer Access"
];

const musicAccess = [
  "General Access",
  "Backstage Access",
  "Media Access",
  "Sponsor Access",
  "Crew Access"
];

const fashionAccess = [
  "Runway Access",
  "Backstage Access",
  "Media Access",
  "VIP Access"
];

const hackathonAccess = [
  "Participant Access",
  "Mentor Access",
  "Judge Access",
  "Organizer Access"
];

const gamingAccess = [
  "Player Access",
  "Caster Access",
  "Media Access",
  "Organizer Access",
  "Spectator Access"
];


const weddingAccessMap = {
  "Bride Family": "Family Access",
  "Groom Family": "Family Access",
  "Bride Friend": "Guest Access",
  "Groom Friend": "Guest Access",
  "Relative": "Family Access",
  "VIP Guest": "VIP Family Access",
  "Family Elder": "Stage Access",
  "Close Friend": "Guest Access",
  "Special Invitee": "VIP Family Access",
  "Wedding Guest": "Guest Access"
};

const conferenceAccessMap = {
  "Speaker": "Speaker Access",
  "Attendee": "Attendee Access",
  "VIP Delegate": "VIP Access",
  "Sponsor Representative": "VIP Access",
  "Panelist": "Speaker Access",
  "Organizer": "Organizer Access",
  "Media": "VIP Access",
  "Volunteer": "Organizer Access",
  "Industry Expert": "VIP Access",
  "Guest": "Attendee Access"
};

const musicAccessMap = {
  "VIP Guest": "VIP Access",
  "General Attendee": "General Access",
  "Artist": "Backstage Access",
  "Performer": "Backstage Access",
  "Influencer": "Media Access",
  "Media": "Media Access",
  "Sponsor Representative": "Sponsor Access",
  "Festival Crew": "Crew Access",
  "Organizer": "Crew Access",
  "Special Guest": "Sponsor Access"
};

const fashionAccessMap = {
  "Designer": "Backstage Access",
  "Model": "Runway Access",
  "Judge": "VIP Access",
  "Celebrity Guest": "VIP Access",
  "Fashion Buyer": "VIP Access",
  "Media": "Media Access",
  "Organizer": "Backstage Access",
  "VIP Guest": "VIP Access",
  "Brand Representative": "VIP Access",
  "Special Invitee": "VIP Access"
};

const hackathonAccessMap = {
  "Participant": "Participant Access",
  "Team Lead": "Participant Access",
  "Mentor": "Mentor Access",
  "Judge": "Judge Access",
  "Organizer": "Organizer Access",
  "Sponsor": "Organizer Access",
  "Volunteer": "Organizer Access",
  "Technical Reviewer": "Judge Access",
  "Industry Expert": "Mentor Access",
  "Guest": "Participant Access"
};

const gamingAccessMap = {
  "Player": "Player Access",
  "Team Captain": "Player Access",
  "Caster": "Caster Access",
  "Streamer": "Media Access",
  "Judge": "Organizer Access",
  "Organizer": "Organizer Access",
  "Spectator": "Spectator Access",
  "VIP Guest": "Organizer Access",
  "Media": "Media Access",
  "Coach": "Player Access"
};

  let roles = [];
  let companies = [];
  let accessTypes = []
;
  if (type.includes("wedding")) {
    roles = weddingRoles;
    companies = weddingCompanies;
    accessTypes = weddingAccess;
  }
  else if (type.includes("conference")) {
    roles = conferenceRoles;
    companies = conferenceCompanies;
    accessTypes = conferenceAccess;
  }
  else if (type.includes("music")) {
    roles = musicRoles;
    companies = musicCompanies;
    accessTypes = musicAccess;
  }
  else if (type.includes("fashion")) {
    roles = fashionRoles;
    companies = fashionCompanies;
    accessTypes = fashionAccess;
  }
  else if (type.includes("hackathon")) {
    roles = hackathonRoles;
    companies = hackathonCompanies;
    accessTypes = hackathonAccess;
  }
  else if (type.includes("gaming")) {
    roles = gamingRoles;
    companies = gamingCompanies;
    accessTypes = gamingAccess;
  }
  else {
    roles = conferenceRoles;
    companies = conferenceCompanies;
    accessTypes = conferenceAccess;
  }

  return Array.from({ length: count }).map((_, index) => {

    const first =
      indianFirstNames[
        Math.floor(
          Math.random() *
          indianFirstNames.length
        )
      ];

    const last =
      lastNames[
        Math.floor(
          Math.random() *
          lastNames.length
        )
      ];

    const role =
      roles[
        Math.floor(
          Math.random() *
          roles.length
        )
      ];

      let specialAccess = "General Access";

      if (type.includes("wedding")) {
        specialAccess = weddingAccessMap[role];
      }
      else if (type.includes("conference")) {
        specialAccess = conferenceAccessMap[role];
      }
      else if (type.includes("music")) {
        specialAccess = musicAccessMap[role];
      }
      else if (type.includes("fashion")) {
        specialAccess = fashionAccessMap[role];
      }
      else if (type.includes("hackathon")) {
        specialAccess = hackathonAccessMap[role];
      }
      else if (type.includes("gaming")) {
        specialAccess = gamingAccessMap[role];
      }


    const company =
      companies[
        Math.floor(
          Math.random() *
          companies.length
        )
      ];

    const fullName =
      `${first} ${last}`;

    const status =
      Math.random() > 0.25
        ? "Confirmed"
        : "Pending";

return {
  id: `guest-${index}-${Date.now()}`,
  name: fullName,
  category: role,
  specialAccess,
  contact: type.includes("wedding")
  ? `${first.toLowerCase()}.${last.toLowerCase()}@gmail.com`
  : `${first.toLowerCase()}.${last.toLowerCase()}@${
      company.toLowerCase().replace(/\s/g, "")
    }.com`,
  meal:
    mealOptions[
      Math.floor(
        Math.random() *
        mealOptions.length
      )
    ],
  status
};
  });
};

export default function Guests() {

  const {
    eventData
  } = useContext(EventContext);

  const [eventInfo, setEventInfo] =
    useState({
      name: "AI Event",
      type: "Conference"
    });

  const [guests, setGuests] =
    useState([]);

  const [search, setSearch] =
    useState("");

  const [currentPage, setCurrentPage] =
    useState(1);

  const [selectedGuest, setSelectedGuest] =
    useState(null);

  const guestsPerPage = 10;



  const eventColor = {

  Wedding: "#ec4899",

  Conference: "#2563eb",

  "Music Festival": "#7c3aed",

  "Fashion Show": "#f97316",

  Hackathon: "#10b981",

  "Gaming Tournament": "#ef4444"

}[eventInfo.type] || "#7c3aed";

  /* =========================
     LOAD
  ========================= */

  useEffect(() => {

    if (eventData) {

      setEventInfo({

        name:
          eventData?.eventName ||
          "AI Event",

        type:
          eventData?.eventType ||
          "Conference"
      });

      if (
  eventData?.guestsList &&
  eventData.guestsList.length > 0
) {

  setGuests(
    eventData.guestsList
  );

} else {

  const guestCount = Math.min(

    Number(
      eventData?.guests
    ) ||

    Number(
      eventData?.expectedGuests
    ) ||

    500,

    2000
  );

  const smartGuests =
    generateSmartGuests(
      guestCount,
      eventData?.eventType
    );

  setGuests(
    smartGuests
  );
}
    }

  }, [eventData]);

  /* =========================
     FILTER
  ========================= */

  const filteredGuests =
  useMemo(() => {

    return guests

      .filter(
        (guest) =>

          [
            guest.name,
            guest.category,
            guest.specialAccess
          ]

            .join(" ")

            .toLowerCase()

            .includes(
              search.toLowerCase()
            )
      )

      .sort((a, b) => {

        if (
          a.status === "Confirmed" &&
          b.status === "Pending"
        ) return -1;

        if (
          a.status === "Pending" &&
          b.status === "Confirmed"
        ) return 1;

        return 0;
      });

  }, [
    guests,
    search
  ]);
  /* =========================
     PAGINATION
  ========================= */

  const totalPages =
    Math.ceil(
      filteredGuests.length /
      guestsPerPage
    );

  const indexOfLastGuest =
    currentPage *
    guestsPerPage;

  const indexOfFirstGuest =
    indexOfLastGuest -
    guestsPerPage;

  const currentGuests =
    filteredGuests.slice(
      indexOfFirstGuest,
      indexOfLastGuest
    );

  /* =========================
     STATS
  ========================= */

  const totalGuests =
    guests.length;

  const confirmedGuests =
    guests.filter(
      (g) =>
        g.status ===
        "Confirmed"
    ).length;

  const pendingGuests =
    guests.filter(
      (g) =>
        g.status ===
        "Pending"
    ).length;


  

  const guestEfficiency =
    totalGuests > 0
      ? Math.round(
          (confirmedGuests / totalGuests) * 100
      )
    : 0;


  return (

    <div className="guests-page">

      <div className="guests-hero">

        <div className="hero-left">

          <div className="hero-badge">

            <Sparkles size={14} />

            AI GUEST MANAGEMENT

          </div>

          <h1>
            {eventInfo.name}
          </h1>

          <p
            style={{
              color: eventColor,
              fontWeight: 600
            }}
          >
            {eventInfo.type}
          </p>

        </div>

      </div>

      {/* STATS */}

      <div className="stats-grid">

        <div className="stat-card">

          <div className="stat-icon purple">

            <Users size={18} />

          </div>

          <div>

            <span>
              Total Guests
            </span>

            <h2>
              {totalGuests}
            </h2>

          </div>

        </div>

        <div className="stat-card">

          <div className="stat-icon green">

            <CircleCheck size={18} />

          </div>

          <div>

            <span>
              Confirmed
            </span>

            <h2>
              {confirmedGuests}
            </h2>

          </div>

        </div>

        <div className="stat-card">

          <div className="stat-icon yellow">

            <Clock3 size={18} />

          </div>

          <div>

            <span>
              Pending
            </span>

            <h2>
              {pendingGuests}
            </h2>

          </div>

        </div>

        

        <div className="stat-card">

          <div className="stat-icon blue">

            <TrendingUp size={18} />

          </div>

        <div>

         <span>
            RSVP Rate
        </span>

        <h2>
          {guestEfficiency}%
        </h2>

    </div>

  </div>

        

      </div>

      {/* SEARCH */}

      <div className="top-controls">

        <div className="search-box">

          <Search size={18} />

          <input
            type="text"
            placeholder="Search guest, category or access..."
            value={search}
            onChange={(e) => {

              setSearch(
                e.target.value
              );

              setCurrentPage(1);
            }}
          />

        </div>

      </div>

      {/* TABLE */}

      <div className="table-wrapper">

        <table>

          <thead>

            <tr>

              <th>Guest Name</th>
              <th>Category</th>
              <th>Access Type</th>
              <th>Status</th>

            </tr>

          </thead>

          <tbody>

            {

              currentGuests.length > 0

                ? currentGuests.map(
                    (guest) => (

                      <tr 
                        key={guest.id}
                        onClick={() =>
                          setSelectedGuest(guest)
                        }
                        className="guest-row"
                        >

                        <td className="guest-name">
                          {guest.name}
                        </td>

                        <td>
                          {guest.category}
                        </td>

                        <td>
                          <span
                            className={`access-badge ${
                              guest.specialAccess
                                .toLowerCase()
                                .replace(/\s/g, "-")
                            }`}
                          >
                            {guest.specialAccess}
                          </span>
                        </td>

          
                        <td>

                          <span
                            className={`status-badge ${
                              guest.status.toLowerCase()
                            }`}
                          >

                            {guest.status}

                          </span>

                        </td>

                      </tr>
                    )
                  )

                : (

                  <tr>

                    <td
                      colSpan="6"
                      className="empty-state"
                    >

                      No guests found

                    </td>

                  </tr>
                )
            }

          </tbody>

        </table>

        {/* FOOTER */}

        <div className="table-footer">

          <div className="footer-left">

            Showing{" "}

            {filteredGuests.length > 0
              ? indexOfFirstGuest + 1
              : 0}

            {" "}to{" "}

            {
              Math.min(
                indexOfLastGuest,
                filteredGuests.length
              )
            }

            {" "}of{" "}

            {filteredGuests.length}

            {" "}entries

          </div>

          <div className="footer-right">

            <button
              className="pagination-btn nav-btn"
              disabled={currentPage === 1}
              onClick={() =>
                setCurrentPage(
                  currentPage - 1
                )
              }
            >
              ‹
            </button>

            {

              (() => {

                const visiblePages = [];

                visiblePages.push(1);

                if (currentPage > 4) {

                  visiblePages.push(
                    "left-dots"
                  );
                }

                for (

                  let i = Math.max(
                    2,
                    currentPage - 1
                  );

                  i <= Math.min(
                    totalPages - 1,
                    currentPage + 1
                  );

                  i++
                ) {

                  visiblePages.push(i);
                }

                if (
                  currentPage <
                  totalPages - 3
                ) {

                  visiblePages.push(
                    "right-dots"
                  );
                }

                if (
                  totalPages > 1 &&
                  ! visiblePages.includes(totalPages)
                ) {

                  visiblePages.push(
                    totalPages
                  );
                }
                const uniquePages = [...new Set(visiblePages)];

                return uniquePages.map(
                  (page, index) => {

                    if (

                      page ===
                        "left-dots" ||

                      page ===
                        "right-dots"
                    ) {

                      return (

                        <span
                          key={index}
                          className="pagination-dots"
                        >
                          ...
                        </span>
                      );
                    }

                    return (

                      <button
                        key={`${page}-${index}`}
                        className={`pagination-btn ${
                          currentPage ===
                          page
                            ? "active"
                            : ""
                        }`}
                        onClick={() =>
                          setCurrentPage(
                            page
                          )
                        }
                      >

                        {page}

                      </button>
                    );
                  }
                );
              })()
            }

            <button
              className="pagination-btn nav-btn"
              disabled={
                currentPage ===
                totalPages
              }
              onClick={() =>
                setCurrentPage(
                  currentPage + 1
                )
              }
            >
              ›
            </button>

          </div>

        </div>

      </div>

      {selectedGuest && (
        <div
          className="guest-modal-overlay"
          onClick={() => setSelectedGuest(null)}
        >
          <div
            className="guest-modal"
            onClick={(e) => e.stopPropagation()}
          >

            <h2>{selectedGuest.name}</h2>

              <p
                style={{
                  marginBottom: "20px",
                  color: "#64748b"
                }}
              >
                {selectedGuest.category}
              </p>

          <div
            className={`access-badge ${
              selectedGuest.specialAccess
                .toLowerCase()
                .replace(/\s/g, "-")
            }`}
          >
            {selectedGuest.specialAccess}
          </div>

            <div className="guest-detail">
              <strong>Category:</strong>
              <span>{selectedGuest.category}</span>
            </div>

            <div className="guest-detail">
              <strong>Access Type:</strong>
              <span>{selectedGuest.specialAccess}</span>
            </div>

            <div className="guest-detail">
              <strong>Meal Preference:</strong>
              <span>{selectedGuest.meal}</span>
            </div>

            <div className="guest-detail">
              <strong>Contact:</strong>
              <span>{selectedGuest.contact}</span>
            </div>
            
            <div className="guest-detail">
              <strong>Status:</strong>
              <span>{selectedGuest.status}</span>
            </div>

            <button
              className="close-modal-btn"
              onClick={() => setSelectedGuest(null)}
            >
              Close
            </button>

          </div>
        </div>
      )}

    </div>
  );
}