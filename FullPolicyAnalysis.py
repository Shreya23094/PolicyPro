from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from PolicySummary import PolicySummary
from ClaimProceduresInfo import ClaimProcedure
from CoverageDetails import CoverageSection
from EligibilityCriteria import EligibilitySection
from ObligationsAndResponsibilities import ObligationsSection
from ContactInformation import ContactsSection
from TermsAndConditions import TermsAndConditionsSection

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

    obligations: Optional[ObligationsSection] = Field(
        default=None,
        description="Responsibilities and required actions of the policyholder."
    )

    terms_and_conditions: Optional[TermsAndConditionsSection] = Field(
        default=None,
        description="General legal clauses, exceptions, or renewal terms."
    )

    contact_information: Optional[ContactsSection] = Field(
        default=None,
        description="Important contact details like email, phone, or web support links."
    )

    other_sections: Optional[Dict[str, str]] = Field(
        default=None,
        description="Any unmatched or miscellaneous sections stored as key-value pairs of section title and text."
    )
