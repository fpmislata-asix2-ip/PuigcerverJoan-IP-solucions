def is_valid(hours, minutes, seconds):
    valid = True
    if hours < 0 or hours > 23:
        print(f"El valor '{hours}' no és vàlid per a les hores.")
        valid = False
    if minutes < 0 or minutes > 59:
        print(f"El valor '{minutes}' no és vàlid per als minuts.")
        valid = False
    if seconds < 0 or seconds > 59:
        print(f"El valor '{seconds}' no és vàlid per als segons.")
        valid = False
    return valid


def next_second(hours, minutes, seconds):
    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


hours = int(input())
minutes = int(input())
seconds = int(input())

valid = is_valid(hours, minutes, seconds)
if valid:
    next_second(hours, minutes, seconds)