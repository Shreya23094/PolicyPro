from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class ContactInfo(BaseModel):
    department: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    website: Optional[HttpUrl] = None
    hours_of_operation: Optional[str] = None

class ContactsSection(BaseModel):
    section_name: str = Field("Contact Information")
    contacts: Optional[List[ContactInfo]] = None
