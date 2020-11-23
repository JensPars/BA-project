
from geopy.geocoders import Nominatim
geolocator = Nominatim()
lon = []
lat = []
for i,j in zip(df['City'],df['Country']):
  try:
    loc = geolocator.geocode(i + ', ' + j)[-1]
    lon.append(loc[0])
    lat.append(loc[1])
  except:
    lon.append(0)
    lat.append(0)
df['lat'] = lat
df['lon'] = lon
import plotly.express as px
fig = px.scatter_geo(df[df['lat']!=0], lon='lat',lat='lon', color = 'Continent',
                     hover_name="City", size="CO2 Emissions per Capita (metric tonnes)",
                     projection="natural earth")
fig.show()
