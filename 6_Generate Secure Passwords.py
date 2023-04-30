import random
num=['0','1','2','3','4','5','6','7','8','9']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sym=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','$','#','_']
spe=['$','#','_']
s=input('SHOULD A RANDOM PASSWORD BE GENERATED?(Y/N)')
pas=''
while s in 'YESyes':
    for i in range(8):
        pas+=random.choice(alpha)
    for i in range(2):
        pas+=random.choice(num)
    pas+=random.choice(spe)
    for i in range(16-len(pas)):
        pas+=random.choice(sym)
    if len(pas)>=16:
        break
if s in 'yesYES':
    print("PASSWORD GENERATED")
    print(pas)
else:
    print('Thanks for visiting')
    