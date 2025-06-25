from pydantic import BaseModel, Field
from typing import Optional, List

class Obligation(BaseModel):
    """
    A single obligation or responsibility.
    """
    description: str = Field(..., description="Description of the policyholder's obligation.")
    consequence_of_non_compliance: Optional[str] = Field(None, description="What happens if this obligation is not met.")

class ObligationsSection(BaseModel):
    """
    Policyholder obligations and responsibilities.
    """
    section_name: str = Field("Obligations and Responsibilities", description="Name of the section.")
    obligations: List[Obligation] = Field(..., description="List of policyholder obligations.")