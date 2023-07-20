from pydantic import BaseModel

class Review(BaseModel):
    id: int
    message: str
    user: str