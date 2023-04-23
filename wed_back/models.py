from sqlalchemy import Boolean, Column, String

from database import Base


class Claim(Base):
    __tablename__ = "claims"

    slug = Column(String, primary_key=True, index=True, unique=True)
    will_come = Column(Boolean)
    solo = Column(Boolean)
    have_car = Column(Boolean)
    transfer_to = Column(Boolean)
    transfer_from = Column(Boolean)
