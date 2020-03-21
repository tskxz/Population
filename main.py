# Importing pandas and bokeh
import folium
import pandas
from bokeh.plotting import figure
from bokeh.plotting import show
from bokeh.plotting import output_file


# Map
class Meterology():

    """
    The map shows the informations of the basics meteorology, if it's rainning return blue on the each country, return yellow if it's a good time!
    """

    # Constructs a base map
    def __init__(self):

        global base_map
        
        
        base_map = folium.Map(
            location = [41.1579, -8.6291],
            min_zoom = 3,
            max_zoom = 10,
            zoom_start = 10,
            tiles = 'OpenStreetMap'
        )

    def saveFile(self):
        """ Save the map file in the html file """
        
        base_map.save("meteo.html")

 
    def populationGroup(self):
        """
        Add the GeoJson layers on the map
        """
        fgP = folium.FeatureGroup(name="Population on the world")
        
        fgP.add_child(folium.GeoJson(data=open('world.json', 'r').read(),
        style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'}))
        base_map.add_child(fgP)
    
    def addControl(self):
        folium.LayerControl().add_to(base_map)
        