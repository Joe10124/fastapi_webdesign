from pydantic import BaseModel

# Pydantic models
class TodoBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False
class TodoCreate(TodoBase):
    pass
class TodoResponse(TodoBase):
    id: int
    class Config:
        from_attributes = True