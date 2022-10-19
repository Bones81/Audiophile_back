####### THE FOLLOWING FILE WAS USED TO IMPORT DATA FROM PREVIOUS HEROKU-HOSTED POSTGRES DB TO A NEW ELEPHANTSQL-HOSTED DB

# import psycopg2
# import urllib.request, json

# albums_url = "https://young-savannah-30515.herokuapp.com/api/albums"
# with urllib.request.urlopen(albums_url) as request:
#     response = request.read()
#     record_list = json.loads(response) # full list of album data to export into new db
#     # print(record_list[0]) # test line to see one data object


#     for record in record_list:
#         conn = psycopg2.connect("dbname='bsykvpdh' user='bsykvpdh' host='batyr.db.elephantsql.com' password='OO00M3ydrD1pgUOQmWhvua7vI0Fh58wH'")
#         cur = conn.cursor()

#         id = record['id']
#         name = record['name']
#         year = record['year']
#         image = record['image']

#         sql = '''INSERT INTO albums_api_album(id, name, year, image) VALUES(%s, %s, %s, %s) RETURNING id'''
#         cur.execute(sql, (id, name, year, image))

#         # get the generated id back
#         album_id = cur.fetchone()[0]
#         print(album_id)

#         ### USE THE FOLLOWING TO CLEAR TABLE -- CAUTION
#         # sql = '''DELETE FROM albums_api_album'''
#         # cur.execute(sql)
#         ###############################################

#         conn.commit()

#         conn.close()


# artists_url = "https://young-savannah-30515.herokuapp.com/api/artists"
# with urllib.request.urlopen(artists_url) as request:
#     response = request.read()
#     record_list = json.loads(response) # full list of artist data to export into new db
#     # print(record_list[0]) # test line to see one data object


#     for record in record_list:
#         conn = psycopg2.connect("dbname='bsykvpdh' user='bsykvpdh' host='batyr.db.elephantsql.com' password='OO00M3ydrD1pgUOQmWhvua7vI0Fh58wH'")
#         cur = conn.cursor()

#         id = record['id']
#         name = record['name']
#         genre = record['genre']
#         image = record['image']

#         sql = '''INSERT INTO artists_api_artist(id, name, genre, image) VALUES(%s, %s, %s, %s) RETURNING id'''
#         cur.execute(sql, (id, name, genre, image))

#         # get the generated id back
#         artist_id = cur.fetchone()[0]
#         print(artist_id)

#         ### USE THE FOLLOWING TO CLEAR TABLE -- CAUTION
#         # sql = '''DELETE FROM artists_api_artist'''
#         # cur.execute(sql)
#         ###############################################

#         conn.commit()

#         conn.close()
