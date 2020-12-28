# Ultimate Bearing Capacity of Soil
# Find the ultimate bearing capacity of soil by using Terzaghi Bearing Capacity Theory
# Tommy Swimmer
# December 21, 2020
# Fort Lewis College

import math
import sys

# Qualify "shallow foundation" description.
# D_f >> B
D_f = int(input('Enter depth of foundation (inches): ')) # 48 inches

B = int(input('Enter width of foundation (inches): ')) # 8 inches

shallow_foundation = D_f / B
if int(shallow_foundation) <= 3: # conservative analysis of shallow foundation 
    print('Foundation is considered a deep foundation.')
else:
    print('\n Not considered a shallow foundation! \n D_f / B:',shallow_foundation, sep=" ")

# Prompt to continue or not.
print('\nAre you sure? To continue. (y/n)')
prompt = input()
if prompt != "y":
    sys.exit("Exit reason: User inputted n")
    
# Must define:
    # c' = cohesion of soil
    # gamma = unit weight of soil
    # q = gamma * D_f
    # N_c,N_q,N_gamma = bearing capacity factors that are nondimenstional and are functions only of the soil friction angle psi'

# Cohesion of soil
c_prime = int(input('Enter cohesion: ')) # 420 lb/ft^2 (soil type SM-saturated, UCSC Classification)

#  Unit weight of soil: gamma
gamma = int(input('Enter gamma: ')) # 75 lb/ft^3 (approximate weight of loose earth)

q = gamma * (D_f/12) # dimensionless (?)

# Let's make phi_prime = 23 degrees (can find experimentally if needed)
# Based on Table 3.1...

N_c = float(input('Enter N_c: ')) # 21.75
N_q = float(input('Enter N_q: ')) # 10.23
N_gamma = float(input('Enter N_gamma: ')) # 6

# Record Used Values
print('\nWould you like to record used values? (y/n)')
used_prompt = input()
if used_prompt =="y":
    print('c_prime:', c_prime, 'lb/ft^2', '\ngamma:', gamma, 'lb/ft^3', '\nq:', q,
    '\nN_c', N_c, '\nN_q', N_q, '\nN_gamma', N_gamma, sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))
elif used_prompt =="n":
    print('\nNo recorded values')

#-------------- MAIN CALCULATION ----------------------------------------------
# Circular Foundation Equation
q_u = (1.3 * c_prime * N_c) + (q * N_q) + (0.3 * gamma * (B/12) * N_gamma)
print('\nq_u:', q_u, 'kip/ft^2', sep=" ")
#------------------------------------------------------------------------------

# Print out results
print('\nq_u:', q_u/1000, 'kip/ft^2',
      sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))

# Factor of Safety
FS = 3
q_all = (q_u/1000) / FS
print('\nq_all:', q_all, 'kip/ft^2', sep=" ")
print('q_all:', q_all, 'kip/ft^2', sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))

# Total allowable gross load
Q = (q_all * math.pi * ((B/12)/2)**2)*4
print('\nQ:', Q, 'kip', sep=" ")
print('Q:', Q, 'kip', sep=" ", file=open("Ultimate_Bearing_Capacity.txt", "a"))

# Reminder of .txt file export
print('\n Success! Final results are recorded in the Ultimate_Bearing_Capacity text file.')