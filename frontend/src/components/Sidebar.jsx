import { NavLink } from "react-router-dom";

import {
  FaHome,
  FaFileAlt,
  FaRobot,
  FaClipboardList,
  FaStore,
  FaUsers,
  FaClock,
  FaCog
} from "react-icons/fa";

import "../styles/sidebar.css";

function Sidebar() {

  const menuItems = [

    {
      path: "/",
      label: "Dashboard",
      icon: <FaHome />
    },

    {
      path: "/brief",
      label: "Event Brief",
      icon: <FaFileAlt />
    },

    {
      path: "/workflow",
      label: "AI Workflow",
      icon: <FaRobot />
    },

    {
      path: "/plan",
      label: "Event Plan",
      icon: <FaClipboardList />
    },

    {
      path: "/vendors",
      label: "Vendors",
      icon: <FaStore />
    },

    {
      path: "/guests",
      label: "Guests",
      icon: <FaUsers />
    },

    {
      path: "/timeline",
      label: "Timeline",
      icon: <FaClock />
    },

    {
      path: "/settings",
      label: "Settings",
      icon: <FaCog />
    }

  ];

  return (

    <div className="sidebar">

      {/* TOP */}

      <div className="sidebar-top">

        <div className="brand-section">

          <div className="brand-text">

            <h1>AI Event Planner</h1>

            

          </div>

        </div>

      </div>

      {/* MENU */}

      <div className="sidebar-menu">

        {
          menuItems.map((item) => (

            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                isActive
                  ? "sidebar-link active"
                  : "sidebar-link"
              }
            >

              <div className="sidebar-icon">

                {item.icon}

              </div>

              <span>
                {item.label}
              </span>

            </NavLink>

          ))
        }

      </div>

    </div>
  );
}

export default Sidebar;