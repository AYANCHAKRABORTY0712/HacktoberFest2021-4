import random
t=[]
pos=['1','2','3','4','5','6','7','8','9']
mwin=0;cwin=0;draw=0
while(1):
    m=input("Choose your player: X or O\n")
    if(m=='X'): 
        c='O'
        break
    elif(m=='O'): 
        c='X'
        break
    else: 
        print("Select a valid choice")
while(1):
    m_ts=int(input("Let's flip a coin to choose who will give the first turn:\n Select your side: Press 1 for Head Or  0 for Tail\n"))
    toss=random.randint(0,1)
    if(m_ts!=0 and m_ts!=1):
        print("Select a valid choice")
        continue
    if(toss==m_ts):
        print("You Won The Toss. First turn is yours.")
        tw=1
        break
    else:
        print("Computer Won The Toss. Computer will give the first turn.")
        tw=0
        break
start=input("Press any key to start the game.")
def game_board(n,pl):
    print("**********")
    for i in range(3):
        for j in range(3):
            if(t[i][j]==n):
                t[i][j]=pl
            if(j==2):
                print(t[i][j])
            else:
                print(t[i][j],end='  ')
    print("**********\n")
def game_executer():
    game=0
    for k in range(3):
        if((t[k][0]==t[k][1] and t[k][1]==t[k][2]) or
           (t[0][k]==t[1][k] and t[1][k]==t[2][k])):
            game=1
            break
    if(game==0):
        if((t[0][0]==t[1][1] and t[1][1]==t[2][2]) or 
           (t[0][2]==t[1][1] and t[1][1]==t[2][0])):
            game=1
    if(game==0):
        game=-1
        for i in t:
            for j in i:
                if j in pos:
                    game=0
                    break
    return game
def computer_turn():
    turn=0
    """searching winning scope"""
    for k in range(3):
        hor=sorted(t[k])
        ver=sorted([t[0][k],t[1][k],t[2][k]])
        if(hor[0] in pos and hor[1]==c and hor[2]==c):
            turn=hor[0]
            break
        if(ver[0] in pos and ver[1]==c and ver[2]==c):
            turn=ver[0]
            break
    if(turn==0):
        d1=sorted([t[0][0],t[1][1],t[2][2]])
        d2=sorted([t[0][2],t[1][1],t[2][0]])
        if(d1[0] in pos and d1[1]==c and d1[2]==c):
            turn=d1[0]
        elif(d2[0] in pos and d2[1]==c and d2[2]==c):
            turn=d2[0]
    """defensive"""
    if(turn==0):
        for k in range(3):
            hor=sorted(t[k])
            ver=sorted([t[0][k],t[1][k],t[2][k]])
            if(hor[0] in pos and hor[1]==m and hor[2]==m):
                turn=hor[0]
                break
            if(ver[0] in pos and ver[1]==m and ver[2]==m):
                turn=ver[0]
                break
        if(turn==0):
            d1=sorted([t[0][0],t[1][1],t[2][2]])
            d2=sorted([t[0][2],t[1][1],t[2][0]])
            if(d1[0] in pos and d1[1]==m and d1[2]==m):
                turn=d1[0]
            elif(d2[0] in pos and d2[1]==m and d2[2]==m):
                turn=d2[0]
    """offensive"""
    if(turn==0):
        for k in range(3):
            hor=sorted(t[k])
            ver=sorted([t[0][k],t[1][k],t[2][k]])
            if(hor[0] in pos and hor[1] in pos and hor[2]==m):
                turn=random.choice([hor[0],hor[1]])
                break
            if(ver[0] in pos and ver[1] in pos and ver[2]==m):
                turn=random.choice([ver[0],ver[1]])
                break
        if(turn==0):
            d1=sorted([t[0][0],t[1][1],t[2][2]])
            d2=sorted([t[0][2],t[1][1],t[2][0]])
            if(d1[0] in pos and d1[1] in pos and d1[2]==m):
                turn=random.choice([d1[0],d1[1]])
            elif(d2[0] in pos and d2[1] in pos and d2[2]==m):
                turn=random.choice([d2[0],d2[1]])
    """random"""
    if(turn==0):
        while(1):
            i=random.randint(0,2)
            j=random.randint(0,2)
            if t[i][j] in pos:
                turn=t[i][j]
                break
    return turn
while(1):
    t=[['1','2','3'],['4','5','6'],['7','8','9']]
    game_board(0,0)
    if(tw==1):
        while(1):
            mturn=input("\n\n\nYour turn. Enter position:- ")
            game_board(mturn,m)
            if(game_executer()==1):
                print("You Won!!!")
                mwin+=1
                break
            elif(game_executer()==-1):
                print("Game Drawn")
                draw+=1
                break
            cturn=computer_turn()
            game_board(cturn,c)
            if(game_executer()==1):
                print("Computer Won.")
                cwin+=1
                break
    elif(tw==0):   
        while(1):
            cturn=computer_turn()
            game_board(cturn,c)
            if(game_executer()==1):
                print("Computer Won.")
                cwin+=1
                break
            elif(game_executer()==-1):
                print("Game Drawn")
                draw+=1
                break
            mturn=input("\n\n\nYour turn. Enter position:- ")
            game_board(mturn,m)
            if(game_executer()==1):
                print("You Won!!!")
                mwin+=1
                break
    print("You:> %d\t\tComputer:> %d\t\tDrawn:> %d"%(mwin,cwin,draw))
    yn=input("Do you want to play again?: if yes press y, else press any key ")
    if(yn!='y'):
        break



