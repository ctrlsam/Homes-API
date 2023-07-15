from typing import List


class PropertyDetails:
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data.get('id')

    @property
    def listing_type(self) -> str:
        return self._data.get('listing_type')

    @property
    def property_type(self) -> str:
        return self._data.get('property_type')

    @property
    def headline(self) -> str:
        return self._data.get('headline')

    @property
    def description(self) -> str:
        return self._data.get('description')

    @property
    def num_bathrooms(self) -> int:
        return self._data.get('num_bathrooms')

    @property
    def num_bedrooms(self) -> int:
        return self._data.get('num_bedrooms')

    @property
    def num_car_spaces(self) -> int:
        return self._data.get('num_car_spaces')

    @property
    def floor_area_m2(self) -> int:
        return self._data.get('floor_area_m2')

    @property
    def land_area_m2(self) -> int:
        return self._data.get('land_area_m2')

    @property
    def cover_image_url(self) -> str:
        return self._data.get('cover_image_url')

    @property
    def image_urls(self) -> List[str]:
        return self._data.get('image_urls', [])

    @property
    def created_at(self) -> str:
        return self._data.get('created_at')

    @property
    def updated_at(self) -> str:
        return self._data.get('updated_at')

    @property
    def display_price(self) -> str:
        return self._data.get('display_price')
