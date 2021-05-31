def hex2dec(n):
    ans = 0
    x = 1
    s = len(n)
    for i in range(s-1, -1, -1):
        if n[i] >= '0' and n[i] <= '9':
            ans += x*(int(n[i]))
        elif n[i] >= 'A' and n[i] <= 'F':
            ans += x*(ord(n[i])-ord('A')+10)
        x *= 16
    return ans


print(hex2dec('12A1B23'))
