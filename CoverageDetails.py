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
    section_name: str
    coverages: Optional[List[Union[CoverageDetail, str]]] = None

