from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import date

class PolicySummary(BaseModel):
    """
    High-level summary of a policy document.
    """
    policy_name: str = Field(..., description="The official name or title of the policy.")
    policy_type: Optional[str] = Field(None, description="The type of policy (e.g., 'Health Insurance', 'Car Warranty', 'Privacy Policy', 'Government Scheme').")
    policy_id: Optional[str] = Field(None, description="Unique identifier for the policy, if available.")
    effective_date: Optional[date] = Field(None, description="The date the policy becomes effective.")
    expiration_date: Optional[date] = Field(None, description="The date the policy expires, if applicable.")
    issuing_entity: Optional[str] = Field(None, description="The organization or entity issuing the policy (e.g., 'LIC', 'Samsung', 'Ministry of Finance').")
    summary: str = Field(..., description="A concise, high-level summary of the policy's purpose and scope.")
    last_updated: Optional[date] = Field(None, description="The date the policy was last revised or updated.")
    source_url: Optional[HttpUrl] = Field(None, description="URL where the original policy document can be found, if applicable.")
    key_definitions: Optional[Dict[str, str]] = Field(None, description="A dictionary of important terms and their definitions found in the policy.")
    table_of_contents: Optional[List[str]] = Field(None, description="A list of main sections or headings in the policy.")