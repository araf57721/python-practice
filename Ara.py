for i in range():
    for j in range(7):
        if(i == 0):
            if(j == 1 or j == 2 or j == 4 or j ==5):
                print("&", end = " ")
            elif(j == 6):
                print(" ")
            else:
                print(" ", end = " ")    

        elif(i == 1):
            if(j == 0 or j == 3 ):
                print("&", end = " ")
            elif(j == 6):
                print("&")
            else:
                print(" ", end = " ")

        elif(i == 2):
            if(j == 1 or j == 5 ):
                print("&", end = " ")
            elif(j == 6):
                print(" ")
            else:
                print(" ", end = " ")

        elif(i == 3):
            if(j == 2 or j == 4 ):
                print("&", end = " ")
            elif(j == 6):
                print(" ")
            else:
                print(" ", end = " ")

        elif(i == 4):
            if( j == 3 ):
                print("&", end = " ")
            elif(j == 6):
                print(" ")
            else:
                print(" ", end = " ")