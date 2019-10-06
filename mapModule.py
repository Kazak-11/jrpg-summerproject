def gen(size): #Генерирует матрицу, заполненную "+", используется как карта местности
    a=[]
    for i in range(size):
        a.append([])
        for j in range(size):
            a[i].append('+')
    return a

def print_array(a): #Печает матрицу, которую передали, используя буферную переменную string для каждой строки вывода
    size = len(a)
    for i in range(size):
        string = ''
        for j in range(size):
            string = string +' ' + a[i][j]
        print(string)

def over(a,b): #Накладывает матрицу b на матрицу a(как в фотошопе слои)
    size = len(a)
    c = []
    for i in range(size):
        c.append([])
        for j in range(size):
            if b[i][j] == '+':
                c[i].append(a[i][j])
            else:
                c[i].append(b[i][j].mark)
    return c