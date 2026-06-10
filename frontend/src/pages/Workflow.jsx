import {
  useContext,
  useEffect,
  useState,
  useRef,
  useMemo
} from "react";

import "../styles/workflow.css";

import {
  FaBrain,
  FaRobot,
  FaCheckCircle,
  FaSpinner
} from "react-icons/fa";

import {
  EventContext
} from "../context/EventContext";




const formatAgentName = (name) => {

  const mapping = {

    event_classifier_agent: "Event Classifier Agent",

    vendor_agent: "Vendor Agent",

    venue_agent: "Venue Agent",

    food_agent: "Food Agent",

    budget_agent: "Budget Agent",

    decoration_agent: "Decoration Agent",

    security_agent: "Security Agent",

    entertainment_agent: "Entertainment Agent",

    timeline_agent: "Timeline Agent"
  };

  return mapping[name] || name;
};


const agentDescriptions = {

  event_classifier_agent:
    "Analyzing event requirements",

  vendor_agent:
    "Selecting best vendor partners",

  venue_agent:
    "Finding optimal venue",

  food_agent:
    "Planning catering services",

  budget_agent:
    "Optimizing budget allocation",

  decoration_agent:
    "Designing event aesthetics",

  security_agent:
    "Planning security coverage",

  entertainment_agent:
    "Managing entertainment schedule",

  timeline_agent:
    "Building execution timeline"
};

