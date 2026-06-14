// EventPlan.jsx

import { useContext } from "react";

import {
  FaCalendarAlt,
  FaMapMarkerAlt,
  FaUsers,
  FaRobot,
  FaCheckCircle,
  FaChartPie,
  FaChartLine
} from "react-icons/fa";

import {
  EventContext
} from "../context/EventContext";

import {
  getEventTheme
} from "../data/eventThemes";

import "../styles/event-plan.css";

function EventPlan() {

  const {
    eventData
  } = useContext(EventContext);

  console.log(
    "PLAN PAGE DATA",
    eventData
  );

 const handleDownloadReport = async () => {

  console.log(
    "SENDING PDF DATA",
    eventData
  );

  console.log("FOOD:", eventData?.food);

  console.log("DECORATION:", eventData?.decoration);

  console.log("ENTERTAINMENT:", eventData?.entertainment);

  console.log("SECURITY:", eventData?.security);

  console.log("TIMELINE:", eventData?.timeline);

  console.log("VENDORS:", eventData?.vendors);

  try {


    const pdfData = {
      ...eventData,
      image:
        eventData?.image ||
        eventThemeData?.image
    };

    console.log("=================================");
    console.log("PDF DATA SENT");
    console.log(pdfData);
    console.log("IMAGE:", pdfData.image);
    console.log("EVENT IMAGE:", eventData?.image);
    console.log("THEME IMAGE:", eventThemeData?.image);
    console.log("=================================");

    console.log("PDF DATA SENT:", pdfData);

    console.log(
      "CURRENT EVENT ID:",
      eventData.eventId
    );


    console.log(
    "PDF EVENT NAME",
    eventData.eventName
    );

    console.log(
      "EVENT ID USED FOR PDF =",
      eventData?.eventId
    );

    const response = await fetch(
      `http://127.0.0.1:8000/events/${eventData.eventId}/report`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify(pdfData)
      }
    );

    console.log(
      "STATUS:",
      response.status
    );

    console.log(
      "CONTENT TYPE:",
      response.headers.get("content-type")
    );


    if (!response.ok) {

      const text = await response.text();

      console.log(text);

      throw new Error(text);
    }

    const blob = await response.blob();

    const url =
      window.URL.createObjectURL(blob);

    const link =
      document.createElement("a");

    link.href = url;

    link.download =
      `${eventData.eventName}_Report.pdf`;

    document.body.appendChild(link);

    link.click();

    link.remove();

  } catch (error) {

    console.error(error);

  }

};
  /* =========================
     EVENT THEME
  ========================= */

  const eventThemeData =
    getEventTheme(

      eventData?.eventType,

      eventData?.eventName,

      eventData?.theme
    );

  /* =========================
     FORMATTER
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

  if (
    !eventData ||
    Object.keys(eventData).length === 0
  ) {

    return (

      <div className="empty-state">

        <h2>
          No Event Data Found
        </h2>

      </div>
    );
  }

  /* =========================
     BUDGET PLAN
  ========================= */

  const budgetPlan =

  eventData?.workflowData
    ?.budgetPlan ||

  eventData?.budgetPlan ||

  {};

console.log(
  "EVENT DATA:",
  eventData
);

console.log(
  "FOOD DATA:",
  eventData?.food
);

console.log(
  "DECORATION DATA:",
  eventData?.decoration
);

console.log(
  "ENTERTAINMENT DATA:",
  eventData?.entertainment
);

console.log(
  "LOCATION VALUE:",
  eventData?.location
);

console.log(
  "BUDGET PLAN:",
  budgetPlan
);

  const venueCost =
    Number(
      budgetPlan?.venue_cost || 0
    );

  const foodCost =
    Number(
      budgetPlan?.food_cost || 0
    );

  const decorationCost =
    Number(
      budgetPlan?.decoration_cost || 0
    );

  const securityCost =
    Number(
      budgetPlan?.security_cost || 0
    );

  const miscellaneousCost =
    Number(
      budgetPlan?.miscellaneous_cost || 0
    );

  const totalBudget =
    Number(
      eventData?.budget || 0
    );
const allocatedBudget =

  venueCost +

  foodCost +

  decorationCost +

  securityCost +

  miscellaneousCost;
