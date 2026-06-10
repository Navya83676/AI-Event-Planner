import BudgetPieChart from "../components/charts/BudgetPieChart";
import "../styles/dashboard.css";

import {
  FaUsers,
  FaBolt,
  FaCheckCircle,
  FaMoneyBillWave,
  FaBell,
  FaClock,
} from "react-icons/fa";

import { useContext } from "react";

import { EventContext } from "../context/EventContext";

export default function Dashboard() {

  const {
    eventData,
    activities
  } = useContext(EventContext);

  /* =========================
     FORMATTERS
  ========================= */

  const formatText = (
    text = ""
  ) => {

    return text

      .replaceAll("_", " ")

      .replace(/\b\w/g, (char) =>
        char.toUpperCase()
      );
  };

  /* =========================
     EMPTY STATE
  ========================= */

  if (!eventData) {

    return (

      <div className="dashboard page-container empty-dashboard">

        <h2>
          Loading Event Data...
        </h2>

      </div>
    );
  }

  /* =========================
     SAFE DATA
  ========================= */

  const vendors =

    Array.isArray(
      eventData?.vendors
    )

      ? eventData.vendors

      : [];

  

  /* =========================
     TIMELINE DATA
  ========================= */

  const timelineData =
  eventData?.timeline || {};

const timeline =

  Array.isArray(
    timelineData?.event
  )

    ? timelineData.event.map(
        (item) => ({

          title:
            item?.title ||
            item?.activity ||
            item,

          time:
            item?.time ||
            "Scheduled"
        })
      )

    : [];

    console.log(
      "RAW TIMELINE DATA",
      JSON.stringify(
        eventData?.timeline,
        null,
        2
      )
    );

    console.log(
      "DASHBOARD TIMELINE",
      timeline
    );

console.log(
  "TIMELINE COUNT",
  timeline.length
);
  const timelineItems = timeline.length;

  const budgetPlan =

    eventData?.workflowData
      ?.budgetPlan ||

    eventData?.budgetPlan ||

    {};

  /* =========================
     ANALYTICS
  ========================= */

  
const totalBudget =
  Number(eventData?.budget || 0);

const budgetPercentages = Object.entries(
  budgetPlan
)
.filter(
  ([key, value]) =>

    ![
      "tool_recommendation",
      "error",
      "remaining_budget",
      "total_estimated_cost",
      "reserve_cost"
    ].includes(key)

    && Number(value) > 0
)
.map(([key, value]) => ({

  name: formatText(key),

  percentage: (
    (Number(value) / totalBudget) * 100
  ).toFixed(1)

}));
  const dashboardData = {

    name:
      eventData?.eventName ||
      "AI Event",

    type:
      `${eventData?.eventType || "AI Event"} Experience`,

    budget:
      `₹${Number(
        eventData?.budget || 0
      ).toLocaleString()}`,

    guests:
      Number(
        eventData?.guests || 0
      ),

    vendors:

      vendors.length ||

      eventData?.workflowData
      ?.vendors?.length ||

      0,

    timeline: timelineItems,

    remainingBudget:

      eventData?.budgetPlan
        ?.remaining_budget ||

      eventData?.workflowData
        ?.budgetPlan
        ?.remaining_budget ||

      0,
  };

  /* =========================
     STATS
  ========================= */

  const stats = [

    {
      title: "Budget",
      value: dashboardData.budget,
      icon: <FaMoneyBillWave />,
      className: "green",
    },

    {
      title: "Guests",
      value: dashboardData.guests,
      icon: <FaUsers color="#93c5fd" />,
      className: "blue",
    },

    {
      title: "Vendors",
      value: dashboardData.vendors,
      icon: <FaCheckCircle color="#fdba74" />,
      className: "orange",
    },

    {
      title: "Timeline",
      value: dashboardData.timeline,
      icon: <FaClock />,
      className: "purple",
    },
    
  ];

  return (

    <div className="dashboard page-container">

      {/* TOPBAR */}

      <div className="topbar">

        <div>

          <h1 className="dashboard-title">
            {dashboardData.name}
          </h1>

          <p className="page-subtitle">
            {dashboardData.type}
          </p>

        </div>

        <div className="online-box">

          <div className="online-dot"></div>

          <span>
            System Online
          </span>

        </div>

      </div>

      {/* STATS */}

      <div className="stats-grid">

        {

          stats.map(
            (
              item,
              index
            ) => (

              <div
                className={`stat-card ${
                  item.title === "Budget"
                    ? "budget-card"
                    : ""
                }`}
                key={index}
              >

                <div
                  className={`stat-icon ${item.className}`}
                >
                  {item.icon}
                </div>

                <div>

                  <p className="stat-label">
                    {item.title}
                  </p>

                  <h2
                    className={
                      item.title === "Budget"
                        ? "stat-value budget-value"
                        : "stat-value"
                    }
                  >
                    {item.value}
                  </h2>

                </div>

              </div>
            )
          )
        }

      </div>

      {/* MAIN GRID */}

      <div className="main-grid">

        {/* LEFT */}

        <div className="left-column">

          {/* EVENT OVERVIEW */}

          <div className="card">

            <div className="card-head">

              <h2>
                Event Overview
              </h2>

            </div>

            <div className="overview-grid">

              <div className="overview-item">

                <span>
                  Event Type
                </span>

                <strong>
                  {eventData?.eventType || "N/A"}
                </strong>

              </div>

              <div className="overview-item">

                <span>
                  Venue
                </span>

                <strong>
                  {eventData?. venue?.venue_name ||
                    eventData?.venueName ||
                    "Venue Pending"
                    }
                </strong>

              </div>

              <div className="overview-item">

                  <span>
                    Venue Capacity
                  </span>

                  <strong>

                      {
                        eventData?.venue
                           ?.capacity || 0
                      }

                  </strong>

              </div>
              <div className="overview-item">

                  <span>
                    Event Date
                  </span>

                  <strong>
                      {eventData?.eventDate || "N/A"}
                  </strong>

              </div>

              <div className="overview-item">

                <span>
                  Guests
                </span>

                <strong>
  {
    Number(
      eventData?.guests || 0
    )
  }
</strong>

              </div>

              <div className="overview-item">

                <span>
                  Vendors
                </span>

                <strong>
                  {vendors.length}
                </strong>

              </div>

              <div className="overview-item">

  <span>
    Budget
  </span>

  <strong>

    ₹

    {Number(
      eventData?.budget || 0
    ).toLocaleString()}

  </strong>

</div>

            </div>

          </div>

          {/* TIMELINE PREVIEW */}

          <div className="card timeline-preview-card">

            <div className="card-head">

              <h2>
                Upcoming Schedule
              </h2>

              <FaClock />

            </div>

            <div className="timeline-preview-list">

              {

                timeline.length > 0

                  ? timeline
                      .slice(0, 3)

                      .map(
                        (
                          item,
                          index
                        ) => (

                          <div
                            className="preview-item"
                            key={index}
                          >

                            <div className="preview-dot"></div>

                            <div>

                              <h4>
                                 {
                                    typeof item.title === "object"
                                       ? item.title?.day
                                       : item.title
                                  }
                              </h4>

                              <p>
                                {item.time}
                              </p>

                            </div>

                          </div>
                        )
                      )

                  : (

                    <p>
                      No upcoming schedule available
                    </p>
                  )
              }

            </div>

          </div>

        </div>

        {/* RIGHT */}

        <div className="right-column">

          {/* BUDGET */}

          <div className="card">

            <div className="card-head">

              <h2>
                Budget Allocation
              </h2>

              <FaMoneyBillWave />

            </div>
            <BudgetPieChart />
            

           <div className="budget-list">

            {budgetPercentages.map((item, index) => (

              <div
                 className={`budget-row budget-color-${index + 1}`}
                  key={index}
              >

                <span>
                   {item.name}
                </span>

                <strong>
                    {item.percentage}%
                </strong>

              </div>

          ))}

        </div>

          </div>
      

          {/* ACTIVITY */}

          <div className="card">

            <div className="card-head">

              <h2>
                Recent Activity
              </h2>

              <FaBell />

            </div>

            <div className="activity-feed">

              {

                activities.length > 0

                  ? activities

                      .slice(0, 5)

                      .map(
                        (activity) => (

                          <div
                            className="activity-item"
                            key={activity.id}
                          >

                            <div className="activity-dot"></div>

                            <div>

                              <h4>
                                {activity.text}
                              </h4>

                              <p>
                                {activity.time}
                              </p>

                            </div>

                          </div>
                        )
                      )

                  : (

                    <p>
                      No recent activities
                    </p>
                  )
              }

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}