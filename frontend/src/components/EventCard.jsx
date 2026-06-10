import ReactMarkdown from "react-markdown";

function EventCard({ title, data }) {

  return (
    <div className="agent-card">

      <h2>{title}</h2>

      <ReactMarkdown>
        {data}
      </ReactMarkdown>

    </div>
  );
}

export default EventCard;