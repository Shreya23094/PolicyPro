from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class CoverageDetail(BaseModel):
    """
    Details of a specific coverage or benefit within a policy.
    """
    name: str = Field(..., description="Name of the specific coverage or benefit (e.g., 'Hospitalization', 'Engine Repair', 'Data Breach').")
    description: str = Field(..., description="A clear description of what the coverage entails.")
    limits: Optional[str] = Field(None, description="Any financial limits or caps on this coverage (e.g., '$10,000', 'Up to vehicle value').")
    deductible: Optional[str] = Field(None, description="The amount the policyholder must pay before this coverage kicks in (e.g., '$500', '10% of claim').")
    conditions: Optional[List[str]] = Field(None, description="Specific conditions that must be met for this coverage to apply.")
    exclusions: Optional[List[str]] = Field(None, description="Specific scenarios or items explicitly not covered by this benefit.")

class CoverageSection(BaseModel):
    """
    A collection of coverage details.
    """
    section_name: str = Field(..., description="Name of the coverage section (e.g., 'Medical Benefits', 'Vehicle Damage', 'Data Usage').")
    coverages: List[CoverageDetail] = Field(..., description="List of individual coverage details within this section.")