from random import choice

def play():
    u = 0 # user score
    c = 0 # comp score
    while u < 3 and c < 3:
        user = input("r, p, s: ").lower()
        computer = choice(["r", "p", "s"])

        if user == computer: # if it's a tie
            print(f"It's a tie, computer also picked {computer}")
            continue

        if userWin(user, computer):
            print(f"You win, computer picked {computer}")
            u += 1
        else:
            print(f"You lost, computer picked {computer}")
            c += 1

        print(f"Score: {u} - {c}")

# if you win, return true, else return false
def userWin(user, computer):
    if (user == "p" and computer == "r") or (user == "s" and computer == "p") or (user == "r" and computer == "s"):
        return True
    return False

play()