import "./ActivityPanel.css";

function ActivityPanel() {
  const activities = [
    "Supervisor Agent analyzing requirements",
    "Budget Agent optimized allocation",
    "Venue Agent found suitable venues",
    "Catering Agent created menu plan",
    "Decoration Agent prepared themes",
    "Scheduling Agent generated timeline",
  ];

  return (
    <div className="activity-panel">
      <h3>Live Agent Activity</h3>

      {activities.map((item, index) => (
        <div className="activity-item" key={index}>
          <div className="activity-dot"></div>
          <p>{item}</p>
        </div>
      ))}
    </div>
  );
}

export default ActivityPanel;