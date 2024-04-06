from pulp import *

"""
Foods
- SKIN-ON SOCKEYE SALMON WITH BLACKENED BUTTER, $18.98 / LB: https://wildforkfoods.com/products/skin-on-sockeye-salmon-with-blackened-butter/
    - Serving size: 1 portion (170g)(2.66 servings per package)
    - Cost per serving: $7.14
    - Sodium: 570mg (25%)
    - Calories: 410 per serving
    - Protein: 31g
    - Vitamin D: 0 mcg
    - Calcium: 27mg (2%)
    - Iron: 1mg (6%)
    - Potassium: 527mg (10%)


- HERB & OLIVE OIL SEASONED PORK TENDERLOIN, $3.98 / LB: https://wildforkfoods.com/products/herb-olive-oil-seasoned-pork-tenderloin/
    - Serving size: 112g
    - Cost per serving: 0.98
    - Sodium: 270mg (12%)
    - Calories: 130 per serving
    - Protein: 23g
    - Vitamin D: 0mcg
    - Calcium: 13mg (2%)
    - Iron: 1mg (6%)
    - Potassium: 547mg (10%)
    

- MEXICAN STYLE STREET CORN - FAMILY SIZE, $7.98 / 1.5 LB: https://wildforkfoods.com/products/mexican-style-street-corn/
    - Serving size: 1/2 cup (113g)
    - Cost per serving: 1.33
    - Sodium: 150 mg (7%)
    - Calories: 160
    - Protein: 5g
    - Vitamin D: 0%
    - Calcium: 64mg (4%)
    - Iron: 1mg (6%)
    - Potassium: 225mg (4%)

- SKIN-ON GOLDBAND SNAPPER WITH MEDITERRANEAN BUTTER, $14.98 / lb: https://wildforkfoods.com/products/goldband-snapper-with-mediterranean-butter/
    - Cost per serving: $6.57
    - Serving size: 198g
    - Sodium: 310mg
    - Calories: 350
    - Protein: 35g
    - Vitamin D: 17mcg
    - Calcium: 74mg
    - Iron: 1mg
    - Potassium: 734mg

- MUSHROOM & TRUFFLE PIZZA, $8.98: https://wildforkfoods.com/products/mushroom-truffle-pizza-1/
    - Serving size: 1/3 pizza (136g)
    - Cost per serving: 2.99
    - Sodium: 700mg (31%)
    - Calories: 350
    - Protein: 12g
    - Vitamin D: 0mcg
    - Calcium: 158mg (10%)
    - Iron: 0.79mg (4%)
    - Potassium: 262mg (6%)
"""


# Defining the decision variables
salmon = LpVariable("salmon", 0, None)
pork = LpVariable("pork", 0, None)
corn = LpVariable("corn", 0, None)
snapper = LpVariable("snapper", 0, None)
pizza = LpVariable("pizza", 0, None)

# Defining the problem - we want to minimize the cost/servings, so it should be a minimization problem
prob = LpProblem("problem", LpMinimize)

# Define the constraints
prob += 570*salmon + 270*pork + 150*corn + 310*snapper + 700*pizza   <= 35000   # sodium constraint
prob += 410*salmon + 130*pork + 160*corn + 350*snapper + 350*pizza   >= 14000   # calorie constraint
prob +=  31*salmon +  23*pork +   5*corn +  35*snapper +  12*pizza   >=   350   # protein constraint
prob +=                                     17*snapper               >=   140   # vitamin d constraint
prob +=  27*salmon +  13*pork +  64*corn +  74*snapper + 158*pizza   >=  9100   # calcium constraint
prob +=   1*salmon +   1*pork +   1*corn +   1*snapper + 0.79*pizza  >=   126   # iron constraint
prob += 527*salmon + 547*pork + 225*corn + 734*snapper + 262*pizza   >= 32900   # potassium constraint

# Define the objective function
prob += 7.14*salmon + 0.98*pork + 1.33*corn + 6.57*snapper + 2.99*pizza 

# Solve the problem
status = prob.solve()
print(f"Problem 1")
print(f"status={LpStatus[status]}")

for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(prob.objective)}")
print(f"")


# Part 4 - require at least 1 serving of each food item
# Re-define the decision variables with a lower bound of 1
salmon = LpVariable("salmon", 1, None)
pork = LpVariable("pork", 1, None)
corn = LpVariable("corn", 1, None)
snapper = LpVariable("snapper", 1, None)
pizza = LpVariable("pizza", 1, None)


# Solve the problem again with the new lower bounds
# Defining the problem - we want to minimize the cost/servings, so it should be a minimization problem
prob = LpProblem("problem2", LpMinimize)

# Define the constraints
prob += 570*salmon + 270*pork + 150*corn + 310*snapper + 700*pizza   <= 35000   # sodium constraint
prob += 410*salmon + 130*pork + 160*corn + 350*snapper + 350*pizza   >= 14000   # calorie constraint
prob +=  31*salmon +  23*pork +   5*corn +  35*snapper +  12*pizza   >=   350   # protein constraint
prob +=                                     17*snapper               >=   140   # vitamin d constraint
prob +=  27*salmon +  13*pork +  64*corn +  74*snapper + 158*pizza   >=  9100   # calcium constraint
prob +=   1*salmon +   1*pork +   1*corn +   1*snapper + 0.79*pizza  >=   126   # iron constraint
prob += 527*salmon + 547*pork + 225*corn + 734*snapper + 262*pizza   >= 32900   # potassium constraint

# Define the objective function
prob += 7.14*salmon + 0.98*pork + 1.33*corn + 6.57*snapper + 2.99*pizza 

# Solve the problem
status = prob.solve()
print(f"Problem 2")
print(f"status={LpStatus[status]}")

for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(prob.objective)}")
print(f"")