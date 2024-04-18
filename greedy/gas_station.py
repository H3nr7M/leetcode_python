'''
There are n gas stations along a circular route, where the amount of gas at the 
ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel 
from the ith station to its next (i + 1)th station. You begin the journey with an 
empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if 
you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
'''

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
   
        total_gas = 0
        total_cost = 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            
            # Si en algún punto nos quedamos sin gas, reiniciamos el tanque y 
            #marcamos la siguiente estación como posible punto de inicio.
            if tank < 0:
                tank = 0
                start = i + 1
        
        # Si la suma total de gasolina es menor que la suma total de costos, 
        #no hay suficiente gas para completar el circuito.
        if total_gas < total_cost:
            return -1
        else:
            return start if start < len(gas) else -1
    
sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas, cost))
