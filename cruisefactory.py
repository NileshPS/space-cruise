import cruisebase
import mars2020

__KNOWN_CRUISES = { 'mars2020' : mars2020.CruiseDataProvider }

def get_cruise_data_provider(id: str, *args, **kwargs) -> cruisebase.AbstractCruiseDataProvider:
	clss = __KNOWN_CRUISES.get(id.lower(), None)
	return clss(*args, **kwargs) if clss else None
