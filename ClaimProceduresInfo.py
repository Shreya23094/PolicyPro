from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Step(BaseModel):
    step_number: Optional[int] = Field(None, description="Sequence number of the step.")
    description: Optional[str] = Field(None, description="Description of the action.")
    required_documents: Optional[List[str]] = None
    contact_info: Optional[str] = None

class ClaimProcedure(BaseModel):
    procedure_name: str = Field(..., description="Name of the procedure.")
    overview: Optional[str] = None
    steps: Optional[List[Step]] = None
    timeline: Optional[str] = None
    support_contacts: Optional[Dict[str, str]] = None
    notes: Optional[str] = None