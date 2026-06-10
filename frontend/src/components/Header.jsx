import {
  FaBell,
  FaSearch,
  FaRobot
} from "react-icons/fa";

function Header() {

  return (

    <div className="top-header">

      {/* LEFT */}

      <div className="header-left">

        <h2>
          AI Event Intelligence Platform
        </h2>

        <p>
          Autonomous event orchestration system
        </p>

      </div>

      {/* CENTER */}

      <div className="header-search">

        <FaSearch />

        <input
          type="text"
          placeholder="Search events, vendors, analytics..."
        />

      </div>

      {/* RIGHT */}

      <div className="header-right">

        <div className="ai-status">

          <FaRobot />

          <span>
            AI Active
          </span>

        </div>

        <div className="notification-btn">

          <FaBell />

          <div className="notification-dot">

          </div>

        </div>

        <div className="profile-card">

          <img
            src="https://i.pravatar.cc/100"
            alt="profile"
          />

          <div>

            <h4>
              Event Admin
            </h4>

            <p>
              AI Coordinator
            </p>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Header;