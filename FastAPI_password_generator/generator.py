import string 
import random 

def generate_password(length: int =12, include_upper: bool = True, include_digits: bool = True, include_special:bool = False) -> str:
    charset = list(string.ascii_lowercase)
    if include_upper:
        charset += list(string.ascii_uppercase)
    if include_digits:
        charset += list(string.digits)
    if include_special:
        charset += list("!@#$%^&*()-=")
    
    if length < 5: 
        raise ValueError("Minimum password length should be 5.")
    
    return "".join(random.choice(charset) for _ in range(length))

        