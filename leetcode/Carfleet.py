class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: return 1

        pairs = sorted(zip(position, speed))
        
        position , speed = zip(*pairs)
        position = list(position)
        speed = list(speed)

        time = [(target - p)/s for p,s in zip(position,speed)]

        s = []

        for i in time:
            while s and i >= s[-1]:
                s.pop()
            s.append(i)
        return len(s)

