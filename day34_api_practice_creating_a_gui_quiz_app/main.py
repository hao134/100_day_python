# age: int
# name: str
# height: float
# is_human: bool


def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "They can Drive" # Type hint is bool, but return value not the boolean