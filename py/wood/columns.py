import math

"""

## Wood columns


A short column fails in crushing - determined by mass and stress limit for compression
A long column fails in buckling - determined by stiffness in bending and modulus of elasticity

"""


class WoodColumn(object):

    def __init__(self, length, compression=None, width=None, depth=None, unbraced_length=None):

        self.length = length # unbraced.
        self.unbraced_length = unbraced_length or self.length

        self.width = width
        self.depth = depth

        self.compression = compression

    @property
    def critical_dimension(self):
        return min(self.width, self.depth)

    def slenderness_ratio(self):
        return self.unbraced_length / float(self.critical_dimension)

    @property
    def cs_area(self):
        return self.width * self.depth


    def allowable_compression_load(self, dv_compression):
        return self.cs_area * self.stability * dv_compression
        



EULER = 1

def slenderness(unbraced_length, width, depth):
    # maximum slenderness ratio for simple solid columns is ~50.
    return unbraced_length / float(min(width, depth))


def allowable_compression_load(cs_area, dv_compression, stability):
    return cs_area * dv_compression * stability

def column_stability(dv_compression, wood_type):
    factor = {
        'sawn_lumber': .8,
        'poles'; .85,
        'glued': .9,
        }[wood_type]

    buckling_stress = (.822 * modulus_of_elasticity) / (float(unbraced_length)

    ratio = 1.0 * buckling_stress / dv_compression

    a = (1 + ratio) / 2 * factor
    b = a ** 2 - (ratio / factor)
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

there are many situations where structural members undergo simultaneous axial compression and bending.
studs in interior walls take gravity plus wind loads.

common cases involving axial compression and bending
1. exterior stud or truss chord
2. column with bracketed support for spanning member.


fa/Fa + fb/Fb <=1
proportion of allowable bending force plus proportion fo allowable load force <= 1.
"""


def interaction_relationship(Pn, Po, Mn, Mo):
    return Pn/Po + Mn/Mo <= 1





