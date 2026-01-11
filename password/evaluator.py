from password.blocklist import is_blocklisted
from utils.entropy import estimate_entropy


def evaluate_password(password):

    findings = []
    recommendations = []

    length = len(password)
    words = password.split()

    print("\nPassword Security Evaluation")
    print("----------------------------")

    # Length Evaluation
    if length < 8:
        findings.append("Password length is critically short.")
        recommendations.append(
            "Use a password or passphrase of at least 12 characters."
        )
    elif length < 12:
        findings.append("Password length is below recommended minimum.")
        recommendations.append(
            "Increase password length to at least 12 characters."
        )
    else:
        findings.append("Password length meets recommended standards.")

    # Passphrase Detection
    if len(words) >= 2:
        findings.append("Passphrase detected (multiple words).")
    else:
        recommendations.append(
            "Consider using a multi-word passphrase for better memorability and security."
        )

    # Blocklist Check
    if is_blocklisted(password):
        findings.append("Password is present in a common or breached password list.")
        recommendations.append(
            "Choose a password that is unique and not present in known breach datasets."
        )

    # Truncation Risk Awareness
    if length > 64:
        findings.append(
            "Password exceeds 64 characters; backend systems may truncate input."
        )

    # Entropy Estimation (Offline Cracking Resistance)
    entropy_bits = estimate_entropy(password)

    if entropy_bits < 40:
        findings.append("Estimated entropy is low, indicating weak resistance to cracking.")
        recommendations.append("Increase password length or use a multi-word passphrase.")
    elif entropy_bits < 60:
        findings.append("Estimated entropy is moderate.")
    else:
        findings.append("Estimated entropy is strong.")

    # Output Report
    print("\nFindings:")
    for item in findings:
        print(f"- {item}")

    if recommendations:
        print("\nRecommendations:")
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("\nNo critical issues identified. Password aligns with modern guidance.")
