const API_BASE_URL = "http://127.0.0.1:8000";

export const generateEventPlan = async (eventData) => {

  try {

    const response = await fetch(
      `${API_BASE_URL}/generate`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify(eventData)
      }
    );

    const data = await response.json();

    return data;

  } catch (error) {

    console.error(
      "Backend API Error:",
      error
    );

    return {
      success: false,
      error: "Failed to connect to backend"
    };
  }
};