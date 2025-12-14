from PolicySummary import PolicySummary
from CoverageDetails import CoverageSection
from EligibilityCriteria import EligibilitySection
from ClaimProceduresInfo import ClaimProcedure
from ObligationsAndResponsibilities import ObligationsSection
from TermsAndConditions import TermsAndConditionsSection
from ContactInformation import ContactsSection

from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class FullPolicyAnalysis(BaseModel):
    summary: PolicySummary

    coverages: Optional[List[CoverageSection]] = None
    eligibility: Optional[EligibilitySection] = None
    claim_procedures: Optional[List[ClaimProcedure]] = None
    obligations: Optional[ObligationsSection] = None
    terms_and_conditions: Optional[TermsAndConditionsSection] = None
    contact_information: Optional[ContactsSection] = None
    other_sections: Optional[Dict[str, str]] = None
