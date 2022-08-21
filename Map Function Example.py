scores = [365, 450, 290, 398, 270, 430]

def percent(li):
    return (li*100)/500 

mapped_list = map(percent, scores)

print(list(mapped_list))