from homes_api.sdk import HomeSDK
from homes_api.geosearch import GeoSearch
from shapely.geometry import Polygon

sdk = HomeSDK()
searcher = GeoSearch(sdk)

wellington_city = Polygon([
    (-41.29136, 174.76341),
    (-41.29381, 174.79826),
    (-41.31625, 174.79911),
    (-41.31522, 174.76066)
])

# Query with a large area
# Large areas will be broken down into multiple
# areas to query the API to avoid reaching the
# maximum properties returnable.
results = searcher.search(wellington_city)

# Or manually with a small area
results = sdk.get_properties_within_area(
    polylines=['jda{Fwi{i`@gBdkAbaApGs@sqA??']
)

# Display first 5 results
for prop in results[:5]:
    print(f'\n{prop.id}\nhttps://homes.co.nz/address{prop.url}')
    details = sdk.get_property_details(prop.id)
    print(f'Floor area: {details.floor_area_m2}m^2')
    print(f'Land Area: {details.land_area_m2}m^2')
