import csv
from geojson import Feature, FeatureCollection, Point
csv_to_convert = 'Infotag_160324.csv'
features = []
with open(csv_to_convert, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    first_row = next(reader)
    for topic, nr, category, time, room, lat, lon, title, url in reader:
        lat, lon = map(float, (lat, lon))
        features.append(
            Feature(
                id='event/'+nr,
                properties={
                    'id': "event/"+nr,
                    'number': nr,
                    'name': title,
                    'place': room,
                    'time': time,
                    'description': "",
                },
                geometry = Point((lon, lat))
            )

        )

collection = FeatureCollection(features)

with open("GeoObs.json", "w", newline='\n') as f:
    f.write('%s' % collection)