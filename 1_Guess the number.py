import random
s = input("DO YOU WANT TO GUESS THE NUMBER ?(Y/N) ")
while s in 'YESyes':
    n=random.randint(0,100)
    c=0
    while True:
        num=int(input('ENTER YOUR GUESS:'))
        if num==n:
            c+=1
            print('YOU WON IN:',c,'TURNS')
            print('YOUR SCORE IS:',(100-c))
            break
        elif num<=n:
            if (n-num)<=10:
                print('YOU ARE CLOSE...TRY A LITTLE HIGHER')
                c+=1
            else:
                print("TRY A HIGHER NUMBER")
                c+=1
        elif num>=n:
            if (num-n)<=10:
                print("YOU ARE CLOSE...TRY A LOWER NUMBER")
                c+=1
            else:
                print("TRY A LOWER NUMBER")
                c+=1
    s=input("DO YOU WANT TO GUESS AGAIN?(Y/N) ")
print("THANK YUO FOR PLAYING")
    