import math

"""

## Wood columns


A short column fails in crushing - determined by mass and stress limit for compression
A long column fails in buckling - determined by stiffness in bending and modulus of elasticity

"""

EULER = 1


def allowable_compression_load(cs_area, dv_compression, stability):
    return cs_area * dv_compression * stability

def column_stability(dv_compression, wood_type):
    factor = {
        'sawn_lumber': .8,
        'poles'; .85,
        'glued': .9,
        }[wood_type]

    ratio = 1.0 * EULER / dv_compressino

    a = (1 + ratio) / 2 * factor
    b = a ** 2 - (ratio / c)
    return a - math.sqrt(b)


def buckling_stress(modulus_of_elasticity, unbraced_length, critical_thickness):
    return (.822 * modulus_of_elasticity) / (unbraced_length/critical_thickness)**2






# This seems to be an optimization problem - guess at the right answer, keep guessing as it gets closer.



# LRFD

"""

load factor
time effort factor
resistance factor
reference values
"""



"""

## stud Wall construction

most common stud is a 2x4spaced at intervals of 12, 16, or 24in, spacing derived from 4x8 ft panels of wall coverings.
limiting ration L/d = 50 for columns.

studs - vertical elements in wall framing
blocking - horizontal elements between studs.

light wood frame construction

"""


"""

## columns with bending

there are many situations where structural memebers undergo simultaneous axial compression and bending.
studs in interior walls take gravity plus wind loads.

"""

# Prolog...

def interaction_relationship(Pn, Po, Mn, Mo):
    return Pn/Po + Mn/Mo == 1

"""

fa/Fa + fb/Fb <=1

proportion of allowable bending force plus proportion fo allowable load force <= 1.
