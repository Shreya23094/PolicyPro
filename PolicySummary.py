from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import date


class Clause(BaseModel):
    heading: Optional[str] = Field(None, description="Heading of the clause if it exists.")
    content: str = Field(..., description="Full text of the clause.")
    keywords: Optional[List[str]] = Field(None, description="Key terms or concepts.")


class Obligation(BaseModel):
    description: str = Field(..., description="Policyholder obligation.")
    consequence_of_non_compliance: Optional[str] = Field(
        None, description="Consequence if obligation is not met."
    )


class ContactInfo(BaseModel):
    department: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    address: Optional[str] = Field(None)
    website: Optional[HttpUrl] = Field(None)
    hours_of_operation: Optional[str] = Field(None)


class PolicySummary(BaseModel):
    """
    High-level summary PLUS core policy sections.
    """

    # ─── BASIC POLICY INFO ─────────────────────────────
    policy_name: str = Field(..., description="Official name of the policy.")
    policy_type: Optional[str] = Field(None, description="Type of policy.")
    policy_id: Optional[str] = Field(None, description="Unique policy identifier.")
    effective_date: Optional[date] = Field(None, description="Policy start date.")
    expiration_date: Optional[date] = Field(None, description="Policy end date.")
    issuing_entity: Optional[str] = Field(None, description="Issuing organization.")
    summary: str = Field(..., description="High-level policy overview.")

    # ─── TERMS & CONDITIONS ────────────────────────────
    terms_section_name: str = Field(
        "Terms and Conditions", description="Name of terms section."
    )
    clauses: List[Clause] = Field(
        ..., description="List of terms and conditions clauses."
    )

    # ─── OBLIGATIONS ───────────────────────────────────
    obligations_section_name: str = Field(
        "Obligations and Responsibilities",
        description="Name of obligations section."
    )
    obligations: List[Obligation] = Field(
        ..., description="Policyholder obligations."
    )

    # ─── CONTACT INFORMATION ───────────────────────────
    contact_section_name: str = Field(
        "Contact Information", description="Name of contact section."
    )
    contacts: List[ContactInfo] = Field(
        ..., description="Support and contact details."
    )
