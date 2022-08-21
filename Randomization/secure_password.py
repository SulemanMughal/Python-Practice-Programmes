import string
import random
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 4
    return ''.join(random.choice(chars) for x in
    range(size,20))

def main():
    n=0
    while n<50:
        print(randompassword())
        n=n+1

if __name__ == "__main__":
    main()