const remainingBudget =
  Number(
    budgetPlan?.remaining_budget || 0
  );

  const venuePercent =
  allocatedBudget > 0
    ? Math.round(
        (venueCost / allocatedBudget) * 100
      )
    : 0;

  const foodPercent =
  allocatedBudget > 0
    ? Math.round(
        (foodCost / allocatedBudget) * 100
      )
    : 0;

  const decorationPercent =
  allocatedBudget > 0
    ? Math.round(
        (decorationCost / allocatedBudget) * 100
      )
    : 0;

  const securityPercent =
  allocatedBudget > 0
    ? Math.round(
        (securityCost / allocatedBudget) * 100
      )
    : 0;

    

  /* =========================
     WORKFLOW AGENTS
  ========================= */

  const agents =

    Array.isArray(
      eventData?.workflowData?.agents
    )

      ? eventData.workflowData.agents

      : [];

  /* =========================
     AI INSIGHTS
  ========================= */

  const aiInsights =

  Array.isArray(
    eventData?.insights
  ) &&

  eventData.insights.length > 0

    ? eventData.insights

    : eventThemeData?.insights || [];

  const timelineItems =

  Array.isArray(
    eventData?.timeline?.event
  )

    ? eventData.timeline.event.length

    : 0;

  /* =========================
     READINESS SCORE
  ========================= */

 const readinessScore = Math.min(
  95,

  (

    (eventData?.eventName ? 10 : 0) +

    (eventData?.location ? 10 : 0) +

    (eventData?.eventDate ? 10 : 0) +

    (totalBudget > 0 ? 10 : 0) +

    (eventData?.venue?.venue_name ? 15 : 0) +

    Math.min(
      (eventData?.vendors?.length || 0) * 4,
      20
    ) +

    Math.min(
      agents.length * 3,
      15
    ) +

    (
      Object.keys(budgetPlan).length > 0
        ? 15
        : 0
    ) +

    (
      timelineItems > 0
        ? 15
        : 0
    )

  )
);

const timelineData =
  eventData?.timeline || {};

const morningActivities =
  Array.isArray(timelineData?.morning)
    ? timelineData.morning
    : [];

const afternoonActivities =
  Array.isArray(timelineData?.afternoon)
    ? timelineData.afternoon
    : [];

const eveningActivities =
  Array.isArray(timelineData?.evening)
    ? timelineData.evening
    : [];

const genericActivities =
  Array.isArray(timelineData?.event)
    ? timelineData.event
    : [];

console.log(
  "GENERIC ACTIVITIES",
  genericActivities
);

console.log(
  "TIMELINE STRUCTURE",
  JSON.stringify(
    eventData.timeline,
    null,
    2
  )
);

console.log(
  "EVENT IMAGE = ",
  eventData?.image
);

