def solution(s1, s2):
    answer = ''
    pre = ""
    post = ""
    for i in range(len(s2)-1):
        pre+="!"
        post+="!"
    first = pre+s1+post
    
    
    lst = []
    for i in range(len(first)-len(s2)+1):
        s3 = ""
        t = 0
        fin = True
        left = False
        right = False
        for j in range(len(s2)):
            if first[i+j]!="!" and first[i+j]!=s2[j]:
                fin = False
                break

            if first[i+j]==s2[j]:
                t+=1
                s3+=s2[j]
            else:
                if first[i+j]=="!":
                    idx = (i+j)
                    if idx>=0 and idx<=len(s2)-1:
                        left=True
                    else:
                        right=True 
                    s3+=s2[j]    
            
        if fin:
            if left:
                for i in range(t,len(s1)):
                    s3+=s1[i]
            else:
                temp = ""
                for i in range(0,len(s1)-1):
                    temp+=s1[i] 
                s3= temp+s3 

            lst.append(s3)
        # print(s3)
        # print(t)

    print(lst)
    
    if s1==s2:  
        answer =s1
        
    return answer

a=solution("xyZA","ABCxy")
b=solution("AxA","AyA")
print(a)
print(b)