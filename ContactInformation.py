from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class ContactInfo(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None


class ContactsSection(BaseModel):
    section_name: str = "Contact Information"
    contacts: Optional[List[ContactInfo]] = None