from typing import List
import polyline
import numpy as np
from shapely.geometry import Polygon, box

from .parsers.property_item import PropertyItem
from .sdk import HomeSDK


class GeoSearch:

    def __init__(self, sdk: HomeSDK) -> None:
        self.sdk = sdk

    def search(self, area: Polygon, square_size_km=1) -> List[PropertyItem]:
        """Perform a property search for a large area.
        The area gets split into small "squares" so the HomesAPI can return
        all the houses.

        Args:
            area (Polygon): area to scan
            square_size_km (int, optional): size of each tile. Defaults to 1.

        Returns:
            List[PropertyItem]: list of found properties within the area
        """
        grid = GeoSearch.create_grid(area, square_size_km)

        properties = []

        for square in grid:
            encoded_square = GeoSearch.polygon_to_encoded_polyline(square)
            query_response = self.sdk.get_properties_within_area([encoded_square])

            if len(query_response):
                # print(f'Found {len(properties)} properties in {encoded_square}')
                properties += query_response

        return properties

    @staticmethod
    def create_grid(area: Polygon, square_size_km: float) -> List[Polygon]:
        """Create a grid of squares of size 'step' inside a bounding box.

        Args:
            area (Polygon): Large area to split into a smaller grid of polygons
            square_size_km (float): km of grid squares

        Returns:
            List[Polygon]: List of Polygon objects each representing a grid cell
        """
        # Conversion factors
        km_per_degree_latitude = 110.574

        # Approximate conversion from km to degrees
        square_size_deg = square_size_km / km_per_degree_latitude
        minx, miny, maxx, maxy = area.bounds
        x_coords = np.arange(minx, maxx, square_size_deg)
        y_coords = np.arange(miny, maxy, square_size_deg)

        grid = []
        for x in x_coords:
            for y in y_coords:
                square = box(x, y, x + square_size_deg, y + square_size_deg)
                if area.intersects(square):
                    grid.append(square.intersection(area))

        return grid

    @staticmethod
    def polygon_to_encoded_polyline(polygon: Polygon) -> str:
        """Convert a polygon to a encoded polyline
        https://developers.google.com/maps/documentation/utilities/polylineutility

        Args:
            polygon (Polygon): Area to convert

        Returns:
            str: encoded polyline
        """
        points = list(polygon.exterior.coords)

        # Convert each point to lat/lon
        latlon_points = [(point[1], point[0]) for point in points]

        return polyline.encode(latlon_points)
