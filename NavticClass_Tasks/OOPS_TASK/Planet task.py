
# class planet:
#         def __init__(self, planet, star):
#             self.planet =planet
#             self.star = star
#
#         def __str__(self):
#             return self.planet + ' in ' + self.star
#
#     sun = planet("earth orbit", "Milky Way")
#     print(sun)


class Star:
    def __init__(self, planet, sun):
        self.planet = planet
        self.sun = sun
    def __str__(self):
        return self.planet + ' orbits Sun in ' + self.sun

sun = Star("Earth", "Milky Way")
print(sun)






