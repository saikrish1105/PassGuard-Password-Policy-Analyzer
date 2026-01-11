# PassGuard: Password Policy Analyzer

## Overview

**PassGuard** is a command-line tool designed to help organizations assess and improve their password policies based on modern security guidance from OWASP standards. It evaluates both organizational password policies and individual passwords to ensure they align with best practices, such as using long passphrases, blocking common or breached passwords, and enforcing secure storage and authentication protections.

---

## Motivation

Many enterprises still rely on outdated password rules, like mandatory periodic resets or rigid composition requirements, which are no longer considered secure. This tool provides a **structured, evidence-based approach** to evaluate password policies, helping organizations:

* Identify weaknesses in their current policies
* Stay compliant with modern password security standards
* Encourage strong, user-friendly authentication practices
* Reduce risk from breaches and credential-stuffing attacks

---

## Key Features

* **Policy Compliance Check:** Ask targeted questions to assess organizational password rules.
* **Password Strength Evaluation:** Analyze individual passwords or passphrases for security and adherence to best practices.
* **Blocklist Enforcement:** Detect common or previously breached passwords.
* **Actionable Recommendations:** Suggest improvements to enhance overall authentication security.

---

## How to Run

### 1. Clone the repository

```bash
git clone <https://github.com/saikrish1105/PassGuard-Password-Policy-Analyzer.git>
cd password_policy_analyzer
```

### 2. Run Policy Compliance Check

```bash
python password_analyzer.py policy-check
```

You will be prompted to answer questions about your organization’s password policy. A compliance score and recommendations will be displayed.

### 3. Evaluate a Password

```bash
python password_analyzer.py password-check -p "yourPasswordHere"
```

The tool will analyze the password, check against blocklists, and provide recommendations for improvement.

---

## Requirements

* Python 3.7+
* No external dependencies required (uses standard Python libraries)
