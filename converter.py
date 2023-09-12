import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('theCSV.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    first_row = next(reader)
    for Thema, Nr, Kategorie, Zeitbereich, Zeitbemerkung, Raum, lat, lon, Title in reader:
        lat, lon = map(float, (lat, lon))
        features.append(
            Feature(
                properties={
                    'name': 'Nr: ' + Nr + '\n' + Title,
                    'alt_name': Nr,
                    'room': Kategorie,
                    'ref': Raum,
                    'description': Zeitbemerkung,
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
            "@id": "nood/1",
            "indoor": "room",
            "ref": "1.269/1.271",
            "name": "Nr: 1 \n Einführung in die Künstliche Intelligenz."
            "alt_name": "1"
            "room": "Showvorlesung"
            "description": "10.30 –11.30\n14.30 –15.30"
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