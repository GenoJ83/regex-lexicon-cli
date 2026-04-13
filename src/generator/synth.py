import random
import string

def generate_matching_email() -> str:
    user = "".join(random.choices(string.ascii_lowercase, k=6))
    domain = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"{user}@{domain}.com"
