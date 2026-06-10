import {
  useContext
} from "react";

import {
  EventContext
} from "../context/EventContext";

import "./WorkflowGraph.css";

function WorkflowGraph() {

  const {
    eventData
  } = useContext(EventContext);

  const executionFlow =
    eventData?.execution_flow || [];

  return (

    <div className="workflow-container">

      <h2>
        AI Agent Workflow
      </h2>

      <div className="workflow-grid">

        {

          executionFlow.map(
            (agent, index) => (

              <div
                className="workflow-card"
                key={index}
              >

                <h3>
                  {agent}
                </h3>

                <p>
                  Active
                </p>

              </div>

            )
          )
        }

      </div>

    </div>
  );
}

export default WorkflowGraph;