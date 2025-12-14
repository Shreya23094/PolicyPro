from pydantic import BaseModel, Field
from typing import Optional, List

class Clause(BaseModel):
    """
    A single clause or term.
    """
    heading: Optional[str] = Field(None, description="Heading of the clause if it exists.")
    content: str = Field(..., description="Full text of the clause.")
    keywords: Optional[List[str]] = Field(None, description="Key terms or concepts within the clause.")

class TermsAndConditionsSection(BaseModel):
    clauses: Optional[List[str]] = None
