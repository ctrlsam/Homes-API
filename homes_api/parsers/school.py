from typing import Optional


class School:
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data.get('id')

    @property
    def school_name(self) -> str:
        return self._data.get('school_name')

    @property
    def location(self) -> dict:
        return self._data.get('location')

    @property
    def school_zone(self) -> Optional[str]:
        return self._data.get('point')

    @property
    def address(self) -> str:
        return self._data.get('address')

    @property
    def phone(self) -> str:
        return self._data.get('phone')

    @property
    def website(self) -> str:
        return self._data.get('website')

    @property
    def gender(self) -> str:
        return self._data.get('gender')

    @property
    def type(self) -> str:
        return self._data.get('type')

    @property
    def definition(self) -> str:
        return self._data.get('definition')

    @property
    def authority(self) -> str:
        return self._data.get('authority')

    @property
    def roll(self) -> int:
        return self._data.get('roll')

    @property
    def decile(self) -> int:
        return self._data.get('decile')

    @property
    def in_zone(self) -> bool:
        return self._data.get('in_zone')

    @property
    def zoned_school(self) -> bool:
        return self._data.get('zoned_school')

    @property
    def distance(self) -> float:
        return self._data.get('distance')
