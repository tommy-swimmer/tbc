# Ultimate Bearing Capacity of Soil
# Find the ultimate bearing capacity of soil by using Terzaghi Bearing Capacity Theory
# Tommy Swimmer
# December 21, 2020
# Fort Lewis College

import math

# Qualify "shallow foundation" description.
# D_f >> B
D_f = 48 # inches
B = 16 # inches
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
c_prime = 420 # lb/ft^2 (soil type SM-saturated, UCSC Classification)

#  Unit weight of soil: gamma
gamma = 75 # lb/ft^3 (approximate weight of loose earth)

q = gamma * (D_f/12) # dimensionless (?)

# Let's make phi_prime = 23 degrees (can find experimentally if needed)
# Based on Table 3.1...

N_c = 21.75
N_q = 10.23
N_gamma = 6

# Record Used Values
print('c_prime:', c_prime, 'lb/ft^2', '\ngamma:', gamma, 'lb/ft^3', '\nq:', math.ceil(q),
    '\nN_c', N_c, '\nN_q', N_q, '\nN_gamma', N_gamma, sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))

# Circular Foundation Equation
q_u = (1.3 * c_prime * N_c) + (q * N_q) + (0.3 * gamma * B * N_gamma)
print('\nUltimate Bearing Capacity is:', math.ceil(q_u/1000), 'kip/ft^2', sep=" ")

# Print out results
print('Ultimate Bearing Capacity:', math.ceil(q_u/1000), 'kip/ft^2',
      sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))

# Factor of Safety
FS = 3
q_all = (q_u/1000) / FS
print('\nq_all:', math.ceil(q_all), 'kip/ft^2', sep=" ")
print('q_all:', math.ceil(q_all), 'kip/ft^2', sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))

# Total allowable gross load
Q = q_all * math.pi * ((B/12)/2)**2
print('\nQ:', math.ceil(Q), 'kip/ft^2', sep=" ")
print('Q:', math.ceil(Q), 'kip/ft^2', sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))