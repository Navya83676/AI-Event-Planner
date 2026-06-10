import "../styles/components.css";

function StatCard({

  icon,

  title,

  value,

  subtitle,

  color = "purple"

}) {

  return (

    <div
      className="global-stat-card"
      style={{
        padding: "20px",
        minHeight: "190px"
      }}
    >

      <div
        className={`global-stat-icon ${color}`}
        style={{
          width: "58px",
          height: "58px",
          marginBottom: "18px"
        }}
      >

        {icon}

      </div>

      <h4
        style={{
          fontSize: "16px",
          marginBottom: "10px"
        }}
      >
        {title}
      </h4>

      <h2
        style={{
          fontSize: "42px",
          marginBottom: "10px"
        }}
      >
        {value}
      </h2>

      {

        subtitle && (

          <p
            style={{
              fontSize: "14px"
            }}
          >
            {subtitle}
          </p>
        )
      }

    </div>
  );
}

export default StatCard;