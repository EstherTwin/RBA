#Robust Gate Assignment

#the goal is to allocate bays to the selected schedule
#There are certain constraints to consider
#The objectives are:
#Minimize the number of ungated flghts
#Minimize the passenger connection time

from __future__ import print_function

import cplex

Gates = ["1A", "1B", "2A","2B","2C","3A"]

#Aircrafts to locate the bays

Aircrafts = ["KQ120", "KQ121", "KQ122", "KQ125", "KQ189", "KQ348"]

#Actual arrival time and actual departure time of each flight

ActualTime = {"KQ120":[10:00,10:50],
              "KQ121":[1:00,1:50],
              "KQ122":[2:00,2:45],
              "KQ125":[3:00,3:50],
              "KQ189":[4:00,4:40],
              "KQ348":[5:00,5:40]}

def allocate():
	model = cplex.Cplex()

	model.solve()


	print()
	print("started"

