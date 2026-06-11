import axios from "axios";

/* =========================
   AXIOS INSTANCE
========================= */

const API = axios.create({

  baseURL: "https://ai-event-planner-sjgz.onrender.com",

  headers: {
    "Content-Type":
      "application/json"
  }

});

/* =========================
   GENERATE EVENT PLAN
========================= */

export const generateEventPlan =
  async (eventData) => {

    try {

      console.log(
        "GENERATE PAYLOAD:",
        eventData
      );

      const response =
        await API.post(
          "/generate",
          eventData
        );

      console.log(
        "GENERATE RESPONSE:",
        response.data
      );

      return response.data;

    } catch (error) {

      console.log(
        "GENERATE ERROR:",
        error
      );

      throw error;
    }
};

/* =========================
   DOWNLOAD REPORT
========================= */

export const downloadReport =
  async (eventData) => {

    try {

      const response =
        await API.post(

          "/download-report",

          eventData,

          {
            responseType: "blob"
          }
        );

      return response.data;

    } catch (error) {

      console.log(
        "DOWNLOAD REPORT ERROR:",
        error
      );

      throw error;
    }
};

/* =========================
   GET ALL EVENTS
========================= */

export const getAllEvents =
  async () => {

    try {

      const response =
        await API.get(
          "/events"
        );

      console.log(
        "ALL EVENTS:",
        response.data
      );

      return response.data;

    } catch (error) {

      console.log(
        "GET EVENTS ERROR:",
        error
      );

      throw error;
    }
};

/* =========================
   GET SINGLE EVENT
========================= */

export const getSingleEvent =
  async (id) => {

    try {

      const response =
        await API.get(
          `/events/${id}`
        );

      console.log(
        "SINGLE EVENT:",
        response.data
      );

      return response.data;

    } catch (error) {

      console.log(
        "GET SINGLE EVENT ERROR:",
        error
      );

      throw error;
    }
};

/* =========================
   DELETE EVENT
========================= */

export const deleteEvent =
  async (id) => {

    try {

      const response =
        await API.delete(
          `/events/${id}`
        );

      console.log(
        "DELETE RESPONSE:",
        response.data
      );

      return response.data;

    } catch (error) {

      console.log(
        "DELETE EVENT ERROR:",
        error
      );

      throw error;
    }
};

/* =========================
   DEFAULT EXPORT
========================= */

export default API;