import { useState, useContext } from "react";

import { EventContext } from "../context/EventContext";

import { generateEventPlan } from "../services/api";

function NewEvent() {

  const { setEventData } = useContext(EventContext);

  const [formData, setFormData] = useState({

    customer_name: "",

    event_name: "",

    event_type: "",

    guests: "",

    budget: "",

    venue: "",

    event_date: "",


    requirements: ""

  });

  const handleChange = (e) => {

    setFormData({

      ...formData,

      [e.target.name]: e.target.value

    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      // =========================
      // API CALL
      // =========================

      const response = await generateEventPlan(formData);

console.log(
  "API RESPONSE:",
  response
);

console.log(
  "EVENT DATA:",
  response?.data
);

// =========================
// SAVE TO CONTEXT
// =========================

if (
  response?.success &&
  response?.data
) {

  setEventData(
    response.data
  );

  alert(
    "Event Generated Successfully"
  );

} else {

  alert(
    "Invalid API Response"
  );
}

    } catch (error) {

      console.log(error);

      alert("Something went wrong");

    }

  };

  return (

    <div>

      <h1>Create Event</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="customer_name"
          placeholder="Customer Name"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="text"
          name="event_name"
          placeholder="Event Name"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="text"
          name="event_type"
          placeholder="Event Type"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="number"
          name="guests"
          placeholder="Guests"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="number"
          name="budget"
          placeholder="Budget"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="text"
          name="venue"
          placeholder="Venue"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="date"
          name="event_date"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="text"
          name="theme"
          placeholder="Theme"
          onChange={handleChange}
        />

        <br /><br />

        <textarea
          name="requirements"
          placeholder="Requirements"
          onChange={handleChange}
        />

        <br /><br />

        <button type="submit">

          Generate Event

        </button>

      </form>

    </div>

  );

}

export default NewEvent;