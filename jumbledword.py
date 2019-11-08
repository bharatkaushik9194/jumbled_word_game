import random


def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics',
             'convinient', 'technology', 'board', 'ecology', 'education']
    pick = random.choice(words)
    return pick


def jumble(word):
    jumbled = " ".join(random.sample(word, len(word)))
    return jumbled


def thank(p1name, p2name, pp1, pp2):
    print(p1name, "your score is :", pp1)
    print(p2name, "your score is :", pp2)
    print("thanks for playing")


def play():
    p1name = input("player 1 , enter your name \n")
    p2name = input("player 2 , enter your name \n")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(True):
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)

        if turn % 2 == 0:
            print(p1name, "your  turn")
            ans = input("what is on my mind ? \n")
            if ans == picked_word:
                pp1 = pp1+1
                print("your score is :", pp1)
            else:
                print("better luck next time. I thought:", picked_word)
            c = int(input("press 1 to continue and 0 to quit \n"))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break

        else:
            print(p2name, "your  turn")
            ans = input("what is on my mind ? \n")
            if ans == picked_word:
                pp2 = pp2+1
                print("your score is :", pp2)
            else:
                print("better luck next time. I thought:", picked_word)
            c = int(input("press 1 to continue and 0 to quit \n"))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        turn = turn+1


play()
