def detect_phishing(email):
    # Define a list of common phishing keywords
    phishing_keywords = [
        "Dear customer",
        "Click here",
        "Confirm your",
        "Update your",
        "Urgent action required",
        "Verify your",
        "Your account has been suspended",
        "Security breach detected",
        "Unauthorized access"
    ]

    # Check if any phishing keywords appear in the email content
    for keyword in phishing_keywords:
        if keyword.lower() in email.lower():
            return True

    return False

def main():
    # Example email content
    email_content = """
    Dear customer,

    Your account requires immediate attention. Click the link below to verify your account information:
    http://example.com/verify-account

    Thank you,
    Example Bank
    """

    # Detect phishing based on email content
    if detect_phishing(email_content):
        print("Warning: This email may be a phishing attempt.")
    else:
        print("This email appears to be legitimate.")


main()
