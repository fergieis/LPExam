from gurobipy import *

m = Model("LP1")
red = m.addVar(vtype="c", name="Product Red")
blue = m.addVar(vtype="c", name="Product Blue")

#Expected Value of cost coefficients, E[c]
c_red = .3*2000 + .2*4000 + .5*5000
c_blue = .3*3000 + .2*4000 + .5*3000

#E[b]
b_A = .3*150 + .2*200 + .5*200
b_B = .3*200 + .2*180 + .5*100
m.update()


#maximize profit, expected cost vector * dvs
m.setObjective(c_red * red + c_blue * blue, GRB.MAXIMIZE)

#subject to:

#sum of expected value of material A usage per dv unit * dvs <= material A available
m.addConstr((.3*1+.2*4+.5*3) * red + (.3*2+.2*3+.5*2)*blue <= b_A, "A_limit")

#2*red + 2*blue <= material B available (since the values don't change across scenarios)
m.addConstr(              2  * red +               2 *blue <= b_B, "B_limit")

#DVs are non-negative by default


m.optimize()
for v in m.getVars():		#Solution printing "liberated" from  
	print v.varName, v.x	#Gurobi documentation. 

#fergieis@computerOfFergieis:~/Desktop/LPExam$ gurobi.sh LPExam1.py
#Optimize a model with 2 rows, 2 columns and 4 nonzeros
#Coefficient statistics:
#  Matrix range    [2e+00, 3e+00]
#  Objective range [3e+03, 4e+03]
#  Bounds range    [0e+00, 0e+00]
#  RHS range       [1e+02, 2e+02]
#Presolve time: 0.00s
#Presolved: 2 rows, 2 columns, 4 nonzeros
#
#Iteration    Objective       Primal Inf.    Dual Inf.      Time
#       0    7.1000000e+33   3.200000e+30   7.100000e+03      0s
#       2    2.7750000e+05   0.000000e+00   0.000000e+00      0s
#
#Solved in 2 iterations and 0.00 seconds
#Optimal objective  2.775000000e+05
#Product Red 71.1538461538
#Product Blue 0.0

