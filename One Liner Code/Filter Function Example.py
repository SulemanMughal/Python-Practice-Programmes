scores = [76, 23,54,12,65,43]

def score_check(s):
    if s > 50:
        return True
    return False

students_passed = filter(score_check, scores)

for i in students_passed:
    print(i)