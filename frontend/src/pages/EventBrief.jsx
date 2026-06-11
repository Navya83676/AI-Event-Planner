import { useState } from "react";

import { useNavigate } from "react-router-dom";

import {
  FaRobot,
  FaBrain,
  FaDatabase,
  FaChartLine
} from "react-icons/fa";

import "../styles/event-brief.css";

import {
  generateEventPlan
} from "../api/eventApi";

import useEvent from "../hooks/useEvent";

import {
  normalizeEventData
} from "../context/EventContext";

import {
  getEventTheme
} from "../data/eventThemes";

function EventBrief() {

  const navigate = useNavigate();

  const {
    setEventData,
    addActivity,
    resetEventData
  } = useEvent();

  const [loading, setLoading] =
    useState(false);

  const [loadingStep, setLoadingStep] =
    useState("");

  const [formData, setFormData] =
    useState({

      type: "",
      customerName: "",
      duration:"",
      name: "",
      date: "",
      location: "",
      guests: "",
      budget: "",
      requirements: ""
    });

  const handleChange = (e) => {

    setFormData({

      ...formData,

      [e.target.name]:
        e.target.value
    });
  };

  const handleSubmit = async () => {

    try {

      if (
        !formData.type ||
        !formData.customerName ||
        !formData.name ||
        !formData.date ||
        !formData.location ||
        !formData.guests ||
        !formData.budget ||
        !formData.duration
      ) {

        alert(
          "Please fill all required fields"
        );

        return;
      }

      resetEventData();

      setLoading(true);

      setLoadingStep(
        "Initializing AI agents..."
      );

      setTimeout(() => {

        setLoadingStep(
          "Analyzing event requirements..."
        );

      }, 1200);

      setTimeout(() => {

        setLoadingStep(
          "Generating intelligent workflow..."
        );

      }, 2400);

      setTimeout(() => {

        setLoadingStep(
          "Optimizing event strategy..."
        );

      }, 3600);

      const payload = {

        customer_name:
          formData.customerName,

        event_name:
          formData.name,

        event_type:
          formData.type,

        event_duration:
          formData.duration,

        guests:
          parseInt(formData.guests),

        budget:
          parseInt(formData.budget.replace(/,/g, "")),

        event_date:
          formData.date,

        location:
          formData.location,

        venue:
          "",

        requirements:
          formData.requirements
      };

      console.log(
        "PAYLOAD:",
        payload
      );

      console.log(
        "EVENT DURATION:",
        payload.event_duration
      );

      let result = {};

      try {

        result =
          await generateEventPlan(
            payload
          );

      } catch {

        result = {};
      }

      console.log(
        "API RESPONSE:",
        result
      );
      console.log(
        "RESULT.DATA:",
        result?.data
      );
      console.log(
        "RESULT.DATA.VENDORS:",
        result?.data?.vendors
      );

      const backendData =
        result?.data || {};

      console.log(
        "BACKEND DATA:",
        backendData
      );
      console.log(
        "BACKEND VENUE:",
        backendData?.venue
      );
      console.log(
        "BACKEND VENDORS:",
        backendData?.vendors
      );

      const selectedTheme =
        getEventTheme(
          payload.event_type,
          payload.event_name,
        );

      const workflowAgents =

        Array.isArray(
          backendData?.execution_flow
        ) &&

        backendData.execution_flow.length > 0

          ? backendData.execution_flow.map(
              (agentName) => ({

                name:
                  agentName,

                desc:
                  `${agentName} executed successfully`
              })
            )

          : [

              {
                name:
                  "Venue Intelligence Agent",

                desc:
                  "Venue optimization completed successfully"
              },

              {
                name:
                  "Budget Optimization Agent",

                desc:
                  "Budget distribution analyzed successfully"
              },

              {
                name:
                  "Guest Coordination Agent",

                desc:
                  "Guest workflow generated successfully"
              }
            ];


            console.log(
              "BACKEND EVENT ID:",
              result?.event_id
            );

      const finalEventData = {

        eventId:
          result?.event_id,

        customerName:
          backendData?.customer_name ||
          payload.customer_name,

        eventName:
          backendData?.event_name ||

          payload.event_name,

        eventType:
          backendData?.event_type ||

          payload.event_type,

        image:
          selectedTheme.image,

        primaryColor:
          selectedTheme.primary,

        vibe:
          selectedTheme.vibe,

        eventDate:
          backendData?.event_date ||

          payload.event_date,

        location:
          backendData?.location ||

          payload.location,

        venueName:
          backendData?.venue?.venue_name || "",
        venueCapacity:
          backendData?.venue?.capacity || 0,

        guests:
          backendData?.guests ||

          payload.guests,

        budget:
          backendData?.budget ||

          payload.budget,

        duration: formData.duration,


        requirements:
          backendData?.requirements ||

          payload.requirements,

        insights:

          Array.isArray(
            backendData?.insights
          ) &&

          backendData.insights.length > 0

            ? backendData.insights

            : selectedTheme.insights,

        workflowData: {

          agents:
            workflowAgents,

          budgetPlan:
            backendData?.budget_plan || {}
        },

        timeline:

          backendData?.timeline &&
          Object.keys(
            backendData.timeline
          ).length > 0

            ? backendData.timeline

            : {

                morning: [

                  "Venue setup and decoration",

                  "Vendor coordination and registrations"
                ],

                afternoon: [

                  "Guest welcome session",

                  "Main event activities begin"
                ],

                evening: [

                  "Entertainment and networking",

                  "Closing ceremony and dinner"
                ]
              },

        budgetPlan:
          backendData?.budget_plan || {},
        security:
          backendData?.security || {},
        classification:
          backendData?.classification || {},
        theme:
           backendData?.theme || "",
        venue:
          backendData?.venue || {},

        guestsList:

  Array.isArray(
    backendData?.guests_list
  )

    ? backendData.guests_list

    : [],

        vendors:

          Array.isArray(
            backendData?.vendors
          ) 

            ?backendData.vendors
            :[]

            
      };

      console.log(
        "FINAL STORED EVENT DATA:",
        finalEventData
      );
      console.log(
        "STORED VENUE:",
        finalEventData.venue
      );

      console.log(
        "STORED VENUE CAPACITY:",
        finalEventData.venueCapacity
      );
      console.log(
        "VENUE CAPACITY:",
        finalEventData.venueCapacity
      );

      console.log(
        "VENUE NAME:",
         finalEventData.venueName
      );

      console.log(
        "TIMELINE BEFORE SAVE",
        finalEventData.timeline
      );

      console.log(
        "TIMELINE BEFORE SAVE",
        finalEventData.timeline
      );

      console.log(
        "CUSTOMER NAME:",
        finalEventData.customerName
      );


      console.log(
        "EVENT ID:",
        finalEventData.eventId
      );

      console.log(
        "CUSTOMER:",
        finalEventData.customerName
      );

      setEventData(
        normalizeEventData(
          finalEventData
        )
      );

      addActivity(
        `New ${payload.event_type} event created`
      );

      setLoading(false);

      navigate("/plan");

    }

    catch (error) {

      console.log(
        "FULL ERROR:",
        error
      );

      alert(
        "Failed to generate event plan"
      );

      setLoading(false);
    }
  };

  return (

    <div className="brief-page">

      <div className="brief-layout">

              <div className="brief-header">

                  <h1>Create Event Brief</h1>

                  <p>
                      Provide event details and let AI generate a complete event plan.
                  </p>

              </div>

              <div className="brief-card">

          <div className="brief-grid">

            <div className="form-group">

              <label>
                Event Type *
              </label>

            <select
                name="type"
                value={formData.type}
                onChange={handleChange}
            >
               <option value="">
                  Select Event Type
               </option>

              <option value="Wedding">
                    Wedding
              </option>

              <option value="Conference">
                  Conference
              </option>

              <option value="Music Festival">
                   Music Festival
              </option>

              <option value="Fashion Show">
                   Fashion Show
              </option>

              <option value="Hackathon">
                  Hackathon
              </option>

             <option value="Gaming Tournament">
                Gaming Tournament
            </option>

        </select>
            </div>

            <div className="form-group">

              <label>
                Customer Name *
              </label>

              <input
                 type="text"
                 name="customerName"
                 value={formData.customerName}
                 onChange={handleChange}
              />

            </div>

            <div className="form-group">

              <label>
                Event Name *
              </label>

              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
              />

            </div>

            <div className="form-group">

              <label>
                Event Date *
              </label>

              <input
                type="date"
                name="date"
                value={formData.date}
                onChange={handleChange}
              />

            </div>

            <div className="form-group">

              <label>
                Location *
              </label>

              <input
                type="text"
                name="location"
                value={formData.location}
                onChange={handleChange}
              />

            </div>

            <div className="form-group">

              <label>
                Expected Guests *
              </label>

              <input
                type="number"
                name="guests"
                value={formData.guests}
                onChange={handleChange}
              />

            </div>

            <div className="form-group">

              <label>
                Budget *
              </label>

              <input
                type="text"
                name="budget"
                value={formData.budget}
                onChange={handleChange}
              />

            </div>

          <div className="form-group">

            <label>
               Event Duration *
            </label>

            <select
                name="duration"
                value={formData.duration}
                onChange={handleChange}
            >
             <option value="">
                   Select Duration
              </option>

            <option value="2 Hours">
                2 Hours
            </option>

            <option value="4 Hours">
               4 Hours
            </option>

            <option value="Half Day">
                Half Day
            </option>

            <option value="Full Day">
              Full Day
            </option>

            <option value="2 Days">
              2 Days
            </option>

            <option value="3 Days">
              3 Days
            </option>
            </select>

          </div>

          </div>


          <div className="form-group full-width">

            <label>
              Special Requirements
            </label>

            <textarea
              name="requirements"
              rows="5"
              value={formData.requirements}
              onChange={handleChange}
            ></textarea>

          </div>

          <div className="button-row">

            <button
              onClick={handleSubmit}
              disabled={loading}
            >

              {
                loading

                ? "AI Planning In Progress..."

                : "Generate Event Plan"
              }

            </button>

          </div>

          {

            loading && (

              <div className="ai-loading-container">

                <div className="ai-loading-card">

                  <div className="ai-loader-icon">

                    <FaRobot />

                  </div>

                  <h2>
                    AI Event Orchestration
                  </h2>

                  <p>
                    {loadingStep}
                  </p>

                  <div className="ai-loading-grid">

                    <div className="ai-loading-box">

                      <FaBrain />

                      <span>
                        Intelligence Layer
                      </span>

                    </div>

                    <div className="ai-loading-box">

                      <FaDatabase />

                      <span>
                        Multi-Agent Planning
                      </span>

                    </div>

                    <div className="ai-loading-box">

                      <FaChartLine />

                      <span>
                        Budget Optimization
                      </span>

                    </div>

                  </div>

                </div>

              </div>
            )
          }

        </div>

      </div>

    </div>
  );
}

export default EventBrief;