class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: return 1

#        pairs = sorted(zip(position, speed))
#        
#        position , speed = zip(*pairs)
#        position = list(position)
#        speed = list(speed)
#
#        time = [(target - p)/s for p,s in zip(position,speed)]
#
#        s = []
#
#        for i in time:
#            while s and i >= s[-1]:
#                s.pop()
#            s.append(i)
#        return len(s)
# this is a faster smarter idea but it is not a stack
        fleets = 0
        how_long_next_fleet_is_taking = 0
        cars = sorted(zip(position,speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos)/spd
            if time > how_long_next_fleet_is_taking:
                fleets += 1
                how_long_next_fleet_is_taking = time
        return fleets

