n, m, k = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applicants.sort()
apartments.sort()

i = j = matches = 0

while i < n and j < m:
    if abs(applicants[i] - apartments[j]) <= k:
        matches += 1
        i += 1
        j += 1
    elif applicants[i] < apartments[j] - k:
        i += 1
    else:
        j += 1

print(matches)
