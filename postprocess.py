from models import (
    CoverageDetail,
    Step,
    Obligation,
    ContactInfo
)

def normalize_coverages(sections):
    if not sections:
        return sections

    for sec in sections:
        if sec.coverages is None:
            sec.coverages = [
                CoverageDetail(
                    name=sec.section_name,
                    description=sec.section_name
                )
            ]
        else:
            normalized = []
            for c in sec.coverages:
                if isinstance(c, str):
                    normalized.append(
                        CoverageDetail(name=c, description=c)
                    )
                else:
                    normalized.append(c)
            sec.coverages = normalized
    return sections


def normalize_claims(procedures):
    if not procedures:
        return procedures

    for i, proc in enumerate(procedures, start=1):
        if proc.steps is None:
            proc.steps = [
                Step(step_number=1, description=proc.procedure_name)
            ]
    return procedures


def normalize_obligations(section):
    if not section or not section.obligations:
        return section

    normalized = []
    for o in section.obligations:
        if isinstance(o, str):
            normalized.append(Obligation(description=o))
        else:
            normalized.append(o)
    section.obligations = normalized
    return section
