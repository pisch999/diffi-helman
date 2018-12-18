import random
def diffy():
        new_file = open("output.txt", "w")
        mass=[]
        i=2
        while i<=100:
            f=True
            j=2
            while f and j<i:
                if not i%j: f=False
                j+=1
            if f:
                mass.append(i)
            i+=1
        q =random.choice(mass)
        P = 2*q+1;
        mass_a=[]
        for a in range(1,100):
            if a>1 and a<(P-1):
                if not((a**q) % P == 1):
                    mass_a.append(a)
        A =random.choice(mass_a)
        print(P)
        print(A)
        x1 = int(input('Enter x1: '))
        x2 = int(input('Enter x2: '))
        Y1 = (A**x1)%P
        Y2 = (A**x2)%P
        print(Y1)
        print(Y2)
        Z1 = (Y2)**x1 % P
        Z2= (Y1)**x2 % P
        print('Z1= ',Z1)
        print ('Z2= ',Z2)
        if Z1 == Z2 :
            new_file.write('Z1 equals Z2 = ')
            new_file.write(str(Z2))
        new_file.close()

diffy()
