def fibonocciSeq(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 1:
        ans =  fibonocciSeq(x-1) + fibonocciSeq(x-2)
        return ans
        
    
steps = int(input('Enter the range : '))
this_com = [fibonocciSeq(x) for x in range(steps+1)]
print(this_com)
