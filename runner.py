import sys
import termtables as tt
import cruisefactory

if __name__ == '__main__':
    craftid = input('Enter space craft name : ')
    provider = cruisefactory.get_cruise_data_provider(craftid)
    if not provider:
        print('We\'re sorry ! We do not have information about that space craft yet.')
        sys.exit(1)
    data = [ 
        [craftid, provider.get_destination(), provider.get_distance_travelled(), provider.get_distance_travelled(), provider.get_current_speed()]
    ]
    tt.print(data, header=['Spacecraft', 'Destination', 'Distance travelled (km)', 'Distance remaining (km)', 'Speed relative to sum (km/h)'], style=tt.styles.ascii_thin, padding=(0, 1))
