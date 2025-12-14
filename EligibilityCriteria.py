from pydantic import BaseModel, Field
from typing import Optional, List

class EligibilityCriterion(BaseModel):
    criterion: Optional[str] = None
    details: Optional[str] = None
    is_required: Optional[bool] = None

class EligibilitySection(BaseModel):
    section_name: str = Field("Eligibility")
    criteria: Optional[List[EligibilityCriterion]] = None
    notes: Optional[str] = None