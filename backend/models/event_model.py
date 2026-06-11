from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime
)

from datetime import datetime

from pydantic import BaseModel

from database import Base


# =========================
# DATABASE MODEL
# =========================

class Event(Base):

    __tablename__ = "events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_name = Column(
        String,
        nullable=False
    )

    event_name = Column(
        String,
        nullable=False
    )

    event_type = Column(
        String,
        nullable=False
    )

    guests = Column(
        Integer,
        nullable=False
    )

    budget = Column(
        Integer,
        nullable=False
    )

    event_date = Column(
        String,
        nullable=False
    )

    venue = Column(
        String,
        nullable=False
    )

    event_duration = Column(
        String,
        nullable=True
    )

    theme = Column(
        String,
        nullable=True
    )

    requirements = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="GENERATED"
    )

    workflow_data = Column(
        JSON
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================
# REQUEST MODEL
# =========================

class EventRequest(BaseModel):

    customer_name: str

    event_name: str

    event_type: str

    guests: int

    budget: int

    event_date: str

    event_duration: str

    location: str = ""

    venue: str

    theme: str = ""

    requirements: str


# =========================
# RESPONSE MODEL
# =========================

class EventResponse(BaseModel):

    success: bool

    message: str

    data: dict