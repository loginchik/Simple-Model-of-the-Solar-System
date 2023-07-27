# The Earth's velocity
earth_s = 0.05

def rel_speed(days: int, earth_speed: float = earth_s) -> float:
    """Calculates the velocity of planet relative to the velocity of the Earth.
    The Earth's cycle is taken as 365 days per 1 round.

    Args:
        days (int): the number of earth days during which the planet 
        makes one revolution around the sun
        
        earth_speed (float): the Earth's velocity. Defaults to 0.05.

    Returns:
        float: the calculated velocity
    """
    
    return float(str(365 / days * earth_speed))


# The velocity of the planets relative to the velocity of the Earth
mercury_s = rel_speed(88)
venus_s = rel_speed(255)
mars_s = rel_speed(687)
jupiter_s = rel_speed(4332)
saturn_s = rel_speed(10759)
uran_s = rel_speed(30688)
neptun_s = rel_speed(60182)