console.log(
  "THEME IMAGE = ",
  eventThemeData?.image
);


  return (

    <div className="event-page">


      {/* HERO */}

      <div className="event-top-card glass-card">

        <div className="event-left">

          <div className="event-badge">

            <FaRobot />

            <span>
              AI Powered Planning
            </span>

          </div>

          <button
            className="download-report-btn"
            onClick={handleDownloadReport}
          >
               Download AI Report
          </button>

          <h1>
             {eventData?.eventName || "Event Plan"}
          </h1>

          <p>
            {eventData?.theme || "AI-generated execution and optimization strategy"}
          </p>

          <div className="event-details">

            <div>

              <span>

                <FaCalendarAlt />

                Event Overview

              </span>

              <strong>
                {eventData?.eventName}
              </strong>

            </div>

            <div>

              <span>

                <FaCalendarAlt />

                Event Date

              </span>

              <strong>
                {eventData?.eventDate}
              </strong>

            </div>

            <div>

  <span>

    <FaMapMarkerAlt />

    Venue

  </span>

  <strong>

    {eventData?.venue?.venue_name ||

      eventData?.venueName ||

      "Venue Pending"}

  </strong>

</div>

<div>

  <span>

    <FaMapMarkerAlt />

    Location

  </span>

  <strong>

    {eventData?.location ||

      "Location Pending"}

  </strong>

</div>

            <div>

              <span>

                <FaUsers />

                Guests

              </span>

              <strong>
                {eventData?.guests}
              </strong>

            </div>

            <div>

              <span>

                <FaCheckCircle />

                Theme

              </span>

              <strong>
  {
    eventData?.theme ||
    eventThemeData?.vibe ||
    "AI Generated"
  }
</strong>

            </div>

          </div>

        </div>

        <div className="event-right">

          <img
         src={

  eventData?.image ||

  eventThemeData?.image ||

  "https://images.unsplash.com/photo-1511578314322-379afb476865?q=100&w=2400&auto=format&fit=crop"
}

            alt="event"

            onError={(e) => {

              e.target.src =
                "https://images.unsplash.com/photo-1511578314322-379afb476865?q=100&w=2400&auto=format&fit=crop";
            }}
          />

          <div className="readiness-card">

            <div className="readiness-top">

              <FaChartLine />

              <span>
                Event Readiness
              </span>

            </div>

            <h2>
              {readinessScore}%
            </h2>

            <div className="readiness-bar">

              <div
                className="readiness-fill"
                style={{
                  width: `${readinessScore}%`
                }}
              ></div>

            </div>

          </div>

        </div>

      </div>
        
       <div className="timeline-card glass-card">

  <div className="section-title-row">

    <h2>Event Timeline Overview</h2>

    <div className="live-tag">
      {genericActivities.length} Activities
    </div>

  </div>

  <div className="timeline-preview">

  {genericActivities
  .slice(0, 4)
  .map((activity, index) => (

    <div
      className="timeline-preview-item"
      key={index}
    >

      <div className="timeline-number">
        {index + 1}
      </div>

      <div className="timeline-content">

        <h4>
          {
            activity?.day ||
            activity?.title ||
            activity?.activity ||
            activity?.name ||
            "Timeline Activity"
          }
        </h4>

        <span>
          {
            activity?.activities?.length
              ? `${activity.activities.length} Activities`
              : activity?.time || "Scheduled"
          }
        </span>

      </div>

    </div>

))}

</div>

<div className="timeline-footer">

  <span>
    View complete execution timeline progress
  </span>

  <button
    className="timeline-btn"
    onClick={() => window.location.href="/timeline"}
  >
    View Timeline →
  </button>

</div>

</div>   {/* <-- ADD THIS */}


      {/* BUDGET */}

      <div className="plan-highlight-card glass-card">

        <div className="section-title-row">

          <h2>
            Budget Distribution
          </h2>

          <div className="live-tag">
            Optimized
          </div>

        </div>

        <div className="plan-grid">

          <div className="plan-box">

            <span>
              Venue • {venuePercent}%
            </span>

            <h4>
              AI Optimized Venue Allocation
            </h4>

            <strong>
              ₹{venueCost.toLocaleString()}
            </strong>

          </div>

          <div className="plan-box">

            <span>
              Catering • {foodPercent}%
            </span>

            <h4>
              Guest Catering Optimization
            </h4>

            <strong>
              ₹{foodCost.toLocaleString()}
            </strong>

          </div>

          <div className="plan-box">

            <span>
              Decoration • {decorationPercent}%
            </span>

          

            <h4>
              AI Theme Experience Design
            </h4>

            <strong>
              ₹{decorationCost.toLocaleString()}
            </strong>

          </div>

          <div className="plan-box">

            <span>
              Security • {securityPercent}%
            </span>

            <h4>
              Security & Crowd Intelligence
            </h4>

            <strong>
              ₹{securityCost.toLocaleString()}
            </strong>

          </div>
          {/* Miscellaneous */}

  <div className="plan-box">

    <span>
      Miscellaneous
    </span>

    <h4>
      Backup & Contingency
    </h4>

    <strong>
      ₹{miscellaneousCost.toLocaleString()}
    </strong>

  </div>

</div>

        <div className="budget-bottom">

          <div>

            <span>
              Total Budget
            </span>

            <h3>
              ₹{totalBudget.toLocaleString()}
            </h3>

          </div>

          <div>

            <span>
              Contingency Reserve
            </span>

            <h3>
              ₹{remainingBudget.toLocaleString()}
            </h3>

          </div>

        </div>

        <div className="green-line"></div>

      </div>




      
      {/* AI INSIGHTS */}

      <div className="insight-card glass-card">

        <div className="section-title-row">

          <h2>

            <FaChartPie />

            AI Insights

          </h2>

          <div className="live-tag">
            Smart Analysis
          </div>

        </div>

        {

          aiInsights.length > 0

            ? aiInsights.slice(0,8).map(
                (
                  insight,
                  index
                ) => (

                  <div
                    className="insight-item"
                    key={index}
                  >

                    {insight}

                  </div>
                )
              )

            : (

              <div className="insight-item">

                AI analysis ready for this event.

              </div>

              
            )
        }
        </div>


      </div>
  );
}

export default EventPlan;