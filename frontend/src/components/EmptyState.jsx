import "../styles/components.css";

function EmptyState({

  title = "No Data Found",

  subtitle = "There is nothing to display right now."

}) {

  return (

    <div className="empty-state">

      <h2>
        {title}
      </h2>

      <p>
        {subtitle}
      </p>

    </div>
  );
}

export default EmptyState;