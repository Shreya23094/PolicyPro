def normalize_llm_output(data: dict) -> dict:
    # ---------- COVERAGES ----------
    if isinstance(data.get("coverages"), dict):
        sections = []
        for key in data["coverages"].keys():
            sections.append({
                "section_name": key.replace("_", " ").title(),
                "coverages": []
            })
        data["coverages"] = sections

    # ---------- ELIGIBILITY ----------
    if isinstance(data.get("eligibility"), dict):
        criteria = []
        for k, v in data["eligibility"].items():
            criteria.append({
                "criterion": k.replace("_", " ").title(),
                "details": str(v),
                "is_required": True
            })
        data["eligibility"] = {
            "section_name": "Eligibility",
            "criteria": criteria
        }

    # ---------- CLAIM PROCEDURES ----------
    if isinstance(data.get("claim_procedures"), dict):
        steps = []
        i = 1
        for v in data["claim_procedures"].values():
            steps.append({
                "step_number": i,
                "description": v
            })
            i += 1

        data["claim_procedures"] = [{
            "procedure_name": "Claim Procedure",
            "steps": steps
        }]

    # ---------- OBLIGATIONS ----------
    if isinstance(data.get("obligations"), dict):
        data["obligations"] = {
            "section_name": "Obligations",
            "obligations": [
                {"description": v}
                for v in data["obligations"].values()
            ]
        }

    # ---------- CONTACT INFORMATION ----------
    if isinstance(data.get("contact_information"), dict):
        contacts = []
        for v in data["contact_information"].values():
            if isinstance(v, dict):
                contacts.append(v)

        data["contact_information"] = {
            "section_name": "Contact Information",
            "contacts": contacts
        }

    return data
