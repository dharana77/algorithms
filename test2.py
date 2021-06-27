def solution(sticker):
    answer = 0

    if len(sticker)==1:
        return sticker[0]

    dp = [0]*(len(sticker))
    dp[0]=sticker[0]

    if sticker[0]>sticker[1]:
        dp[1]=sticker[0]
    else:
        dp[1]=sticker[1]

    # sticker+=sticker
    for i in range(2,len(sticker)):
        if dp[i-1]>dp[i-2]+sticker[i]:
            dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-2]+sticker[i]
    mx1 = dp[len(sticker)-2]

    first = sticker[0]
    sticker=sticker[1:]
    sticker.append(first)

    dp = [0]*(len(sticker))
    dp[0]=sticker[0]

    if sticker[0]>sticker[1]:
        dp[1]=sticker[0]
    else:
        dp[1]=sticker[1]
    for i in range(2,len(sticker)):
        if dp[i-1]>dp[i-2]+sticker[i]:
            dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-2]+sticker[i]
    mx2 = dp[len(sticker)-2]

    if mx1>mx2:
        answer=mx1
    else:
        answer=mx2

    return answer