# AI Event Planner

AI-powered Multi-Agent Event Planning System that automatically generates complete event plans using specialized AI agents.

## Live Demo

Frontend:
https://ai-event-planner-1.onrender.com

Backend API:
https://ai-event-planner-sjgz.onrender.com/docs

---

## Features

- Multi-Agent AI Architecture
- Dynamic Event Classification
- Venue Recommendation
- Vendor Planning
- Food Planning
- Budget Optimization
- Decoration Planning
- Security Planning
- Entertainment Planning
- Timeline Generation
- PDF Report Generation
- Event History Storage
- Real-Time Workflow Visualization

---

## AI Agents

- Supervisor Agent
- Event Classifier Agent
- Venue Agent
- Vendor Agent
- Food Agent
- Budget Agent
- Decoration Agent
- Security Agent
- Entertainment Agent
- Timeline Agent

---

## Tech Stack

### Frontend

- React
- Vite
- React Router
- Axios
- Recharts
- React Flow
- Framer Motion

### Backend

- FastAPI
- Python
- LangChain
- LangGraph
- Groq LLM
- SQLAlchemy

### Database

- PostgreSQL
- Neon Database

### Deployment

- Render

---

## Workflow

Supervisor Agent
→ Event Classifier
→ Vendor Agent
→ Venue Agent
→ Food Agent
→ Budget Agent
→ Decoration Agent
→ Security Agent (conditional)
→ Entertainment Agent (conditional)
→ Timeline Agent

---

## API Endpoints

POST /generate

GET /events

GET /events/{event_id}

DELETE /events/{event_id}

POST /events/{event_id}/report

GET /health

---

## Project Highlights

- Built a multi-agent AI orchestration workflow using LangGraph.
- Integrated Groq LLM for intelligent event planning.
- Implemented conditional agent routing.
- Designed full-stack architecture using FastAPI and React.
- Deployed frontend and backend on Render.
- Integrated Neon PostgreSQL for cloud data persistence.

---

## Author

Navya

GitHub:
https://github.com/Navya83676
