from pydantic import BaseModel, Field
from typing import Optional, List
from typing import Union


class CoverageDetail(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    limits: Optional[str] = None
    deductible: Optional[str] = None
    conditions: Optional[List[str]] = None
    exclusions: Optional[List[str]] = None

class CoverageSection(BaseModel):
    section_name: str = Field(..., description="Coverage section name.")
    coverages: Optional[List[Union[CoverageDetail, str]]] = Field(
        None,
        description="Coverage details as structured objects or plain text."
    )
