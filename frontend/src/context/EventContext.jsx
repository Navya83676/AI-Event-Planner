import {
  createContext,
  useEffect,
  useState
} from "react";

export const EventContext =
  createContext();

/* =========================
   SAFE LOCAL STORAGE
========================= */

const getLocalStorage = (
  key,
  fallback
) => {

  try {

    const item =
      localStorage.getItem(key);

    return item
      ? JSON.parse(item)
      : fallback;

  } catch (error) {

    console.error(
      `LocalStorage Error (${key})`,
      error
    );

    return fallback;
  }
};

/* =========================
   DEFAULT EVENT STATE
========================= */

const defaultEventData = {

  eventId: null,

  customerName: "",

  eventName: "",

  eventType: "",

  venue: {},

  venueName: "",

  venueCapacity: 0,

  eventDate: "",


  theme: "",

  requirements: "",

  image: "",

  guests: 0,

  budget: 0,

  location: "",

  vendors: [],

  guestsList: [],

 timeline: {

  event: []
  },

  workflowData: {

    agents: []
  },

  budgetPlan: {},

  security: {},

  classification : {},

  aiInsights: [],

  reports: {},

  metrics: {

    readiness: 0,

    efficiency: 0,

    confirmedGuests: 0,

    pendingGuests: 0
  }
};

/* =========================
   NORMALIZE EVENT DATA
========================= */

export const normalizeEventData = (
  data = {}
) => {

  return {

    ...defaultEventData,

    ...data,

    eventId:
      data?.eventId || null,

    customerName:
       data?.customerName || "",

    venue:
      typeof data?.venue === "object"
      ? data.venue
      : {},

    venueName:
      data?.venueName || "",

    venueCapacity:
      data?.venueCapacity ||

      data?.venue?.capacity ||

      0,

    vendors:
      Array.isArray(data?.vendors)
        ? data.vendors
        : [],


    guestsList:
      Array.isArray(data?.guestsList)
        ? data.guestsList
        : [],

  timeline: data?.timeline || {
  morning: [],
  afternoon: [],
  evening: [],
  event: []
},

    workflowData: {

      agents:
        Array.isArray(
          data?.workflowData?.agents
        )
          ? data.workflowData.agents
          : [],

      budgetPlan:
        data?.workflowData?.budgetPlan || {}
    },

    budgetPlan:
      typeof data?.budgetPlan ===
      "object"

        ? data.budgetPlan

        : {},
    security:
      typeof data?.security === "object"

         ? data.security

          : {},

   classification:
      typeof data?.classification === "object"

        ? data.classification

        : {},
  };
};

