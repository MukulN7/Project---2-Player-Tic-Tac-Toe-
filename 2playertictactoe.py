#Initialising the program and greeeting the user
print("Hello players!\nWelcome To the best-tic-tac-toe game you have ever played!\nTo learn how to play the game:Type 'Help'\nTo Start the match:Type 'Start'\nTo exit the program:Type 'Quit'")
while (True):
    while (True):
        #Taking the input start help or quit until a valid input is put
        userinput = str(input("Type 'Start or Help or Quit':"))
        if userinput.lower().strip() in ["start","help","quit"]:
             break
    if userinput.lower().strip()=="start":
        #Basic foundation of the program
        R1=[".",".","."]
        R2=[".",".","."]
        R3=[".",".","."]
        filledchoices = set()
        #The while true for keeping the program running until the match is finished
        while (True):
            #Taking P1's input
            while (True):
                if filledchoices == {1,2,3,4,5,6,7,8,9,}:
                    break
                if R1[0]==R1[1]==R1[2]=="X" or R2[0]==R2[1]==R2[2]=="X" or R3[0]==R3[1]==R3[2]=="X" or R1[0]==R2[0]==R3[0]=="X" or R1[1]==R2[1]==R3[1]=="X" or R1[2]==R2[2]==R3[2]=="X" or R1[0]==R2[1]==R3[2]=="X" or R1[2]==R2[1]==R3[0]=="X":
                    break
                if R1[0]==R1[1]==R1[2]=="O" or R2[0]==R2[1]==R2[2]=="O" or R3[0]==R3[1]==R3[2]=="O" or R1[0]==R2[0]==R3[0]=="O" or R1[1]==R2[1]==R3[1]=="O" or R1[2]==R2[2]==R3[2]=="O" or R1[0]==R2[1]==R3[2]=="O" or R1[2]==R2[1]==R3[0]=="O":
                    break
                print("  ".join(R1),"  ".join(R2),"  ".join(R3),sep="\n")
                try:
                    p1m = int(input("P1's Move: "))
                except ValueError:
                        print("P1,Please enter a number from 1 to 9")
                        continue
                if (p1m > 9 or p1m < 1):
                    print("P1,Please enter a number from 1 to 9")
                    continue
                elif p1m in filledchoices:
                    print("Place already occupied")
                    continue
                elif p1m == 1:
                    filledchoices.add(1)
                    R1[0]="X"
                    break
                elif p1m == 2:
                    filledchoices.add(2)
                    R1[1]="X"
                    break
                elif p1m == 3:
                    filledchoices.add(3)
                    R1[2]="X"
                    break
                elif p1m == 4:
                    filledchoices.add(4)
                    R2[0]="X"
                    break
                elif p1m == 5:
                    filledchoices.add(5)
                    R2[1]="X"
                    break
                elif p1m == 6:
                    filledchoices.add(6)
                    R2[2]="X"
                    break
                elif p1m == 7:
                    filledchoices.add(7)
                    R3[0]="X"
                    break
                elif p1m == 8:
                    filledchoices.add(8)
                    R3[1]="X"
                    break
                elif p1m == 9:
                    filledchoices.add(9)
                    R3[2]="X"
                    break 
            #Taking P2's input
            while (True):
                if filledchoices == {1,2,3,4,5,6,7,8,9,}:
                    break
                if R1[0]==R1[1]==R1[2]=="X" or R2[0]==R2[1]==R2[2]=="X" or R3[0]==R3[1]==R3[2]=="X" or R1[0]==R2[0]==R3[0]=="X" or R1[1]==R2[1]==R3[1]=="X" or R1[2]==R2[2]==R3[2]=="X" or R1[0]==R2[1]==R3[2]=="X" or R1[2]==R2[1]==R3[0]=="X":
                    break
                if R1[0]==R1[1]==R1[2]=="O" or R2[0]==R2[1]==R2[2]=="O" or R3[0]==R3[1]==R3[2]=="O" or R1[0]==R2[0]==R3[0]=="O" or R1[1]==R2[1]==R3[1]=="O" or R1[2]==R2[2]==R3[2]=="O" or R1[0]==R2[1]==R3[2]=="O" or R1[2]==R2[1]==R3[0]=="O":
                    break
                print("  ".join(R1),"  ".join(R2),"  ".join(R3),sep="\n")
                try:
                    p2m = int(input("P2's Move: "))
                except ValueError:
                        print("P2,Please enter a number from 1 to 9")
                        continue
                if (p2m > 9 or p2m < 1):
                    print("P2,Please enter a number from 1 to 9")
                    continue
                elif p2m in filledchoices:
                    print("Place already occupied")
                    continue
                elif p2m == 1:
                    filledchoices.add(1)
                    R1[0]="O"
                    break
                elif p2m == 2:
                    filledchoices.add(2)
                    R1[1]="O"
                    break
                elif p2m == 3:
                    filledchoices.add(3)
                    R1[2]="O"
                    break
                elif p2m == 4:
                    filledchoices.add(4)
                    R2[0]="O"
                    break
                elif p2m == 5:
                    filledchoices.add(5)
                    R2[1]="O"
                    break
                elif p2m == 6:
                    filledchoices.add(6)
                    R2[2]="O"
                    break
                elif p2m == 7:
                    filledchoices.add(7)
                    R3[0]="O"
                    break
                elif p2m == 8:
                    filledchoices.add(8)
                    R3[1]="O"
                    break
                elif p2m == 9:
                    filledchoices.add(9)
                    R3[2]="O"
                    break 
            if filledchoices == {1,2,3,4,5,6,7,8,9,}:
                print("Match is a draw!")
                break
            if R1[0]==R1[1]==R1[2]=="X" or R2[0]==R2[1]==R2[2]=="X" or R3[0]==R3[1]==R3[2]=="X" or R1[0]==R2[0]==R3[0]=="X" or R1[1]==R2[1]==R3[1]=="X" or R1[2]==R2[2]==R3[2]=="X" or R1[0]==R2[1]==R3[2]=="X" or R1[2]==R2[1]==R3[0]=="X":
                print("P1 Wins Hurrayyy!")
                break
            if R1[0]==R1[1]==R1[2]=="O" or R2[0]==R2[1]==R2[2]=="O" or R3[0]==R3[1]==R3[2]=="O" or R1[0]==R2[0]==R3[0]=="O" or R1[1]==R2[1]==R3[1]=="O" or R1[2]==R2[2]==R3[2]=="O" or R1[0]==R2[1]==R3[2]=="O" or R1[2]==R2[1]==R3[0]=="O":
                print("P2 Wins Hurrayyy!")
                break
        #After match stuff giving the optionality to keep the program running and the functionality to replay again
        print("  ".join(R1),"  ".join(R2),"  ".join(R3),"Match Finished","To play again type:start","To Exit the program type:'Quit'",sep="\n")
    elif userinput.lower().strip()=="help":
        print("So the goal of this game is to connect 3 rows or columns or diagonals of your own simbol in a straight line\nPlayer 1's simbol is 'X' by default and player 2's symbol is 'O'\n You input Your choices By putting in the number associated with each dot where you wonna put your symbol\nThe numbers to be put for each dots are represented below:\n1  2  3\n4  5  6\n7  8  9")
    elif userinput.lower().strip()=="quit":
        break