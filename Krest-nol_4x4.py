

def show_field(f):
    num ='  0   1   2   3'
    print(num)
    #zip
    for row,i in zip(f,num.split()):
        print (f"{i} {'   '.join(str(j) for j in row)}")

def users_input(f,user):
    while True:
        place=input(f"Ходит {user} Введите координаты строка столбец:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        #is digit str
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<4 and y>=0 and  y<4):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y


def win_position(f,user):
    f_list=[]
    print(f)
    for l in f:
        f_list+=l
    print(f_list)
    positions=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==4:
            return True
    return False


def start(field):

    count=0
    while True:
        show_field(field)
        if count%2==0:
            user='x'
        else:
            user = 'o'
        if count<16:
            x, y = users_input(field,user)
            field[x][y] = user

        elif count==16:
            print ('Ничья')
            break
        if win_position(field,user):
            print(f"Выиграл {user}")
            break
        count+=1


field = [['-'] * 4 for _ in range(4)]

start(field)