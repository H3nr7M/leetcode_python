'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
'''
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Combinar las posiciones y velocidades en una lista de tuplas
        cars = sorted(zip(position, speed), reverse=True)
        # [(10,2),(8,4),(5,1),(3,3),(0,1)]
        
        # Función para calcular el tiempo que tardará un auto en llegar al destino
        def time_to_reach(car_pos, car_speed):
            return (target - car_pos) / car_speed
        
        fleets = 0
        last_fleet_time = float('-inf')
        
        for pos, speed in cars:
            arrival_time = time_to_reach(pos, speed)
            
            # Si el auto llega después del último auto en la flota actual,
            # se crea una nueva flota y se actualiza el tiempo de llegada del último auto
            if arrival_time > last_fleet_time:
                fleets += 1
                last_fleet_time = arrival_time
        
        return fleets
    
sol = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(sol.carFleet(target, position, speed))
