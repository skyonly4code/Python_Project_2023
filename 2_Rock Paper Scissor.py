import random
rps=['ROCK','PAPER','SCISSOR']
print("LET'S PLAY ROCK PAPER SCISSOR".rjust(60))
s=input('DO YOU WANT TO PLAY?(Y/N):'.rjust(58))
match=0
w=0
l=0
t=0
while s in 'YESyes':
    match+=1
    ai=random.choice(rps)
    print('ENTER 1 FOR ROCK'.rjust(55))
    print('ENTER 2 FOR PAPER'.rjust(56))
    print('ENTER 3 FOR SCISSOR'.rjust(57))
    n=int(input())
    if (n==1 and ai=='ROCK') or (n==2 and ai=='PAPER') or (n==3 and ai=='SCISSOR'):
        print("IT'S A TIE!!!".rjust(54))
        t+=1
        pass
    elif (n==1 and ai=='PAPER') or (n==2 and ai=='SCISSOR') or(n==3 and ai=='ROCK'):
        print('YOU LOSE...'.rjust(54))
        l+=1
    elif (n==1 and ai=='SCISSOR') or (n==2 and ai=='ROCK') or(n==3 and ai=='PAPER'):
        print('YOU WIN!!!'.rjust(54))
        w+=1
    else:
        print('CHOOSE FROM 1,2 OR 3 ONLY')
        continue
    print(f'TOTAL MATCHES:{match}'.rjust(55))
    print(f'YOUR WINS::{w}'.rjust(55))
    print(f'YOUR LOSSES::{l}'.rjust(55))
    print(f'TIES::{t}'.rjust(55))
    s=input('DO YOU WANT TO PLAY AGAIN?(Y/N):'.rjust(60))
print('THANK YOU FOR PLAYING!!!'.rjust(60))