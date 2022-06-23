## 18 - ALGORITMOS DE ORDENAMIENTO
'''
Como se puede observar caso de la busqueda binaria en muchas ocaciones es necesario partir de una lista de datos
ordenada, por este motivo existen distintos algoritmos que permiten ordenar una lista, algunos de los cuales
estudiaremos a contimuación
'''

# TODO: sin conocimiento previo, intente organizar una lista de datos

'''
existen dos tipos de algoritmos de ordenamientos, los algoritmos estables y los inestables. 
en un algoritmo estable se mantiene el orden relativo, es decir si existen datos repetidos, estos siempre 
ocuparán la misma posición tras aplicar el algoritmo 
por otra parte, los algoritmos inestables, no mantendran el orden de los datos relativos 
'''
# códigos tomados de: http://lwh.free.fr/pages/algo/tri/tri_es.htm
## Algoritmos estables
'''
Entre los algoritmos estables enconrtarmos 
inserción
burbuja
burbuja bidireccional 
gnome 
mezcla 
'''

# inserción
def Insertion_sort(Vector):
    for i in range(1,len(Vector)):
        actual = Vector[i]
        j = i
        #Desplazamiento de los elementos de la matriz }
        while j>0 and Vector[j-1]>actual:
            Vector[j]=Vector[j-1]
            j = j-1
        #insertar el elemento en su lugar
        Vector[j]=actual
    return Vector

# Burbuja
def bubble_sort(vector):
    permutation = True
    iteración = 0
    while permutation == True:
        permutation = False
        iteración = iteración + 1
        for actual in range(0, len(vector) - iteración):
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
    return vector

#burbuja Bidireccional

def cocktail_sort(vector):
    permutation,dirección,actual = True,1,0
    comienzo,fin = 0,len(vector)-2
    while permutation == True:
        permutation = False
        while (actual<fin and dirección==1) or \
        (actual>comienzo and dirección==-1) :
            # Prueba si intercambio
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
            actual = actual + dirección
        # Cambiar la dirección de desplazamiento
        if dirección==1:
            fin = fin - 1
        else:
            comienzo = comienzo + 1
        dirección = -dirección
    return vector

# gnome

def Gnome_sort(vector):
    i_b,i_i,taille = 1,2,len(vector)
    while i_b < taille:
        if vector[i_b-1] <= vector[i_b]:
            i_b,i_i = i_i, i_i+1
        else:
            vector[i_b-1],vector[i_b] = vector[i_b],vector[i_b-1]
            i_b -= 1
            if i_b == 0:
                i_b,i_i = i_i, i_i+1
    return vector

# mezcla
# algoritmo tomado de: https://pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html#:~:text=El%20algoritmo%20de%20ordenamiento%20por,solo%20un%20elemento%20de%20longitud.
# Función merge_sort
def merge_sort(lista):
    """
    Lo primero que se ve en el psudocódigo es un if que
    comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
    ¿Por que? Ya esta ordenada.
    """
    if len(lista) < 2:
        return lista

    # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)


# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0  # Variables de incremento
    result = []  # Lista de resultado

    # Intercalar ordenadamente
    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]

    # Retornamos el resultados
    return result

## algoritmos inestables

'''
En cuanto a los algorimos inestables encontramos
selección 
peine 
shell 
monticulos 
quick sort
'''

#selección
def selection_sort(vector):
    nb = len(vector)
    for actual in range(0,nb):
        mas_pequeno = actual
        for j in range(actual+1,nb) :
            if vector[j] < vector[mas_pequeno] :
                mas_pequeno = j
        if min is not actual :
            temp = vector[actual]
            vector[actual] = vector[mas_pequeno]
            vector[mas_pequeno] = temp
#peine
import math
def comb_sort(vector):
    permutación = True
    gap = len(vector)
    while (permutación == True) or  (gap>1):
        permutación = False
        gap = math.floor(gap / 1.3)
        if gap<1: gap = 1
        for actual in range(0, len(vector) - gap):
            if vector[actual] > vector[actual + gap]:
                permutación = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + gap] = \
                vector[actual + gap],vector[actual]
    return vector
#shell

def tri_insertion(tableau, gap, debut):
    for i in range(gap + debut, len(tableau), gap):
        en_cours = tableau[i]
        j = i
        # décalage des éléments du tableau }
        while j > 0 and tableau[j - gap] > en_cours:
            tableau[j] = tableau[j - gap]
            j = j - gap
        # on insère l'élément à sa place
        tableau[j] = en_cours


def tri_shell(tableau):
    for gap in [6, 4, 3, 2, 1]:
        # Pour chaque sous-tableau ...
        for debut in range(0, gap):
            # ... on fait un tri par insertion
            tri_insertion(tableau, gap, debut)
#monticulos

#código tomado de: https://beastieux.com/2011/01/24/codigo-python-ordenamiento-heapsort/

def heapsort(lista, tam):
    for k in range(tam - 1, -1, -1):
        for i in range(0, k):
            item = lista[i]
            j = (i + 1) / 2
            while j >= 0 and lista[j] < item:
                lista[i] = lista[j]
                i = j
                j = j / 2
            lista[i] = item
        temp = lista[0];
    lista[0] = lista[k];
    lista[k] = temp;
    return lista




#quick sort
def quick_sort(vector):
    if not vector:
        return []
    else:
        pivote = vector[-1]
        menor = [x for x in vector     if x <  pivote]
        mas_grande = [x for x in vector[:-1] if x >= pivote]
        return quick_sort(menor) + [pivote] + quick_sort(mas_grande)


#TODO: generar la documentación para cada uno de los algoritmos mostrados anteriormente
#TODO: verificar el tiempo de ejecución de los distintos métodos haciendo uso de listas con distintas longitudes
#   y condiciones iniciales (aleatoria, ordenado, invertido)
#TODO: verificar si los algoritmos son estables o no
#TODO: Revisar en la documentación de python que algoritmo implementa la función sort y porqué