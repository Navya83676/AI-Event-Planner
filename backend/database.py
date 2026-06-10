from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)

# =========================
# DATABASE CONFIGURATION
# =========================

DATABASE_URL = (
    "postgresql://postgres:eventplanner123@localhost:5432/ai_event_planner"
)

# =========================
# DATABASE ENGINE
# =========================

engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True
)

# =========================
# SESSION FACTORY
# =========================

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine
)

# =========================
# BASE MODEL
# =========================

Base = declarative_base()