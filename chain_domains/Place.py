
from pydantic import BaseModel, Field


class Place(BaseModel):
    country: str = Field("Country to live")
    city: str = Field("City to live")
