
# * sitecast concrete (cast-in-place, in situ)
# * precast concrete
# * masonry - CMU or poured loose

# Strength of concrete: f'c
# Stiffness of concrete: modulus of Elasticity, Ec

# n = Es/Ec -> modulus of Elasticity of steel/concrete
#   = 29000ksi.

def modulus_of_elasticity(strength, weight=145):
    # Since unit weight for ordinary stone-aggregate concrete is 145pcf,
    # average concrete modulus = 57000 * sqrt(strength)
    # in MPa, the constant is 4730
    return weight ** 1.5 * (33 * math.sqrt(strength))

# cover
# code minimum for cover is 3/4" for walls and slabs,
# 1.5" for beams and columns


# phi design strength of individual concrete members
# .90 for flexure, tension, combination
# .70 for columns with spirals
# .65 for columns with ties
# .75 for shear and torsion
# .65 for compressive bearing
# .55 for flexure in plan



def percentage_of_reinforcement(cross_sectional_area, width, effective_depth):
    return cross_sectional_area / (width * effective_depth)

def cross_sectional_area(percentage_of_reinforcement, width, effective_depth):
    return percentage_of_reinforcement * width * effective_depth


# b = width of concrete compression zone
# d = effective depth of the section for stress analysis; from 
#     centroid of steel to edge of compressie zone
# h = overall depth (height) of the section
# As = cross-sectional area of reinforcing bars
# p = percentage of reinforcement; = As/bd


# a represents the compressive zone of concrete, which varies
# based on f'c. For concrete where f'c <= 4000psi, a <= .85c,
# where c = distance from extreme fiber to neutral axis.

# resisting moment as developed by concrete:
# Mc = C*(d-a/2) = .85f'c*ba*(d-a/2)
# Mt = T(d-a/2)=Asfy(d-a/2)

# Equate these formulae to create the balanced section.




# Design for beam shear

# ultimate_shear <= .75 * (concrete_shear_capacity + steel_shear_capacity)

# For beams of normal weight concrete, subjected only to flexure and shear, shear
# force is limited to:

# concrete_shear_capacity = 

# When ultimate_shear exceeds the limit of .75*concrete_shear_capacity, reinformcement must be provided.
# Thus, 
# steel_shear_capacity = (ultimate_shear / .75) - concrete_shear_capacity

# Capacity in tensile resistance of a single, two-legged stirrup is the area * yield stress
# tensile_capacity = cs_area * yield_strength

# More math...



