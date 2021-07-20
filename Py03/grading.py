LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())

if (not(0 <= LE <= 100) or not(0 <= RE <= 100) or not(0 <= PE <= 100) or not(0 <= TE <= 100)):
    print("Input error")

elif (PE < 40 or TE < 40):
    print("RFC")

else:
    grade = (LE + RE + 5 * PE + 3 * TE) / 50 + 0.0001
    print(round(grade))