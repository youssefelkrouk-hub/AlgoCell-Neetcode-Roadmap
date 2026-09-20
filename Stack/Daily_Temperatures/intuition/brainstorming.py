# my first solution is to do this  using the list.index(element) method that scan  sequently the entire list 
def dailyTemperatures( temperatures):
    n=len(temperatures)
    res=[0]*(n)
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=temperatures[i]:
                
                stack.pop()
        res[i]=0 if not stack else temperatures.index(stack[-1])-i
        stack.append(temperatures[i])
    return res
        
temperatures = [73,74,75,71,69,72,76,73]
t=dailyTemperatures(temperatures)
print(t)
# calls temperatures.index(...), which does a linear scan (O(n)) to find the value. 
# Since this runs once per iteration of the outer loop, the total cost becomes O(n) × O(n) = O(n²)


print("other effecient solution without using the index method to get the index of stack[-1] ","\n")

def dailytemperatur(num):
    n,stack=len(num),[]
    res=[0]*(n)
    for i in range(n-1,-1,-1):
        while stack and num[stack[-1]]<=num[i]:
             stack.pop()
        if stack:
            res[i]=stack[-1]-i
        stack.append(i)
    return res

temperatures = [73,74,75,71,69,72,76,73]
t= dailytemperatur(temperatures)
print(t)
               





