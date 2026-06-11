from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# =========================
# DATABASE CONFIGURATION
# =========================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./eventplanner.db"
)

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql://",
        1
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