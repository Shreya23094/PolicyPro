from pydantic import BaseModel, Field
from typing import Optional, List

class Obligation(BaseModel):
    """
    A single obligation or responsibility.
    """
    description: str = Field(..., description="Description of the policyholder's obligation.")
    consequence_of_non_compliance: Optional[str] = Field(None, description="What happens if this obligation is not met.")

class ObligationsSection(BaseModel):
    section_name: str = "Obligations and Responsibilities"
    obligations: Optional[List[Obligation]] = None
