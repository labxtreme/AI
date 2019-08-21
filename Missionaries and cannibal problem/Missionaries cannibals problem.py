import copy
ans=[]
result=[]
Start_Bank = dict()
Goal_Bank = dict()
steps=['We start here']
Start_Bank['M']=3
Start_Bank['C']=3
Start_Bank['boat']=True
Goal_Bank['M']=0
Goal_Bank['C']=0
Goal_Bank['boat']=False
def cannotdo(A,B):
    if steps[-1]==steps[-2]:
        return True
    elif A['M']==0  and 4>A['C']>0 :
        return False
    elif B['M']==0  and 4>B['C']>0 :
        return False
    elif A['M']<A['C'] or B['M']<B['C'] or 4<A['M']<0 or 4<B['C']<0 or 4<B['M']<0 or 4<B['C']<0:
        return True
    else :
        return False
def Travel(A,B,str):
     if str[0] in A.keys():   
        if A['boat']==True:
            A['boat']=False
            B['boat']=True
            for var in str:
                A[var]=A[var]-1
                B[var]=B[var]+1
        elif B['boat']==True:
            B['boat']=False
            A['boat']=True
            for var in str:
                B[var]=B[var]-1
                A[var]=A[var]+1
        else:
            pass
     else:
        pass
def cando(A,B):
    global steps
    Travel(A,B,'MC')
    checkanddo(A,B,'MC')
    Travel(A,B,'MM')
    if len(result)!=2:
        checkanddo(A,B,'MM')
        Travel(A,B,'CC')
        checkanddo(A,B,'CC')
        Travel(A,B,'M')
        checkanddo(A,B,'M')
        if len(result)!=2:
            Travel(A,B,'C')
            checkanddo(A,B,'C')    
        
def checkanddo(A,B,str):
    global ans
    global result
    steps.append(str)
    if cannotdo(A,B)==True:
            Travel(A,B,str)
            steps.pop(-1)
            return
    elif B['M']==3 and B['C']==3:
        print("reached the result")
        ans=copy.deepcopy(steps)
        result.append(ans[1:])
        A['M']=3
        A['C']=3
        A['boat']=True
        B['M']=0
        B['C']=0
        B['boat']=False
        steps[1:]=[]
    elif A['M']==3 and A['C']==3:
        Travel(A,B,str)
        steps.pop(-1)
        return
    else:
        
        cando(A,B)
        if len(result)!=2:    
            steps.pop(-1)
Travel(Start_Bank,Goal_Bank,'MC')
checkanddo(Start_Bank,Goal_Bank,'MC')
i=0
for var1 in result:
    Start_Bank['M']=3
    Start_Bank['C']=3
    Start_Bank['boat']=True
    Goal_Bank['M']=0
    Goal_Bank['C']=0
    Goal_Bank['boat']=False
    print("\n\n\n")
    i+=1
    print("Solution Number ",i)
    print(var1)
    for var2 in var1:
      Travel(Start_Bank,Goal_Bank,var2)
      print(Start_Bank,Goal_Bank)
