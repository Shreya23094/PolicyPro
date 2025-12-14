from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict

class ContactInfo(BaseModel):
    """
    Contact details for support or queries.
    """
    department: Optional[str] = Field(None, description="Department or function (e.g., 'Customer Service', 'Claims', 'Legal').")
    phone: Optional[str] = Field(None, description="Contact phone number.")
    email: Optional[str] = Field(None, description="Contact email address.")
    address: Optional[str] = Field(None, description="Physical address.")
    website: Optional[HttpUrl] = Field(None, description="Official website for support.")
    hours_of_operation: Optional[str] = Field(None, description="Hours during which contact is available.")

class ContactsSection(BaseModel):
    """
    Section for various contact points.
    """
    section_name: str = Field("Contact Information", description="Name of the section.")
    contacts: List[ContactInfo] = Field(..., description="List of various contact points.")