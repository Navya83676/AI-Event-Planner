import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/variables.css"
import "./index.css";

import { BrowserRouter } from "react-router-dom";

import { EventProvider } from "./context/EventContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>

    <BrowserRouter>

      <EventProvider>

        <App />

      </EventProvider>

    </BrowserRouter>

  </React.StrictMode>
);