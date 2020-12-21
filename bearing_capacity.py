# Ultimate Bearing Capacity of Soil
# Find the ultimate bearing capacity of soil by using Terzaghi Bearing Capacity Theory
# Tommy Swimmer
# December 21, 2020
# Fort Lewis College

import math

# Qualify "shallow foundation" description.
# D_f >> B
D_f = 48 # inches
B = 8 # inches
shallow_foundation = D_f / 8
if shallow_foundation <= 3: # conservative analysis of shallow foundation 
    print('Foundation is considered a deep foundation.')
else:
    print('D_f / B:',shallow_foundation, sep=" ")

# Must define:
    # c' = cohesion of soil
    # gamma = unit weight of soil
    # q = gamma * D_f
    # N_c,N_q,N_gamma = bearing capacity factors that are nondimenstional and are functions only of the soil friction angle psi'

# Cohesion of soil
c_prime = 1 # kips/ft^2 (see Notion table for details, listed as Medium cohesive soil)

#  Unit weight of soil: gamma
gamma = 75 # lb/ft^3 (approximate weight of loose earth)

q = gamma * D_f

# Let's make phi_prime = 23 degrees
# Based on Table 3.1...

N_c = 21.75
N_q = 10.23
N_gamma = 6

# Circular Foundation Equation
q_u = (1.3 * c_prime * N_c) + (q * N_q) + (0.3 * gamma * B * N_gamma)
print('Ultimate Bearing Capacity is:', math.ceil(q_u/1000), 'kip/ft^2', sep=" ")

# Print out results
print('Ultimate Bearing Capacity:', math.ceil(q_u/1000), 'kip/ft^2',
      sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))
