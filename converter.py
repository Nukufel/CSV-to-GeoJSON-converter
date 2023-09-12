import csv
from geojson import Feature, FeatureCollection, Point

features = []
with open('theCSV.csv', newline='') as csvfile:
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
                    'category': category,
                    'time': time,
                    'description': "",
                    'url': url,
                },
                geometry = Point((lon, lat))
            )

        )

collection = FeatureCollection(features)
with open("GeoObs.json", "w", newline='\n') as f:
    f.write('%s' % collection)



"""
    {
        "type": "Feature",
      "properties": {
        "id": 24,
        "name": "NetQuest",
        "place": "Gebäude 4 Foyer",
        "category": "Spielerisch die OST erleben",
        "time": "permanent",
        "description": "",
        "url": ""
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
              8.8182305,
              47.2237293
            ]
          },



{
      "type": "Feature",
      "properties": {
        "@id": "node/8437256418",
        "door": "yes",
        "level": "2"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          8.8182305,
          47.2237293
        ]
      },
      
      
      
      
      {
      "type": "Feature",
      "properties": {
        "@id": "way/451040254",
        "alt_name": "8.061",
        "email": "rj-ilt@ost.ch",
        "indoor": "room",
        "level": "0",
        "name": "ILT Institut für Laborautomation und Mechatronik",
        "phone": "+41 58 257 47 25",
        "ref": "8.061",
        "room": "office",
        "website": "https://www.ilt.hsr.ch/"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              8.8187026,
              47.2235151
            ],
            [
              8.8186123,
              47.2234644
            ],
            [
              8.8186846,
              47.2234051
            ],
            [
              8.8187001,
              47.2233923
            ],
            [
              8.8187193,
              47.2233765
            ],
            [
              8.8187374,
              47.2233616
            ],
            [
              8.818746,
              47.2233546
            ],
            [
              8.8187628,
              47.2233407
            ],
            [
              8.8188531,
              47.2233913
            ],
            [
              8.8188467,
              47.2233966
            ],
            [
              8.8187026,
              47.2235151
            ]
          ]
        ]
      },
      "id": "way/451040254"
    },
      
      
      
      {
      "type": "Feature",
      "properties": {
        "@id": "way/903034780",
        "description": "Vorraum 4.007 Empfang Schulsekretariat",
        "indoor": "room",
        "level": "0",
        "name": "Empfang Schulsekretariat",
        "ref": "4.007",
        "room": "reception"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              8.8166712,
              47.2231671
            ],
            
            

    },
      
      """