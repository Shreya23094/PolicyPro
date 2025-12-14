from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Step(BaseModel):
    step_number: Optional[int] = None
    description: Optional[str] = None


class ClaimProcedure(BaseModel):
    procedure_name: str
    overview: Optional[str] = None
    steps: Optional[List[Step]] = None
    timeline: Optional[str] = None