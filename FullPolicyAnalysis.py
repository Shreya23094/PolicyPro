from pydantic import BaseModel, Field
from typing import Optional, List
from PolicySummary import PolicySummary
from ClaimProceduresInfo import ClaimProcedure
from CoverageDetails import CoverageSection
from EligibilityCriteria import EligibilitySection

class FullPolicyAnalysis(BaseModel):
    """
    Represents a comprehensive structured analysis of an insurance policy document.
    This model captures key sections like summary, coverages, eligibility criteria,
    claims, obligations, terms, contact details, and other uncategorized sections.
    """

    summary: PolicySummary = Field(..., description="High-level overview of the policy document.")

    coverages: Optional[List[CoverageSection]] = Field(
        default=None,
        description="List of all included coverage types and their descriptions."
    )

    eligibility: Optional[EligibilitySection] = Field(
        default=None,
        description="Details about who qualifies for the policy, including age, conditions, or region."
    )

    claim_procedures: Optional[List[ClaimProcedure]] = Field(
        default=None,
        description="List of steps or required documentation for filing a claim."
    )

