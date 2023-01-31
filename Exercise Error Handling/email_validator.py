from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_name = r'[\w\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = [".com", ".bg", ".org", ".net"]
email = input()
while email != "End":
    try:
        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if findall(pattern_name, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots.")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    except IndexError:
        print("Invalid email")
    else:
        print("Email is valid")
    email = input()
