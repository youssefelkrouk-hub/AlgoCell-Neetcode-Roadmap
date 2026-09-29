def sum_sequare(n):
    output=0
    while n!=0:
        digit=n%10
        output+=digit
        n=n//10
    return output
# a solution using tow point
def happy_number(n):
    slow,fast=n,sum_sequare(n)
    while slow!=fast:
        slow=sum_sequare(slow)
        fast=sum_sequare(sum_sequare(fast))
    return fast==1

print(happy_number(19))