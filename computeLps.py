def computeLPS(s, lps):
    leng = 0 
    i = 1

    while i < len(s):
        if s[i] == s[leng]:
            leng+=1
            lps[i] = leng
            i+=1
        else:
            if leng!=0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i +=1
    return lps

s = "ABCA"
lps = [0]*len(s)

r = computeLPS(s,lps)
print(r)
