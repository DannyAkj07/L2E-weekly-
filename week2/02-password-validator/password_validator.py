def has_min_length(password: str) -> bool:
    # Write your code here
    return len(password) >= 8


def has_uppercase(password):
    # Write your code here
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password):
    # Write your code here
    for char in password:
        if char.islower():
            return True
    return False


def has_digit(password):
    # Write your code here
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special(password: str) -> bool:
    # Write your code here
    for char in password:
        if not char.isalnum() and not char.isspace():
            return True
    return False


def is_valid_password(password):
    # Write your code here
    return has_min_length(password) and has_digit(password) and has_lowercase(password) and has_uppercase(password) and has_special(password) 

# bonus
def get_failed_requirements(password):
    # Write your code here
    rules = {
        "min_length": has_min_length,
        "uppercase": has_uppercase,
        "uppercase": has_lowercase,
        "digit": has_digit,
        "special": has_special
    }
    failed = []
    for name, name_error in rules.items():
        if not name_error(password):
            failed.append(name)
    return failed

    # ==== OR ====
    # return [name for name,name_error in rules.items() if not name_error(password)]

    # === OR ===
    # failed = []
    # if not has_min_length(password):
    #     failed.append("min_length")
    # if not has_uppercase(password):
    #     failed.append("uppercase")
    # if not has_lowercase(password):
    #     failed.append("lowercase")
    # if not has_digit(password):
    #     failed.append("digit")
    # if not has_special(password):
    #     failed.append("special")

    # return failed

# print(is_valid_password('Hello@122'))
print(get_failed_requirements("Hello2"))