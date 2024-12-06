MOD = 10**9 + 7

def count_ways(n):
    dp = [0] * (n + 1)  # dp tömb inicializálása
    dp[0] = 1  # 0-t egyetlen módon érhetjük el

    # Külső ciklus végigmegy az összes értéken 1-től n-ig
    for i in range(1, n + 1):
        # Belső ciklus a dobások 1-től 6-ig terjednek
        for j in range(1, 7):
            if i - j >= 0:  # Csak akkor, ha az i - j nem negatív
                dp[i] = (dp[i] + dp[i - j]) % MOD

    return dp[n]  # Az eredmény: hányféleképpen érhetjük el n-t

# Bemenet
n = int(input())
print(count_ways(n))
