from pydantic import BaseModel


class Claim(BaseModel):
    slug: str
    will_come: bool
    solo: bool
    have_car: bool
    transfer_to: bool
    transfer_from: bool

    class Config:
        orm_mode = True