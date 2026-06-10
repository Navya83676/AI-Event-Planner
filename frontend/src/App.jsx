import {
  Routes,
  Route
} from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

/* PAGES */

import Dashboard from "./pages/Dashboard";
import EventBrief from "./pages/EventBrief";
import Workflow from "./pages/Workflow";
import EventPlan from "./pages/EventPlan";
import Vendors from "./pages/Vendors";
import Guests from "./pages/Guests";

import Timeline from "./pages/Timeline";
import Settings from "./pages/Settings";
import NewEvent from "./pages/NewEvent";


function App() {

  return (

    <Routes>

      {/* MAIN LAYOUT */}

      <Route
        path="/"
        element={<MainLayout />}
      >

        {/* DASHBOARD */}

        <Route
          index
          element={<Dashboard />}
        />

       
        {/* CREATE EVENT */}

        <Route
          path="brief"
          element={<EventBrief />}
        />

        <Route
          path="new-event"
          element={<NewEvent />}
        />

        {/* WORKFLOW */}

        <Route
          path="workflow"
          element={<Workflow />}
        />

        {/* EVENT PLAN */}

        <Route
          path="plan"
          element={<EventPlan />}
        />

        {/* VENDORS */}

        <Route
          path="vendors"
          element={<Vendors />}
        />

        {/* GUESTS */}

        <Route
          path="guests"
          element={<Guests />}
        />

        

        {/* TIMELINE */}

        <Route
          path="timeline"
          element={<Timeline />}
        />

        

        {/* SETTINGS */}

        <Route
          path="settings"
          element={<Settings />}
        />

      </Route>

    </Routes>

  );
}

export default App;