export const EventProvider = ({
  children
}) => {

  /* =========================
     MAIN EVENT STATE
  ========================= */

  const [eventData,
    setEventData] =
    useState(() =>

      normalizeEventData(

        getLocalStorage(
          "eventData",
          defaultEventData
        )
      )
    );

  /* =========================
     ACTIVITIES
  ========================= */

  const [activities,
    setActivities] =
    useState(() =>

      getLocalStorage(
        "activities",
        []
      )
    );

  /* =========================
     LOADING + ERROR
  ========================= */

  const [loading,
    setLoading] =
    useState(false);

  const [error,
    setError] =
    useState(null);

  /* =========================
     SAVE TO LOCAL STORAGE
  ========================= */

  useEffect(() => {

    localStorage.setItem(

      "eventData",

      JSON.stringify(eventData)
    );

  }, [eventData]);

  useEffect(() => {

    localStorage.setItem(

      "activities",

      JSON.stringify(activities)
    );

  }, [activities]);

  /* =========================
     RESET EVENT
  ========================= */

  const resetEventData = () => {

    localStorage.removeItem(
      "eventData"
    );

    localStorage.removeItem(
      "activities"
    );

    setEventData(
      defaultEventData
    );

    setActivities([]);

    setError(null);

    setLoading(false);
  };

  /* =========================
     ACTIVITY LOGGER
  ========================= */

  const addActivity = (
    text
  ) => {

    const activity = {

      id:
        crypto.randomUUID(),

      text,

      time:
        new Date()
          .toLocaleTimeString()
    };

    setActivities((prev) => [

      activity,

      ...prev
    ]);
  };

  /* =========================
     TIMELINE FUNCTIONS
  ========================= */

  const addTimelineEvent = (
    period,
    title
  ) => {

    if (
      ![
        "morning",
        "afternoon",
        "evening"
      ].includes(period)
    ) return;

    setEventData((prev) => ({

      ...prev,

      timeline: {

        ...prev.timeline,

        [period]: [

          ...prev.timeline[period],

          title
        ]
      }
    }));

    addActivity(
      "Timeline Event Added"
    );
  };

  const deleteTimelineEvent = (
    period,
    index
  ) => {

    setEventData((prev) => ({

      ...prev,

      timeline: {

        ...prev.timeline,

        [period]:

          prev.timeline[
            period
          ].filter(
            (_, i) =>
              i !== index
          )
      }
    }));

    addActivity(
      "Timeline Event Deleted"
    );
  };

  /* =========================
     VENDOR FUNCTIONS
  ========================= */

  const addVendor = (
    vendor
  ) => {

    const newVendor = {

      id:
        crypto.randomUUID(),

      ...vendor
    };

    setEventData((prev) => ({

      ...prev,

      vendors: [

        ...(prev.vendors || []),

        newVendor
      ]
    }));

    addActivity(
      "Vendor Added"
    );
  };

  const updateVendor = (
    id,
    updatedData
  ) => {

    setEventData((prev) => ({

      ...prev,

      vendors:

        (prev.vendors || [])
          .map((vendor) =>

            vendor.id === id
              ? {
                  ...vendor,
                  ...updatedData
                }
              : vendor
          )
    }));

    addActivity(
      "Vendor Updated"
    );
  };

  const deleteVendor = (
    id
  ) => {

    setEventData((prev) => ({

      ...prev,

      vendors:

        (prev.vendors || [])
          .filter(
            (vendor) =>

              vendor.id !== id
          )
    }));

    addActivity(
      "Vendor Deleted"
    );
  };

  /* =========================
     GUEST FUNCTIONS
  ========================= */

  const addGuest = (
    guest
  ) => {

    const newGuest = {

      id:
        crypto.randomUUID(),

      ...guest
    };

    setEventData((prev) => ({

      ...prev,

      guestsList: [

        ...(prev.guestsList || []),

        newGuest
      ]
    }));

    addActivity(
      "Guest Added"
    );
  };

  const updateGuest = (
    id,
    updatedData
  ) => {

    setEventData((prev) => ({

      ...prev,

      guestsList:

        (prev.guestsList || [])
          .map((guest) =>

            guest.id === id
              ? {
                  ...guest,
                  ...updatedData
                }
              : guest
          )
    }));

    addActivity(
      "Guest Updated"
    );
  };

  const deleteGuest = (
    id
  ) => {

    setEventData((prev) => ({

      ...prev,

      guestsList:

        (prev.guestsList || [])
          .filter(
            (guest) =>

              guest.id !== id
          )
    }));

    addActivity(
      "Guest Deleted"
    );
  };

  /* =========================
     WORKFLOW STATUS
  ========================= */

  const updateWorkflowStatus = (
    agent,
    status
  ) => {

    setEventData((prev) => ({

      ...prev,

      workflowData: {

        ...prev.workflowData,

        [agent]: status
      }
    }));

    addActivity(
      `${agent} workflow updated`
    );
  };

  /* =========================
     CONTEXT PROVIDER
  ========================= */

  return (

    <EventContext.Provider
      value={{

        /* Main Data */

        eventData,
        setEventData,

        /* Activities */

        activities,
        addActivity,

        /* Loading */

        loading,
        setLoading,

        /* Error */

        error,
        setError,

        /* Workflow */

        updateWorkflowStatus,

        /* Timeline */

        addTimelineEvent,
        deleteTimelineEvent,

        /* Vendors */

        addVendor,
        updateVendor,
        deleteVendor,

        /* Guests */

        addGuest,
        updateGuest,
        deleteGuest,

        /* Reset */

        resetEventData
      }}
    >

      {children}

    </EventContext.Provider>
  );
};