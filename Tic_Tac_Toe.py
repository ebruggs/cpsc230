list=[[' ','1',' ','|',' ','2',' ','|',' ','3',' '],
    ['___',' ','___',' ','___'],
    [' ','4',' ','|',' ','5',' ','|',' ','6',' '],
    ['___',' ','___',' ','___'],
    [' ','7',' ','|',' ','8',' ','|',' ','9',' ']]   
def board():
    list1=''.join(list[0])
    list2=''.join(list[1])
    list3=''.join(list[2])
    list4=''.join(list[3])
    list5=''.join(list[4])
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
def xturn():
    print("x turn")
    turn=input("Which space would you like to place your piece?")
    while turn not in [list[0][1],list[0][5],list[0][9],list[2][1],list[2][5],list[2][9],list[4][1],list[4][5],list[4][9]] or turn=='x' or turn=='o':
            print("Not a valid input")
            turn=input("Which space would you like to place your piece?")
    for row in list:
        for i in row:
            if i==turn:
                spot=row.index(i)
                row[spot]='x'
def oturn():
    print("o turn")
    turn=input("Which space would you like to place your piece?")
    while turn not in [list[0][1],list[0][5],list[0][9],list[2][1],list[2][5],list[2][9],list[4][1],list[4][5],list[4][9]] or turn=='x' or turn=='o':
            print("not a valid input")
            turn=input("Which space would you like to place your piece?")
    for row in list:
        for i in row:
            if i==turn:
                spot=row.index(i)
                row[spot]='o'
def check():
    s1=list[0][1]
    s2=list[0][5]
    s3=list[0][9]
    s4=list[2][1]
    s5=list[2][5]
    s6=list[2][9]
    s7=list[4][1]
    s8=list[4][5]
    s9=list[4][9]
    if s1=='x' and s2=='x' and s3=='x':
        return 'x wins'
    elif s4=='x' and s5=='x' and s6=='x':
        return 'x wins'
    elif s7=='x' and s8=='x' and s9=='x':
        return 'x wins'
    elif s1=='x' and s4=='x' and s7=='x':
        return 'x wins'
    elif s2=='x' and s5=='x' and s8=='x':
        return 'x wins'
    elif s3=='x' and s6=='x' and s9=='x':
        return 'x wins'
    elif s1=='x' and s5=='x' and s9=='x':
        return 'x wins'
    elif s3=='x' and s5=='x' and s7=='x':
        return 'x wins'
    elif s1=='o' and s2=='o' and s3=='o':
        return 'o wins'
    elif s4=='o' and s5=='o' and s6=='o':
        return 'o wins'
    elif s7=='o' and s8=='o' and s9=='o':
        return 'o wins'
    elif s1=='o' and s4=='o' and s7=='o':
        return 'o wins'
    elif s2=='o' and s5=='o' and s8=='o':
        return 'o wins'
    elif s3=='o' and s6=='o' and s9=='o':
        return 'o wins'
    elif s1=='o' and s5=='o' and s9=='o':
        return 'o wins'
    elif s3=='o' and s5=='o' and s7=='o':
        return 'o wins'
    else:
        return "Tie Game"
board()
turncount=0
while check()!='x wins' and check()!='o wins' and turncount<9:
    xturn()
    board()
    check()
    turncount+=1
    if check()=='x wins':
        break
    if turncount>8:
        break
    oturn()
    board()
    check()
    turncount+=1
print(check())
print("Game over")
