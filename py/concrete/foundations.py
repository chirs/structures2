import math

# Footing

#Footing width is determined by soil pressure, assuming that the minimum width required for construction is not adequate for bearing.

#Transverse reinforcement is not required until the footing width exceeds the wall thickness by some significant amount, usually 2 ft or so. A good rule of thumb is to provide transverse reinforcement only if the cantilever edge distance for the footing (from the wall face to the footing edge) exceeds the footing thickness. For average conditions, this means for footings of about 3 ft width or greater.

# Cover requirements are for 2 in. from formed edges and 3 in. from surfaces generated without forming (such as the footing bottom).

SOIL_PRESSURE = 4000

# Multipliers
feet_to_inches = 1 / 12.0
inches_to_feet = 12


ultimate_shear = factored_design_soil_pressure * shear_section_distance * feet_to_inches



def concrete_shear_capacity(concrete_strength, width, effective_depth):
    return 2 * math.sqrt(concrete_strength) * width * effective_depth




# Column footings

def footing_weight(height):
    return 150 * height / 12


def bending_force(soil_pressure, shear_distance, square_footage):
    return soil_pressure * (shear_distance / 12.0) * square_footage

def bending_moment(bending_force, shear_distance):
    return bending_force * (shear_distance / 12.0) * .5


def column_footing_beam_shear(soil_pressure, width, shear_section):
    return soil_pressure * width * shear_section


def column_footing_punch_shear(soil_pressure, width, shear_section):
    return soil_pressure * (width**2 - shear_section**2)


