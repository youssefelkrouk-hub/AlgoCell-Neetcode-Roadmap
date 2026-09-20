class Solution(object):
    def carFleet(self, target, position, speed):
        n = len(position)
        pairs = [(position[i], speed[i]) for i in range(n)]
        pairs.sort(reverse=True)
        fleets = 0
        curr = 0 
        for pos, speed in pairs:
            time = ( target - pos )/float(speed)
            if time > curr:
                fleets += 1
                curr = time

        return fleets