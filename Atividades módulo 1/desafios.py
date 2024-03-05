# #desafio 1
N = int(input())

while(N > 0):
    A = input().split()
    B = input().split()

    if len(B) > len(A) or A[-len(B):] != B:
        print("nao encaixa")
    else: 
        print("encaixa")
    N-=1

