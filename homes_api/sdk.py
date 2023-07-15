import requests
from typing import List

from .parsers import School, PropertyItem, PropertyDetails


class HomeSDK:
    """Provide functionality to interact with the Home.co.nz API"""

    def __init__(self, request_timeout=1000) -> None:
        self.timeout = request_timeout

    def get_property_details(self, property_id: str) -> PropertyDetails:
        """Get details about a property

        Args:
            property_id (str): Properties UUID

        Returns:
            PropertyDetails: details about a property
        """
        url = f'https://api-gateway.homes.co.nz/listing/{property_id}/detail'
        res = self._send_request('GET', url)

        return PropertyDetails(res.json()['listing'])

    def get_properties_within_area(
            self,
            polylines: List[str],
            display_rentals=True,
            for_rent=True,
            for_sale=True,
            just_sold=True,
            off_market=True,
            limit=1500
        ) -> List[PropertyItem]:
        """Get properties within lat-long polyline area

        Args:
            display_rentals (bool): get rental properties
            for_rent (bool): get properties for rent
            for_sale (bool): get properties for sale
            just_sold (bool): get properties that have recently sold
            limit (int): query response limit
            off_market (bool): get properties that are off the market
            polylines (List[str]): area to search properties for

        Returns:
            List[PropertyItem]: Property items within this area
        """
        url = 'https://gateway.homes.co.nz/map/dots'
        payload = {
            "display_rentals": display_rentals,
            "for_rent": for_rent,
            "for_sale": for_sale,
            "just_sold": just_sold,
            "limit": limit,
            "off_market": off_market,
            "polylines": polylines
        }

        res = self._send_request('POST', url, json=payload)
        return  [PropertyItem(location) for location in res.json()['map_items']]

    def get_schools_by_pos(self, lat: float, lon: float) -> List[School]:
        """Get the schools that are located close to a lat-lon position

        Args:
            lat (float): geo latitude position
            lon (float): geo longitude position

        Returns:
            List[School]: List of schools for that location
        """
        url = f'https://gateway.homes.co.nz/schools?lat={lat}&lon={lon}'
        res = self._send_request('GET', url)

        return [School(school) for school in res.json()['schools']]

    def _send_request(self, method: str, url: str, **args) -> requests.Response:
        """Send HTTP request to API

        Args:
            method (str): HTTP method
            url (str): URL to query

        Returns:
            requests.Response: server's response
        """
        return requests.request(method, url, timeout=self.timeout, **args)
