# distanza di Levenshtein
# http://www.andreamarino.it/python/pythonds/Techniques/distance-strings-morabito.html

import timeit

def words_distance_levenshtein(words1, words2):
    """
    words1 e words2 sono due liste di parole
    restituisce la distanza di Levenshtein tra le due liste di parole
    """
    if len(words1) == 0:
        return len(words2)
    if len(words2) == 0:
        return len(words1)
    if words1[0] == words2[0]:
        return words_distance_levenshtein(words1[1:], words2[1:])
    else:
        return min(words_distance_levenshtein(words1, words2[1:]),
                   words_distance_levenshtein(words1[1:], words2),
                   words_distance_levenshtein(words1[1:], words2[1:])) + 1

def Distance(str1,str2):

    # Inizializzazione a zero della matrice di dimensione (m+1)x(n+1)
    m=len(str1)+1
    n=len(str2)+1
    D = [[0 for k in range(n)] for k in range(m)]

    # Assegnazione delle soluzioni ai problemi banali
    for i in range(1,m):
        D[i][0]=i
    for j in range(1,n):
        D[0][j]=j

    # Cicli annidati per la risoluzione dei sottoproblemi
    for i in range(1,m):
        for j in range(1,n):

            # Se i caratteri sono diversi
            if str1[i-1]!=str2[j-1]:
                D[i][j]=1+min(D[i][j-1],D[i-1][j],D[i-1][j-1])

            # Se i caratteri sono uguali
            else:
                D[i][j]= D[i-1][j-1]

    # Restituisce la soluzione del problema
    return D[len(str1)][len(str2)]


def Distance2(str1, str2):

    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0:
        return len(str1)

        if str1[-1] != str2[-1]:
            return min(1 + Distance2(str1[:-1], str2), 1 + Distance2(str1, str2[:-1]),
                    1 + Distance2(str1[:-1], str2[:-1]))
    else:
        return Distance2(str1[:-1], str2[:-1])


def Distance3(str1,str2):

   m = len(str1) + 1
   n = len(str2) + 1

   F = [k for k in range(n)]

   for i in range(1,m):

       S = [0 for k in range(n)]
       S[0] = i

       for j in range(1,n):

           if str1[i-1]!=str2[j-1]:
               S[j]=1+min(S[j-1],F[j-1],F[j])
           else:
               S[j]= F[j-1]

       F = S

   return F[-1]


# time the three functions using the timeit module and print the results
print(timeit.timeit("Distance('cristina patatina la vicini rumina in cucina','maria castro castoro rivoltoso')", 
                    setup="from __main__ import Distance", 
                    number=100_000)
                    )
print(timeit.timeit("Distance2('cristina patatina la vicini rumina in cucina','maria castro castoro rivoltoso')", 
                    setup="from __main__ import Distance2", 
                    number=100_000)
                    )
print(timeit.timeit("Distance3('cristina patatina la vicini rumina in cucina','maria castro castoro rivoltoso')", 
                    setup="from __main__ import Distance3", 
                    number=100_000)
                    )
