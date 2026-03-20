q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    
    # intersección de los dos segmentos
    izq = max(l1, l2)
    der = min(r1, r2)
    
    # dos puntos distintos dentro de la intersección
    a = izq
    b = der  # der siempre >= izq + 1 (garantizado)
    
    print(a, b)