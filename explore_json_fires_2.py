import json 

in_file = open('US_fires_9_1.json','r')

out_file = open('readable_fi_data.json', 'w')

us_fires1 = json.load(in_file)

json.dump(us_fires1,out_file,indent=4)


brights,lons,lats = [],[],[]

for fr in us_fires1: 
    if fr["brightness"] > 450: 
        bright = fr["brightness"]
        lon = fr["longitude"]
        lat = fr["latitude"]    
        brights.append(bright)
        lons.append(lon)
        lats.append(lat) 

print("Brights")
print(brights[:10])

print("Lons")
print(lons[:10])

print("Lats")
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons, 
    'lat':lats,
    'marker': { 
        'size':[5*bright for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True, 
        'colorbar':{'title':'Brightness'}

    },
}]

my_layout = Layout(title = 'US Fires - 9/1/2020 through 9/13/2020')


fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='US_Fire.html')



