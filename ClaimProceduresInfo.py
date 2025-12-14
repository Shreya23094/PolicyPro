from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class Step(BaseModel):
    """
    A single step in a procedure.
    """
    step_number: int = Field(..., description="The sequence number of the step.")
    description: str = Field(..., description="Description of the action to take.")
    required_documents: Optional[List[str]] = Field(None, description="Documents needed for this step.")
    contact_info: Optional[str] = Field(None, description="Contact information relevant to this step.")

class ClaimProcedure(BaseModel):
    """
    Detailed procedure for making a claim or reporting an incident.
    """
    procedure_name: str = Field(..., description="Name of the procedure (e.g., 'Filing a Medical Claim', 'Reporting a Data Breach').")
    overview: Optional[str] = Field(None, description="A brief overview of the entire procedure.")
    steps: List[Step] = Field(..., description="Ordered list of steps to follow.")
    timeline: Optional[str] = Field(None, description="Expected timeline for the procedure (e.g., 'Within 30 days', 'Immediately').")
    support_contacts: Optional[Dict[str, str]] = Field(None, description="Key contact information for assistance.")
    notes: Optional[str] = Field(None, description="Any important notes or warnings about the procedure.")