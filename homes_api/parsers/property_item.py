from typing import Optional


class PropertyItem:
    def __init__(self, data):
        self._data = data

    @property
    def item_id(self) -> str:
        return self._data.get('item_id')

    @property
    def id(self) -> str:
        return self._data.get('id')

    @property
    def state(self) -> int:
        return self._data.get('state')

    @property
    def price(self) -> Optional[int]:
        return self._data.get('price')

    @property
    def point(self) -> dict:
        return self._data.get('point')

    @property
    def url(self) -> str:
        return self._data.get('url')

    @property
    def featured_at(self) -> str:
        return self._data.get('featured_at')

    @property
    def featured_plan(self) -> int:
        return self._data.get('featured_plan')

    @property
    def display_price_short(self) -> str:
        return self._data.get('display_price_short')

    @property
    def display_street_number(self) -> str:
        return self._data.get('display_street_number')
