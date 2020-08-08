import requests
from datetime import datetime, timezone
import cruisebase


class CruiseDataProvider(cruisebase.AbstractCruiseDataProvider):
    '''
    Retrieves information about mars2020 spacecraft from official Nasa website.
    Refer https://mars.nasa.gov/js/countUp/cruisedata.js for impelementation details.
    '''

    TAKEOFF_DATETIME_RAW = '30 July 2020 11:50:00 -0000'
    LANDING_DATETIME_RAW = '18 February 2021 19:36:00 -0000'
    TAKEOFF_DATETIME = datetime.strptime(TAKEOFF_DATETIME_RAW, '%d %B %Y %H:%M:%S %z')
    LANDING_DATETIME = datetime.strptime(LANDING_DATETIME_RAW, '%d %B %Y %H:%M:%S %z')
    RSS_URL = 'https://mars.nasa.gov/rss/api/?feed=cruise&category=mars2020&feedtype=json'

    def __init__(self):
        self.data = None
        self.loadData()

    def loadData(self):
        resp = requests.get(CruiseDataProvider.RSS_URL + '&' + str(datetime.now(timezone.utc).hour))
        self.data = resp.json()

    def get_take_off_date(self) -> datetime:
        return CruiseDataProvider.TAKEOFF_DATETIME

    def get_distance_travelled(self) -> int:
        sp1 = self.data["spacecraftdata"][0]
        sp2 = self.data["spacecraftdata"][1]
        distance_start, distance_end = int(sp1["TRAVELFROM"]), int(sp2["TRAVELFROM"])
        diff = int(distance_end - distance_start)
        km_per_second = diff / 3600
        now = datetime.now()
        seconds_now = now.minute * 60 + now.second
        distance_travelled = distance_start +  seconds_now * km_per_second
        return distance_travelled

    def get_destination(self) -> str:
        return 'Mars'
    
    def get_distance_remaining(self) -> int:
        sp1 = self.data["spacecraftdata"][0]
        sp2 = self.data["spacecraftdata"][1]
        distance_start, distance_end = int(sp1["TRAVELTO"]), int(sp2["TRAVELTO"])
        diff = int(distance_end - distance_start)
        km_per_second = diff / 3600
        now = datetime.now()
        seconds_now = now.minute * 60 + now.second
        distance_to_go = distance_start +  seconds_now * km_per_second
        return distance_to_go

    def get_current_speed(self):
        sp1=self.data['spacecraftdata'][0]
        return int(sp1['RELSPEEDSUN'])

    def get_landing_date(self):
        return CruiseDataProvider.LANDING_DATETIME
        