import math

"""
entropy = Boltzmann constant * natural logarithm(number of microscopic configurations)
S = kB*ln(Ω)

"""

entropy = 0
boltzmann_constant = 1.380649e-23 # J/K
microscopic_configurations = 10e23

entropy = boltzmann_constant * math.log(microscopic_configurations)
print("Entropy is: ",entropy, "J/K")