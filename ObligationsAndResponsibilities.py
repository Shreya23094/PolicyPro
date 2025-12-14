from pydantic import BaseModel, Field
from typing import Optional, List

class Obligation(BaseModel):
    description: Optional[str] = None
    consequence_of_non_compliance: Optional[str] = None

class ObligationsSection(BaseModel):
    section_name: str = Field("Obligations and Responsibilities")
    obligations: Optional[List[Obligation]] = None
