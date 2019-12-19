#--- imput params.
N, L = input().split(' ')
length_list = list(map(int, [input() for _ in range(int(N))]))

#--- main
cnt, residue = 1, int(L)
for i in range(len(length_list) - 1):
    residue = residue - length_list[i]
    if residue >=  length_list[i+1]: pass
    else:
        cnt = cnt + 1
        residue = int(L)
print(cnt)
