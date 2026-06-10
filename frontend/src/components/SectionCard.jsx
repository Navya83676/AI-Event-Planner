import "../styles/components.css";

function SectionCard({

  title,

  subtitle,

  children

}) {

  return (

    <div className="section-card">

      {

        (title || subtitle) && (

          <div className="section-card-header">

            {

              title && (

                <h3>
                  {title}
                </h3>
              )
            }

            {

              subtitle && (

                <span>
                  {subtitle}
                </span>
              )
            }

          </div>
        )
      }

      <div className="section-card-body">

        {children}

      </div>

    </div>
  );
}

export default SectionCard;