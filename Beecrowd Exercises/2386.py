# -*- coding: utf-8 -*-

telescope_opening = int(input())
number_stars = int(input())
human_max_photons = 40000000
visible_stars = 0

for x in range(number_stars):
    stars_photons = int(input())
    if (stars_photons * telescope_opening >= human_max_photons):
        visible_stars +=1

print(visible_stars)