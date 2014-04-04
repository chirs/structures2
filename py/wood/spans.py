
"""
Wood spanning elements


## intro

* solid-sawn - cut directly from logs
* plywood panel - glue together three or more thin plies - used for wall sheathing, roof/floor decking
* paper, cardboard, particle board - reconstitute individual fibers

fiber industry technology steadily advancing - fiber paneling slowly replacing plywood, wood boards.


## structural lumber

individual pieces of lumber are marked for identification as to wood species, grade (quality), size,
usage classification, and grading authority.

apart from species, the most important factors are density, grain pattern, natural defects and moisture content.


### classes of structural lumber

* dimension lumber
* beams and stringers
* posts and timbers
* decking

### classes of trees

trees are either softwood or hardwood; pine, fir, redwood are softwoods, typically coniferous.
Douglas fir and Southern pine common structural lumber - both softwoods.

### dimensions




"""




"""

### plywood

glue together multiple layers of thin wood veneer with alternating layers having grain at right angles. (How is plywood made?)


"""



"""

### glued laminated products


### wood fiber products

wafer board or flake board


### assembled wood structural products

sandwich panel / stressed-skin panel

"""



"""
Design for bending

beams must be considered for shear, deflection, end bearing, and lateral buckling, as well as for bending stress.

Procedure:
1. determine maximum bending moment
2. select species and grade
3. from table 5.1, determine basic allowable bending stress
4. consider appropriate modifications for design stress value
5. using bending stress formula, find required section modulus
6. select a beam size from table A.8
7. investigate applicable concerns.

common forms of bracing consist of bridging and blocking
briding consists of crisscrossed wood or metal members in rows
blocking consists of solid, short pieces of lumber the same size as the framing.

"""


def section_modulus(maximum_bending_moment, allowable_bending_stress):
    # the flexure formula
    return maximum_bending_moment / allowable_bending_stress




"""

beam shear


wood is relatively weak in shear resistance; typical failure is a horizontal splitting of the beam ends.

"""


def horizontal_shear_stress(vertical_shear_force, cs_area):
    return 1.5 * vertical_shear_force / cs_area


"""

bearing


bearing occurs at beam ends. a beam sits on a support or when a concentrated load
is placed on top of a beam within the span. stress is compression perpindicular to grain.

"""

def bearing_stress(bearing_force, contact_area):
    return bearing force / contact_area





"""

deflection

tends to be most critical for rafters and joists - where span-to-depth ratios are often pushed to limits.
long-term high levels of bending stress may cause sag.


limiting span to depth ratio of 25 to 1: practical span limit for general purposes.

"""

def deflection(length, beam_depth, Fb=1500, E=1500.0):
    # for uniform loads only.
    return (5 * L**2 * Fb) / (24 * E * beam_depth)



def equivalent_uniform_loading(moment, length):
    # To a point-loaded beam
    return 8.0 * moment / length


"""

behavior considerations for lrfd

one difference (of course) is the use of ultimate load for design rather than service load.

in LRFD, resistance is derived in total force effect form

"""



