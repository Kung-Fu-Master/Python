import json
import os
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

#load data into a list
filename = os.getcwd()+os.sep+"weather_worldMap_16"+os.sep+"population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

#print the population of each country in 2010
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        #print(country_name +": " + str(population))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print("Error - " + country_name)

cc_pop_1, cc_pop_2, cc_pop_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

#add specific color to the map
#wm_style = RotateStyle("#336699", base_style=LightColorizedStyle)
#wm_style = RotateStyle()
#wm = pygal_maps_world.maps.World(style=wm_style)

wm = pygal_maps_world.maps.World()
wm.title = "World Pupulation in 2010, by Country."
wm.add("0~10m", cc_pop_1)
wm.add("10m~1bn", cc_pop_2)
wm.add(">1bm", cc_pop_3)

wm.render_to_file("weather_worldMap_16/world_population.svg")