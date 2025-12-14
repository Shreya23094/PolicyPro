from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class EligibilityCriterion(BaseModel):
    criterion: Optional[str] = None
    details: Optional[str] = None
    is_required: Optional[bool] = None

class EligibilitySection(BaseModel):
    """
    Overall eligibility requirements for the policy.
    """
    section_name: str = Field("Eligibility", description="Name of the eligibility section.")
    criteria: List[EligibilityCriterion] = Field(..., description="List of eligibility criteria.")
    notes: Optional[str] = Field(None, description="Any general notes or disclaimers about eligibility.")