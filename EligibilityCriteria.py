from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class EligibilityCriterion(BaseModel):
    """
    A single criterion for eligibility.
    """
    criterion: str = Field(..., description="The specific condition or requirement for eligibility (e.g., 'Age', 'Residency', 'Vehicle Type').")
    details: str = Field(..., description="Detailed explanation of the criterion.")
    is_required: bool = Field(..., description="True if this criterion is mandatory, False if optional.")

class EligibilitySection(BaseModel):
    """
    Overall eligibility requirements for the policy.
    """
    section_name: str = Field("Eligibility", description="Name of the eligibility section.")
    criteria: List[EligibilityCriterion] = Field(..., description="List of eligibility criteria.")
    notes: Optional[str] = Field(None, description="Any general notes or disclaimers about eligibility.")