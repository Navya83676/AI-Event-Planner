
import { useContext } from "react";
import "../styles/timeline.css";
import { EventContext } from "../context/EventContext";

function Timeline() {

  const { eventData } =
    useContext(EventContext);


  const eventName =
    eventData?.eventName ||
    eventData?.event_name ||
    "AI Event";

  const eventType =
    eventData?.eventType ||
    eventData?.event_type ||
    "Conference";

  const eventGuests =
    Number(
      eventData?.guests
    ) || 0;

  const vendorsCount =
    Array.isArray(
      eventData?.vendors
    )
      ? eventData.vendors.length
      : 0;

  /* =========================
   TIMELINE DATA
========================= */

const timelineObject =
  eventData?.timeline || {};


const convertTimelineItem = (
  item,
  period
) => {

  // String format
  if (
    typeof item === "string"
  ) {

    return {
      title: item,
      time: period
    };
  }

  // Object format
  return {
    title:
      item?.title ||
      item?.activity ||
      item?.name ||
      item?.task ||
      "Untitled Event",

    time:
      item?.time ||
      period,

    description:
      item?.description ||
      item?.details ||
      ""
  };
};

let timelineData = [];

if (
  Array.isArray(
    timelineObject.event
  )
) {

  const firstItem =
    timelineObject.event[0];

  // MULTI-DAY FORMAT
  if (
    firstItem &&
    Array.isArray(firstItem.activities)
  ) {

    timelineData =
      timelineObject.event.flatMap(
        (dayData) => [

          {
            title: dayData.day,
            time: "",
            description: "",
            isDayHeader: true
          },

          ...(dayData.activities || []).map(
            (activity) => ({

              title:
                activity.activity,

              time:
                activity.time,

              description: "",

              isDayHeader: false
            })
          )
        ]
      );

  }

  // SINGLE-DAY FORMAT
  else {

    timelineData =
      timelineObject.event.map(
        (activity) => ({

          title:
            activity.activity ||
            activity.title ||
            "Untitled Activity",

          time:
            activity.time ||
            "",

          description:
            activity.description ||
            "",

          isDayHeader: false
        })
      );

  }

}

else if (
  timelineObject.day_1 ||
  timelineObject.day_2 ||
  timelineObject.day_3
) {

  timelineData = [];

  Object.entries(
    timelineObject
  ).forEach(

    ([day, activities]) => {

      if (
        day.startsWith("day_") &&
        Array.isArray(activities)
      ) {

        activities.forEach(
          (item) => {

            timelineData.push({

              title:
                item.activity,

              time:
                `${day.replace("_"," ").toUpperCase()} • ${item.time}`,

              description: ""

            });

          }
        );

      }

    }

  );

}

else {

  timelineData = [

    ...(timelineObject.morning || []).map(
      (item) =>
        convertTimelineItem(
          item,
          "Morning"
        )
    ),

    ...(timelineObject.afternoon || []).map(
      (item) =>
        convertTimelineItem(
          item,
          "Afternoon"
        )
    ),

    ...(timelineObject.evening || []).map(
      (item) =>
        convertTimelineItem(
          item,
          "Evening"
        )
    )

  ];

}

  /* =========================
     ENHANCED TIMELINE
  ========================= */

  const now = new Date();

  const eventDate =
    new Date(eventData?.eventDate);

  console.log("Event Date Raw:", eventData?.eventDate);
  console.log("Parsed Date:", eventDate);

  const isFutureEvent =
    eventDate > now;

  let currentDayOffset = 0;
  const enhancedTimeline =
    timelineData.map((item, index) => {

      let status = "Pending";

      if (isFutureEvent) {

        return {
          ...item,
          status: "Pending",
          progress: 0
        };

      }

      if (item.isDayHeader) {

        const dayMatch =
          item.title.match(/\d+/);

        currentDayOffset =
          dayMatch
            ? Number(dayMatch[0]) - 1
            : 0;

        const dayDate = new Date(eventDate);

        dayDate.setDate(
          dayDate.getDate() + currentDayOffset
        );

        const startOfDay = new Date(dayDate);
        startOfDay.setHours(0, 0, 0, 0);

        const endOfDay = new Date(dayDate);
        endOfDay.setHours(23, 59, 59, 999);

        let dayStatus = "Pending";

        if (now > endOfDay) {
          dayStatus = "Completed";
        }
        else if (
          now >= startOfDay &&
          now <= endOfDay
        ) {
          dayStatus = "In Progress";
        }

        return {
          ...item,
          status: dayStatus,
          progress:
            dayStatus === "Completed"
              ? 100
              : dayStatus === "In Progress"
              ? 50
              : 0
        };
      }
    try {

      const eventTime = new Date(eventDate);

      eventTime.setDate(
        eventTime.getDate() +
        currentDayOffset
      );

      const [time, meridian] =
        item.time.split(" ");

      let [hours, minutes] =
        time.split(":").map(Number);

      if (
        meridian === "PM" &&
        hours !== 12
      ) {
        hours += 12;
      }

      if (
        meridian === "AM" &&
        hours === 12
      ) {
        hours = 0;
      }

      eventTime.setHours(
        hours,
        minutes,
        0,
        0
      );

      const nextItem =
        timelineData[index + 1];

      let nextEventTime =
        new Date(eventTime);

      if (nextItem) {

        const [nextTime, nextMeridian] =
          nextItem.time.split(" ");

        let [nextHours, nextMinutes] =
          nextTime.split(":").map(Number);

        if (
          nextMeridian === "PM" &&
          nextHours !== 12
        ) {
          nextHours += 12;
        }

        if (
          nextMeridian === "AM" &&
          nextHours === 12
        ) {
          nextHours = 0;
        }

        nextEventTime.setHours(
          nextHours,
          nextMinutes,
          0,
          0
        );

      } else {

        nextEventTime =
          new Date(eventTime);

        nextEventTime.setMinutes(
          nextEventTime.getMinutes() + 30
        );

      }

      if (eventTime > now) {

        status = "Pending";

      }
      else if (
        eventTime <= now &&
        nextEventTime > now
      ) {

        status = "In Progress";

      }
      else {

        status = "Completed";

      }

    } catch {

      status = "Pending";

    }

    return {

      ...item,

      status,

      progress:
        status === "Completed"
          ? 100
          : status === "In Progress"
          ? 50
          : 0

    };

});
  /* =========================
     OVERALL PROGRESS
  ========================= */

  const actualTasks =
    enhancedTimeline.filter(
      item => !item.isDayHeader
    );

 const completedTasks =
  actualTasks.filter(
    item => item.status === "Completed"
  ).length;

  const overallProgress =

  isFutureEvent

    ? 0

    : actualTasks.length > 0

      ? Math.round(
          (completedTasks / actualTasks.length) * 100
        )

      : 0;

  return (

    <div className="timeline-page">

      <div className="timeline-hero">

        <div className="hero-left">

          <div className="timeline-badge">
            AI EXECUTION TIMELINE
          </div>

          <h1>
             Event Timeline
          </h1>

          <p>
            Smart AI-powered event execution workflow
          </p>

        </div>

        <div className="timeline-event-card">

          <span className="event-label">
            ACTIVE EVENT
          </span>

          <h2>
            {eventName}
          </h2>

          <p>
            {eventType}
          </p>

          <div className="event-stats">

            <div>
              <strong>
                {eventGuests}
              </strong>
              <span>
                Guests
              </span>
            </div>

            <div>
              <strong>
                {vendorsCount}
              </strong>
              <span>
                Vendors
              </span>
            </div>

            <div>
              <strong>
                {isFutureEvent
                  ? "Scheduled"
                  : `${overallProgress}%`}
              </strong>

              <span>
                Status
              </span>
            </div>

          </div>

        </div>

      </div>



      <div className="timeline-summary">

  <div className="summary-card">
    <h3>{actualTasks.length}</h3>
    <p>Total Tasks</p>
  </div>

 <div className="summary-card">
  <h3>
    {completedTasks}
  </h3>
  <p>Completed</p>
</div>

  <div className="summary-card">
    <h3>
      {
        enhancedTimeline.filter(
          item => item.status === "In Progress"
        ).length
      }
    </h3>
    <p>Running</p>
  </div>

  <div className="summary-card">
    <h3>{overallProgress}%</h3>
    <p>Progress</p>
  </div>

</div>



      {isFutureEvent && (

        <div className="future-event-banner">

          Event Scheduled For:
          {eventData?.eventDate}

        </div>

      )}

      <div className="timeline-flow">

        {enhancedTimeline.length > 0 ? (

          enhancedTimeline.map(
            (
              item,
              index
            ) => (

              <div
                key={`${item.title}-${index}`}
                className="timeline-item"
              >

               {!item.isDayHeader && (

                <div
                  className={`timeline-dot ${
                    item.status === "Completed"
                      ? "dot-completed"
                      : item.status === "In Progress"
                      ? "dot-progress"
                      : "dot-pending"
                  }`}
                />

              )}

                <div className="timeline-content">

                  <div className="timeline-top">

                    <div>

                      <div className="timeline-task">

                        {!item.isDayHeader && (

                          <div className="timeline-time-chip">
                            {item.time}
                          </div>

                        )}

                        {item.isDayHeader ? (

                          <div className="day-header">
                            {item.title}
                          </div>

                        ) : (

                          <h3>
                            {item.title}

                          </h3>

                        )}

                      </div>

                     

                    </div>

                    {!isFutureEvent && (

                    <span
                          className={`status-badge ${
                            item.status === "Completed"
                              ? "completed"
                              : item.status === "In Progress"
                              ? "progress"
                              : "pending"
                          }`}
                        >
                          {item.status}
                    </span>

                      )}

                  </div>
                {item.description && (
                  <div className="timeline-details">
                    {item.description}
                  </div>

                )}

                  
                </div>

              </div>

            )
          )

        ) : (

          <div className="timeline-empty">

            <h3>
              No Timeline Generated
            </h3>

            <p>
              Create an event brief and run
              the AI workflow to generate
              the execution timeline.
            </p>

          </div>

        )}

      </div>

    </div>

  );

}

export default Timeline;