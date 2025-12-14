from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict
from datetime import date

class PolicySummary(BaseModel):
    policy_name: Optional[str] = None
    policy_type: Optional[str] = None
    policy_id: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    issuing_entity: Optional[str] = None
    summary: str
    last_updated: Optional[date] = None
    source_url: Optional[HttpUrl] = None
    key_definitions: Optional[Dict[str, str]] = None
    table_of_contents: Optional[List[str]] = None