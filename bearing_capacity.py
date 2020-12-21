# Ultimate Bearing Capacity of Soil
# Find the ultimate bearing capacity of soil by using Terzaghi Bearing Capacity Theory
# Tommy Swimmer
# December 21, 2020
# Fort Lewis College

# Qualify "shallow foundation" description.
# D_f >> B
D_f = 48 # inches
B = 8 # inches
shallow_foundation = D_f / 8
if shallow_foundation <= 3: # conservative analysis of shallow foundation
    print('Foundation is considered a deep foundation.')
else:
    print('D_f / B:',shallow_foundation, sep=" ")

