#level 2 problems

# Find 33

def has_33(lis):
    count=0
    
    for item in lis:
        if item==3:
            count+=1
        else:
            count=0
        if count==2:
            return True
    return False

# paper doll

def paper_doll(st):
    ans=''
    
    for i in range(len(st)):
        for k in range(1,4):
            ans+=st[i]
    return ans

# Black Jack

def blackjack(a,b,c):
    summ=a+b+c
    if summ<=21:
        return summ
    if summ>21 and (a==11 or b==11 or c==11) :
        summ-=10
    if summ>21:
        return 'BUST'
    else:
        return a+b+c-10

# Summer of '69

def summer_69(arr):
    flag=False
    summ=0
    
    for item in arr:
        if item==6:
            flag=True
        elif item==9 and flag==True:
            flag=False
            continue
        if flag==True:
            continue
        else:
            summ=summ+item
    return summ
