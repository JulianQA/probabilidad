def norma(m1):
    res = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res += (m1[i][j][0])**2 + (m1[i][j][1])**2
    raiz = res**0.5
    return raiz

def suma(a,b):
    ent = a[0]+b[0]
    imag = a[1]+b[1]
    return ent,imag
def multiplicacion(a,b):  
    first = a[0] * b[0]
    second = a[0] * b[1]
    third = a[1] * b[0]
    fourth = a[1] * b[1]
    ent = first-fourth
    imag = second+third
    return ent,imag
def multiplicacion_matrices(m1,m2):
    matriz_res = [[(0,0)]*len(m2[0]) for i in range(len(m1))]
    cos = 0
    if len(matriz_res) == 1:
        cos = 1
        
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(matriz_res)+cos):
                matriz_res[i][j] = suma(matriz_res[i][j],multiplicacion(m1[i][k],m2[k][j]))
    return matriz_res

def transpuesta(m1):
    matriz_res = [[None]*len(m1) for i in range(len(m1[0]))]

    for i in range(len(matriz_res)):
        for j in range(len(matriz_res[0])):

            matriz_res[i][j] = m1[j][i]
    return matriz_res

def conju(a):
    res = (a[0],a[1]*-1)
    return res

def mat_conjugada(m1):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m1[i][j] = conju(m1[i][j])
    return m1

def mat_adjunta(m1):
    c = mat_conjugada(transpuesta(m1))
    return c


def proba(vec,pos):
    nor = norma(vec)
    arr = vec[pos]
    p = arr[0][0]**2 + arr[0][1]**2
    res = p/(nor)**2
    return res

def trans(vec1,vec2):
    arr = multiplicacion_matrices(mat_adjunta(vec2),vec1)
    aba = norma(vec1)*norma(vec2)
    izq = arr[0][0][0] / aba
    der = arr[0][0][1] / aba
    res = izq + der
    return res
def hermitian(m1,v1):
    if mat_adjunta(m1) == m1:
        average(m1,v1)
        vari(m1,v1)
    else:
        return False
def average(m1,v1):
    m = multiplicacion_matrices(m1,v1)
    i = mat_adjunta(m)
    res = (i[0][0][0] * v1[0][0][0]) + (i[0][1][1] * v1[1][0][1])
    return res
