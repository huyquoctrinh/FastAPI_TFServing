from typing import List, Union
from pydantic import BaseModel

class DetectObject(BaseModel):
    image: str
    TrackingID: str
    timestamp: int
    masked: bool

class DetectItem(BaseModel):
    client_id: str
    data: List[DetectObject]

class RequestObject(BaseModel):
    image: str 

class RequestList(BaseModel):
    data: List[RequestObject]
    