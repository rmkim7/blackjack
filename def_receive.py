import random

def receive(n):

    cards = 0

    #첫번째 카드 받기
    n = random.randint(1, 10)
    n = int(input())
    cards += n
    return n

if __name__=='__main__':
    user_num = int(input('type integer between 1 to 10:'))
    receive(user_num)


