from abc import ABC, abstractmethod


class IMapBluePrint(ABC):

    @abstractmethod
    def first_floor_url(self):
        pass

    @abstractmethod
    def second_floor_url(self):
        pass

    @abstractmethod
    def y_delta(self):
        pass

    @abstractmethod
    def first_floor_seal_locations(self):
        pass

    def second_floor_seal_locations(self):
        pass
