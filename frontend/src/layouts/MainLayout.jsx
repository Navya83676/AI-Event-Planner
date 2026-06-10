import { Outlet } from "react-router-dom";

import Sidebar from "../components/Sidebar";

import "../styles/layout.css";

const MainLayout = () => {

  return (

    <div className="app-layout">

      {/* SIDEBAR */}

      <Sidebar />

      {/* MAIN CONTENT */}

      <main className="page-container">

        <Outlet />

      </main>

    </div>
  );
};

export default MainLayout;