s = ["O","X"]
print("you only use ", s ," 2 option")

m = []
for i in range(5):
    r = []
    for j in range(5):
        if( i == 1 or i == 3):
            r.append("----")

        elif( j == 1 or j == 3):
            r.append(" | ")

        else:
            r.append("  . ")

    m.append(r)

for x in m:
    print(" ".join(x))

print(" you choose 9 position \n front = [(0,0),(0,2),(0,4)] \n mid = [(2,0),(2,2),(2,4)] \n back = [(4,0),(4,2),(4,4)]")

for i in range(9):
    p = int(input("enter row position :  "))
    if( p != 0 and p!= 2 and p != 4):
        print("Invalid")
        continue
    q = int(input("enter col position :  "))
    if( q != 0 and q!= 2 and q != 4):
        print("Invalid")
        continue
    r = input(" X or O :  ")
    if( r != "O" and r != "X"):
        print("Invalid")
        continue

    m[p][q] = r
        
    for z in m:
        print(" ".join(z))
        
    if(m[0][0] != "  . " and m[0][0] == m[0][2] == m[0][4] or m[2][2] != "  . " and m[2][0] == m[2][2] == m[2][4] or m[4][4] != "  . " and m[4][0] == m[4][2] == m[4][4]):
        print("you win")
        break
    elif(m[0][0] != "  . " and m[0][0] == m[2][0] == m[4][0] or m[2][2] != "  . " and m[0][2] == m[2][2] == m[4][2] or m[4][4] != "  . " and m[0][4] == m[2][4] == m[4][4]):
        print("you win")
        break
    elif(m[0][0] != "  . " and m[0][0] == m[2][2] == m[4][4] or m[2][2] != "  . " and m[0][4] == m[2][2] == m[4][0]):
        print("you win")
        break
    else:
        print("continue the game")
for b in m:
    print(" ".join(b))

if(m[0][0] != "  . " and m[0][0] == m[0][2] == m[0][4] or m[2][2] != "  . " and m[2][0] == m[2][2] == m[2][4] or m[4][4] != "  . " and m[4][0] == m[4][2] == m[4][4]):
    print("you win")
elif(m[0][0] != "  . " and m[0][0] == m[2][0] == m[4][0] or m[2][2] != "  . " and m[0][2] == m[2][2] == m[4][2] or m[4][4] != "  . " and m[0][4] == m[2][4] == m[4][4]):
    print("you win")
elif(m[0][0] != "  . " and m[0][0] == m[2][2] == m[4][4] or m[2][2] != "  . " and m[0][4] == m[2][2] == m[4][0]):
    print("you win")
else:
    print("Match tie")










                    
               







       
        
        