from datetime import datetime
from ninja import Schema

class TaskIn(Schema):
    owner: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
class TaskOut(Schema):
    id:int
    owner:str
    title:str
    content:str
    created_at:datetime
    updated_at:datetime
   