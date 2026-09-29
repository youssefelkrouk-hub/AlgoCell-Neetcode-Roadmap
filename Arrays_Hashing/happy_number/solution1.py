# that's a good easy problem,the intuition behind it is to use to detect a cycle :
# let's take an example 19 is happy beacue :
# 1**2+9**2=82
# 8**2+2**2=68
#6**2+8**2=100
#1**2+0**2+0**2=1
# but 2 is not because !!:
# becaue at some point  xe return to 4 = 2**2 in the cycle of sum of the sequare of the digits 

# so i'ill  use a set just to detect if a sum of sequare of digit is already in the hash set,if yes retur False 
# then , if a sequare of the digit is equal to 1 , return True 

def sum_sequare(n):
    output=0
    while n!=0:
        digit=n%10
        output+=digit
        n=n//10
    return output


def is_happy_number(n):
    Hash_set=set()
    while n not in Hash_set:
        Hash_set.add(n)
        n=sum_sequare(n)
        if n==1:
            return True
    return False

print(is_happy_number(19))