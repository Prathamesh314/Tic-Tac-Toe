import os

arr = [["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]]

chance = 1;
def createTable():
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("|","---","|","---","|","---","|"))
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("|",f"{arr[0][0]}","|",f"{arr[0][1]}","|",f"{arr[0][2]}","|"))
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("|","---","|","---","|","---","|"))
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("|",f"{arr[1][0]}","|",f"{arr[1][1]}","|",f"{arr[1][2]}","|"))
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("|","---","|","---","|","---","|"))
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format("|",f"{arr[2][0]}","|",f"{arr[2][1]}","|",f"{arr[2][2]}","|"))


def updateTable(row: int, col:int,chance:int)->int:
    if(arr[row][col]=="-"):
        if(chance == 1):
            arr[row][col] = "X";
            return 1
        else:
            arr[row][col] = "O"
            return 1
    else:
        return 0
        
        
def checkwin():
    flag = 0
    if(arr[0][0]=="X" and arr[0][1]=="X" and arr[0][2]=="X" or arr[0][0]=="X" and arr[1][0]=="X" and arr[2][0]=="X"):
        return 2;
    if(arr[1][0]=="X" and arr[1][1]=="X" and arr[1][2]=="X" or arr[0][1]=="X" and arr[1][1]=="X" and arr[2][1]=="X"):
        return 2;
    if(arr[2][0]=="X" and arr[2][1]=="X" and arr[2][2]=="X" or arr[0][2]=="X" and arr[1][2]=="X" and arr[2][2]=="X"):
        return 2;
    if(arr[0][0]=="X" and arr[1][1]=="X" and arr[2][2]=="X" or arr[0][2]=="X" and arr[1][1]=="X" and arr[2][0]=="X"):
        return 2;
    if(arr[0][0]=="O" and arr[0][1]=="O" and arr[0][2]=="O" or arr[0][0]=="O" and arr[1][0]=="O" and arr[2][0]=="O"):
        return 1;
    if(arr[1][0]=="O" and arr[1][1]=="O" and arr[1][2]=="O" or arr[0][1]=="O" and arr[1][1]=="O" and arr[2][1]=="O"):
        return 1;
    if(arr[2][0]=="O" and arr[2][1]=="O" and arr[2][2]=="O" or arr[0][2]=="O" and arr[1][2]=="O" and arr[2][2]=="O"):
        return 1;
    if(arr[0][0]=="O" and arr[1][1]=="O" and arr[2][2]=="O" or arr[0][2]=="O" and arr[1][1]=="O" and arr[2][0]=="O"):
        return 1;
    else:
        for i in arr:
            if("-" in i):
                flag=1
                
        if(flag != 1):
            return 0
    


if __name__ == '__main__':
    print("***** Welcome to Tic-Tac-Toe made by Prathamesh *****")
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of player 2: ")
    players = [player1,player2]
    resp = int(input("Enter 1 for 'X' and 0 for 'O' : "))
    createTable()
    while(1):
        if(chance==1):
            print(f"{players[0]} turn...")
        else:
            print(f"{players[1]} turn...")
        box = int(input("Enter numbers from 1-9 to select the box: "))
        q = (box-1)//3;
        r = (box-1)%3;
        os.system("cls")
        while(updateTable(q,r,chance)!=1):
            createTable()
            box = int(input("Enter numbers from 1-9 to select the box: "))
            q = (box-1)//3;
            r = (box-1)%3;
            if(chance == 1):
                print(f"{players[0]} turn...")
            else:
                print(f"{players[1]} turn...")
        os.system("cls")
        updateTable(q,r,chance)
        createTable()
        chance = -1*chance
        if(checkwin()==2):
            print(f"{player1} wins...")
            break;
        elif(checkwin()==1):
            print(f"{player2} wins...")
            break;
        elif(checkwin()==0):
            print("Match Drawn...")
            break;