function Workflow() {

  console.count("Workflow Render");

  const {
    eventData
  } = useContext(EventContext);

  const agents =

    Array.isArray(
      eventData?.workflowData?.agents
    )

      ? eventData.workflowData.agents

      : [];
  const visibleAgents = useMemo(() => {

  return agents.filter(
    (agent) =>
      agent.name !== "supervisor_agent" &&
      agent.name !== "Supervisor Agent"
  );

}, [agents]);
      const agentExecutionTimes = {

  event_classifier_agent: "9.4s",

  vendor_agent: "2.2s",

  venue_agent: "1.4s",

  food_agent: "2.6s",

  budget_agent: "1.8s",

  decoration_agent: "2.1s",

  security_agent: "2.3s",

  entertainment_agent: "2.5s",

  timeline_agent: "2.7s"
};

  const [activeStep, setActiveStep] =
    useState(0);

  const [supervisorExecuting, setSupervisorExecuting] = useState(true);

  const [logs, setLogs] =
    useState([]);

  const terminalRef =
    useRef(null);

  /* AUTO SCROLL */

  useEffect(() => {

    if (terminalRef.current) {

      terminalRef.current.scrollTo({

        top:
          terminalRef.current.scrollHeight,

        behavior: "smooth"
      });
    }

  }, [logs]);

  /* EXECUTION ENGINE */

  useEffect(() => {

    setActiveStep(0);

    setLogs([]);

    setSupervisorExecuting(true);


    const executionLogs = [

      `Initializing ${eventData?.eventName} orchestration...`,

      `Loading ${eventData?.eventType} intelligence...`,

      `Analyzing ${eventData?.guests} guests...`,

      `Optimizing ₹${Number(
        eventData?.budget || 0
      ).toLocaleString()} budget...`,

      `Preparing venue at ${eventData?.location}...`,
    ];

    visibleAgents.forEach((agent) => {

  let agentMessage =
    `[${formatAgentName(agent.name)}] ${agent.desc}`;

  if (
    agent.name === "venue_agent"
  ) {

    agentMessage =
      `[Venue Agent] Selected venue for ${eventData?.guests} guests`;

  }

  else if (
    agent.name ==="food_agent"
  ) {

    agentMessage =
      `[Food Agent] Catering budget allocated`;

  }

  else if (
    agent.name ==="budget_agent"
  ) {

    agentMessage =
      `[Budget Agent] Budget optimization completed`;

  }

  else if (
    agent.name ==="decoration_agent"
  ) {

    agentMessage =
      `[Decoration Agent] Theme design generated`;

  }

  else if (
    agent.name ===
    "security_agent"
  ) {

    agentMessage =
      `[Security Agent] Security coverage planned`;

  }

  else if (
    agent.name ===
    "entertainment_agent"
  ) {

    agentMessage =
      `[Entertainment Agent] Entertainment schedule created`;

  }

  else if (
    agent.name ===
    "timeline_agent"
  ) {

    agentMessage =
      `[Timeline Agent] Timeline generated successfully`;

  }

  executionLogs.push(
    agentMessage
  );

});

    executionLogs.push(
      "Generating final AI coordination report..."
    );

    executionLogs.push(
      "Final AI execution completed successfully..."
    );

    let logIndex = 0;

    let stepIndex = 0;

    const logInterval =
      setInterval(() => {

        if (
          logIndex <
          executionLogs.length
        ) {

          setLogs((prev) => [

            ...prev,

            executionLogs[logIndex]
          ]);

          logIndex++;

        } else {

          clearInterval(logInterval);

        }

      }, 1800);

      let stepInterval;

const supervisorDelay = setTimeout(() => {

  setSupervisorExecuting(false);

  stepInterval = setInterval(() => {

   if (stepIndex < visibleAgents.length) {

  setActiveStep(stepIndex + 1);

  stepIndex++;

} else {

  setActiveStep(visibleAgents.length + 1);

  clearInterval(stepInterval);

}

  }, 1800);

}, 2500);
    return () => {

      clearInterval(logInterval);

      clearInterval(stepInterval);

      clearTimeout(supervisorDelay);

    };

  }, [eventData]);

  /* PROGRESS */

  const progress =

    visibleAgents.length > 0

      ? Math.min(

          Math.floor(

            (
              activeStep /
              visibleAgents.length
            ) * 100
          ),

          100
        )

      : 0;

  return (

    <div className="workflow-page">

      {/* HERO */}

      <div className="workflow-hero">

        <p className="workflow-label">

          AI Orchestration Engine

        </p>

        <h1 className="workflow-title">

          Live AI Workflow

        </h1>

        <p className="workflow-subtitle">

          Real-time orchestration generated for

          {" "}

          <strong>

            {
              eventData?.eventName ||
              "your event"
            }

          </strong>

        </p>

        <div className="workflow-badge">

          <FaBrain />

          <span>
            LIVE EXECUTION
          </span>

        </div>

      </div>

      {/* STATUS */}

      <div className="workflow-status">

        <div>

          <h3>
            AI System Status
          </h3>

          <p>

            {

              progress === 100

                ? "Execution completed successfully"

                : `Running ${activeStep} of ${visibleAgents.length} AI agents`
            }

          </p>

        </div>

        <div className="workflow-progress">

          <span>
            {progress}% Completed
          </span>

          <div className="progress-bar">

            <div
              className="progress-fill"
              style={{
                width: `${progress}%`
              }}
            ></div>

          </div>

        </div>

      </div>

      {/* LIVE EXECUTION STREAM */}

      <div className="workflow-terminal">

        <div className="terminal-top">

          <div className="terminal-dots">

            <span className="red"></span>

            <span className="yellow"></span>

            <span className="green"></span>

          </div>

          <h4>
            LIVE EXECUTION STREAM
          </h4>

        </div>

        <div
          className="terminal-body"
          ref={terminalRef}
        >

          {

            logs.map(
              (
                log,
                index
              ) => (

                <div
                  key={index}
                  className="terminal-log"
                >

                  <span className="log-dot"></span>

                  <p>
                    {log}
                  </p>

                </div>
              )
            )
          }

        </div>

      </div>

      {/* AGENT WORKFLOW */}

      <div className="workflow-graph">

        <div className="supervisor-wrapper">

          <div
            className={`supervisor-node ${
              supervisorExecuting
                ? "active-node"
                : "completed-node"
            }`}
          >

            <div className="node-icon supervisor-icon">

              <FaBrain />

            </div>

            <h2>
              Supervisor Agent
            </h2>

            <p>
              Managing entire AI orchestration workflow
            </p>

            <span>
               {supervisorExecuting
                  ? "EXECUTING"
                  : "COMPLETED"}
            </span>

          </div>

        </div>

        <div className="main-connector"></div>

        <div className="agents-grid">

          {

            visibleAgents.map(
              (
                agent,
                index
              ) => {

                const isCompleted =
                  activeStep > index + 1;

                const isActive =
                  activeStep === index + 1;

                return (

                  <div
                    key={index}
                    className={`agent-node

                      ${
                        isCompleted
                          ? "completed-node"
                          : isActive
                          ? "active-node"
                          : "pending-node"
                      }
                    `}
                  >

                    <div className={`node-icon color-${index % 8}`}>

                      {

                        isCompleted

                          ? <FaCheckCircle />

                          : isActive

                          ? (
                            <FaSpinner className="spin" />
                          )

                          : <FaRobot />
                      }

                    </div>

                    <div>

                      <h3>
                        {formatAgentName(agent.name)}
                      </h3>

                      <div>

                    <p>
                      {
                        agentDescriptions[
                          agent.name
                        ] || agent.desc
                      }
                    </p>

                    <small>

                      Execution:

                      {" "}

                      {
                        agentExecutionTimes[
                          agent.name
                        ] || "0.5s"
                      }

                    </small>

                  </div>

                    </div>

                    <span>

                      {

                        isCompleted

                          ? "Completed"

                          : isActive

                          ? "Executing"

                          : "Pending"
                      }

                    </span>

                  </div>
                );
              }
            )
          }

        </div>

      </div>

    </div>
  );
}

export default Workflow;