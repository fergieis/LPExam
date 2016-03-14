from gurobipy import *

m = Model("LP4")
x1 = m.addVar(vtype="c", name="x1")
x2 = m.addVar(vtype="c", name="x2")
x3 = m.addVar(vtype="c", name="x3")



#E[b]
b = 9

m.update()

#maximize profit, expected cost vector * dvs
m.setObjective(2*x1 + 3*x2 + 1*x3, GRB.MINIMIZE)

#subject to:

# material used in scenario i <= material A available in scenario i, i={1,2,3}
m.addConstr( 3*x1 + 2*x2+ 4*x3 == 9, "A_limit") #b_A1 = 150

#2*red + 2*blue <= min material B available 
#(since the values don't change across scenarios, min is 100)


#DVs are non-negative by default


m.optimize()
for v in m.getVars():		#Solution printing "liberated" from  
	print v.varName, v.x	#Gurobi documentation. 

#fergieis@computerOfFergieis:~/Desktop/LPExam$ gurobi.sh LPExam2.py
#Optimize a model with 4 rows, 2 columns and 8 nonzeros
#Coefficient statistics:
#  Matrix range    [1e+00, 4e+00]
#  Objective range [3e+03, 4e+03]
#  Bounds range    [0e+00, 0e+00]
#  RHS range       [1e+02, 2e+02]
#Presolve time: 0.03s
#Presolved: 4 rows, 2 columns, 8 nonzeros
#
#Iteration    Objective       Primal Inf.    Dual Inf.      Time
#       0    7.1000000e+33   6.500000e+30   7.100000e+03      0s
#       1    1.9500000e+05   0.000000e+00   0.000000e+00      0s
#
#Solved in 1 iterations and 0.04 seconds
#Optimal objective  1.950000000e+05
#Product Red 50.0
#Product Blue 0.0


