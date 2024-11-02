"""
1 megaparsec (3.09*10**19 km)
this is for if i have the constant already if not ill need
to revies it, since the hubbles constant is velocity moving
away from earth over distance from earth it shouldnt be hard
"""


def age(hub_cons):
    """So for this it takes Hubbles cons and outputs the age"""
    MEGPAR_TO_KM = 3.09 * (10 ** 19)  # pylint: disable=C0103
    return MEGPAR_TO_KM * (hub_cons ** (-1))
