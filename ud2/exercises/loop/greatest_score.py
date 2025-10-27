best_score = 100
best_name = ""

name = input()
while name != "END":
    score = int(input())
    if score > best_score:
        best_score = score
        best_name = name

    name = input()

print(f"{best_name}: {best_score}")