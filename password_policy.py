import argparse

from policy.questions import run_policy_check
from policy.scoring import calculate_score, generate_report
from password.evaluator import evaluate_password

def main():
    parser = argparse.ArgumentParser(description="OWASP-Aligned Password Policy Analyzer for Enterprise")
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # policy compliance checker
    subparsers.add_parser("policy-check",
        help="Analayse the organization's password policy compliance with respect to industry standard policies")

    # password strength checker
    password_parser = subparsers.add_parser("pass-check",
        help = "Evaluate a given password against industry standard policies for a strong password")
    password_parser.add_argument("-p",required=True,help="the password to check strength")

    args = parser.parse_args()

    # check command to run
    if args.command == "policy-check":
        responses = run_policy_check()
        score_data = calculate_score(responses)
        report = generate_report(score_data)
        print(report)
    elif args.command == "pass-check":
        evaluate_password(args.p)
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()