import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#条形图上方添加标注 add a label above the bar chart
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2.,
                 1.02*height,
                 "{:,}".format(float(height)),
                 ha = "center",
                 va = "bottom",
                 fontsize = 8)

top10_arrivals_countries = ['CANADA','MEXICO','UNITED\nKINGDOM',\
                            'JAPAN','CHINA','GERMANY','SOUTH\nKOREA',\
                            'FRANCE','BRAZIL','AUSTRALIA']
top10_arrivals_values = [16.625687, 15.378026, 3.934508, 2.999718,\
                         2.618737, 1.769498, 1.628563, 1.419409,\
                         1.393710, 1.136974]
arrivals_countries = ['WESTERN\nEUROPE','ASIA','SOUTH\nAMERICA',\
                      'OCEANIA','CARIBBEAN','MIDDLE\nEAST',\
                      'CENTRAL\nAMERICA','EASTERN\nEUROPE','AFRICA']
arrivals_percent = [36.9,30.4,13.8,4.4,4.0,3.6,2.9,2.6,1.5]

fig, ax1 = plt.subplots(figsize=(8,4))
rects = ax1.bar(range(10), top10_arrivals_values, color="blue")
## add x-ticks to ax1
plt.xticks(range(10), top10_arrivals_countries, fontsize=10)

## ax2 insert into ax1 chart
ax2 = inset_axes(ax1, width=2.5, height=4, loc=4)
explode = (0.08, 0.08, 0.05, 0.05,0.05,0.05,0.05,0.05,0.05)
patches, texts, autotexts = ax2.pie(arrivals_percent, labels=arrivals_countries, autopct="%1.1f%%", explode=explode)

# change the size of ax2 font
for text in texts+autotexts:
    text.set_fontsize(6)

#将x轴y轴设置成不可见 set x-axis y-axis to invisible
for spine in ax1.spines.values():
    spine.set_visible(False)

autolabel(rects)

plt.show()





########################### matplotlib自带了一些图形可供使用comes with some graphics available

import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

patches = []

# Full and ring sectors drawn by Wedge((x,y),r,deg1,deg2)
leftstripe = Wedge((.46, .5), .15, 90,100)           # Full sector by default
midstripe = Wedge((.5,.5), .15, 85,95)                      
rightstripe = Wedge((.54,.5), .15, 80,90)
lefteye = Wedge((.36, .46), .06, 0, 360, width=0.03)  # Ring sector drawn when width <1
righteye = Wedge((.63, .46), .06, 0, 360, width=0.03)
nose = Wedge((.5, .32), .08, 75,105, width=0.03)
mouthleft = Wedge((.44, .4), .08, 240,320, width=0.01)
mouthright = Wedge((.56, .4), .08, 220,300, width=0.01)
patches += [leftstripe,midstripe,rightstripe,lefteye,righteye,nose,mouthleft,mouthright]

# Circles
leftiris = Circle((.36,.46),0.04)
rightiris = Circle((.63,.46),0.04)
patches += [leftiris,rightiris]

# Polygons drawn by passing coordinates of vertices
leftear = Polygon([[.2,.6],[.3,.8],[.4,.64]], True)
rightear = Polygon([[.6,.64],[.7,.8],[.8,.6]], True)
topleftwhisker = Polygon([[.01,.4],[.18,.38],[.17,.42]], True)
bottomleftwhisker = Polygon([[.01,.3],[.18,.32],[.2,.28]], True)
toprightwhisker = Polygon([[.99,.41],[.82,.39],[.82,.43]], True)
bottomrightwhisker = Polygon([[.99,.31],[.82,.33],[.81,.29]], True)
patches+=[leftear,rightear,topleftwhisker,bottomleftwhisker,toprightwhisker,bottomrightwhisker]

# Ellipse drawn by Ellipse((x,y),width,height)
body = Ellipse((0.5,-0.18),0.6,0.8)
patches.append(body)

# Draw the patches
colors = 100*np.random.rand(len(patches)) # set random colors
p = PatchCollection(patches, alpha=0.4)
p.set_array(np.array(colors))
ax.add_collection(p)

# Show the figure
plt.show()










