import re

def count_valid_emails(emails):
    # Basic email regex pattern:
    # 1. Start of string
    # 2. One or more characters that are not @ or whitespace
    # 3. Literal @
    # 4. One or more characters that are not @ or whitespace (domain part)
    # 5. Literal dot
    # 6. One or more characters that are not @ or whitespace (tld part)
    # 7. End of string
    email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    
    count = 0

    if not emails:
        return 0

    for email in emails:
        if isinstance(email, str) and email_pattern.match(email):
            count += 1

    return count