from policy.questions import POLICY_CONTROLS

def calculate_score(responses):

    total_weight = 0
    achieved_weight = 0
    failed_controls = []

    for control in POLICY_CONTROLS:
        weight = control["weight"]
        control_id = control["id"]

        total_weight += weight

        if responses.get(control_id):
            achieved_weight += weight
        else:
            failed_controls.append(control)
    
    compliance_percentage = (achieved_weight / total_weight) * 100

    return {
        "total_weight": total_weight,
        "achieved_weight": achieved_weight,
        "percentage": round(compliance_percentage, 2),
        "risk_level": determine_risk_level(compliance_percentage),
        "failed_controls": failed_controls
    }

def determine_risk_level(percentage):
    # Determines overall risk level based on compliance percentage.
    if percentage >= 80:
        return "Compliant"
    elif percentage >= 60:
        return "Partially Compliant"
    else:
        return "Non-Compliant"
    
def generate_report(score_data):
    # Generates a structured, human-readable compliance report.
    report = []
    report.append("\nPassword Policy Compliance Report")
    report.append("---------------------------------")
    report.append(f"Compliance Score: {score_data['percentage']}%")
    report.append(f"Status: {score_data['risk_level']}")

    if score_data["failed_controls"]:
        report.append("\nIdentified Gaps and Recommendations:")

        for control in score_data["failed_controls"]:
            report.append(
                f"\n[{control['category']}]"
                f"\nIssue: {control['question']}"
                f"\nRecommendation: {control['osi_suggestion']}"
            )
    else:
        report.append("\nNo policy gaps identified. The password policy is aligned with OWASP guidance.")
    return "\n".join(report)