import csv
from geojson import Feature, FeatureCollection, Point
csv_to_convert = 'Vorlage.csv'
features = []
with open(csv_to_convert, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    first_row = next(reader)
    for topic, nr, time, room, lat, lon, title, description, url in reader:
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
                    'category': topic,
                    'description': description,
                },
                geometry = Point((lon, lat))
            )

        )

collection = FeatureCollection(features)

with open("event.geojson", "w", newline='\n') as f:
    f.write('%s' % collection)