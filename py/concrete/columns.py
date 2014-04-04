

# Design of a column is based on 

# maximum soil pressure
# design soil pressure
# control of settlement
# size of the column
# shear capacity limit for the concrete
# flexural tension stress and development length for the bars
# footing thickness for the development of column bars



# Fundamental failure modes of the tension-weak concrete
# Direct Compression Effect
# Lateral Bursting Effect
# Diagonal Shear Effect


# initial estimate for footing size: load / maximum allowable soil pressure




# Select minimum size column
# 1. adjust axial load by standard factors
# 2. adjust bending moments by standard factors
# 3. compute load eccentricity
# 4. find on chart for axial load / eccentricity.

def equivalent_eccentricity(ultimate_moment, ultimate_load):
    # Refer to figure 15.8, 15.11
    return ultimate_moment  / ultimte_load


def slenderness(length, radius):
    return length / radius


