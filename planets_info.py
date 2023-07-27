# Earth velocity
earth_s = 0.05


def rel_speed(days):
    return float(str(365 / days * earth_s))


# The velocity of the planets relative to the velocity of the Earth
mercury_s = rel_speed(88)
venus_s = rel_speed(255)
mars_s = rel_speed(687)
jupiter_s = rel_speed(4332)
saturn_s = rel_speed(10759)
uran_s = rel_speed(30688)
neptun_s = rel_speed(60182)
