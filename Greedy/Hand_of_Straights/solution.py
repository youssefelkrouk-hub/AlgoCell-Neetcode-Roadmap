class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        n = len( hand ) 
        if n % groupSize != 0 : 
            return False 
        count = Counter(hand)
        hand.sort()
        for num in hand :
            if count[num]  :
                for i in range(num,num+groupSize) : 
                    if not count[i] :
                        return False 
                    count[i] -=1 
        return True 
        