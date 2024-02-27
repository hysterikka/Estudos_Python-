import random
def play ():
    user = input ("'r' para pedra, 'p' para papel, 't' para tesoura ")
    computer = random.choice (['r', 'p', 't'])

    if user == computer:
        return 'empate'

            # r > t, t > p, p > r
    if is_win (user, computer) :
        return 'vc venceu'

    return 'vc perdeu :c'    

def is_win (player, oponente):
    #return = true se player vencer
    # r > t, t > p, p > r
    if (player == 'r' and oponente == 't') or (player == 't' and oponente == 'p') \
         or (player == 'p' and oponente == 'r'):
        return True
print (play ())        