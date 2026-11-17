class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # closest to target first
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        # loop through each cars
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)