from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

def dfs(node, tree, subordinates):
    # Minden gyerek bejárása
    for child in tree[node]:
        subordinates[node] += dfs(child, tree, subordinates)  # Gyerekek beosztottainak hozzáadása
    return subordinates[node] + 1  # Saját magát is számolja

def solve():
    n = int(input())  # Alkalmazottak száma
    bosses = list(map(int, input().split()))  # Közvetlen főnökök listája
    
    # Gráf építése (adjacency list)
    tree = defaultdict(list)
    for i in range(n - 1):
        tree[bosses[i]].append(i + 2)  # Az alkalmazottak száma 2-től indul

    # Beosztottak számának tárolása
    subordinates = [0] * (n + 1)  # Minden csomóponthoz 0-ról indul
    
    # DFS meghívása a gyökérre
    dfs(1, tree, subordinates)
    
    # Eredmények kiírása (az 1-től n-ig tartó csomópontokhoz)
    print(" ".join(map(str, subordinates[1:])))

# Példa futtatása
solve()
