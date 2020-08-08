from abc import ABC, abstractmethod
from datetime import datetime

class AbstractCruiseDataProvider(ABC):

    @abstractmethod
    def get_take_off_date(self) -> datetime:
        '''
        Date (and time) of take off from Earth.
        '''
        pass

    @abstractmethod
    def get_distance_travelled(self) -> int:
        '''
        Distance travelled so far from Earth in km.
        '''
        pass

    @abstractmethod
    def get_destination(self) -> str:
        '''
        Where is the craft headed ?
        '''
        pass

    @abstractmethod
    def get_distance_remaining(self) -> int:
        '''
        Get distance (in km) remaining to the destination
        '''
        pass

    @abstractmethod
    def get_current_speed(self) -> int:
        ''' 
        Get speed relative to the sum in km
        '''
        pass

    @abstractmethod
    def get_landing_date(self) -> datetime:
        '''
        Expected date (and time) of arrival at destination in utc
        '''
        pass
