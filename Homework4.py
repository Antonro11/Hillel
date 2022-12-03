from flask import Flask

from  webargs import fields,validate
from webargs.flaskparser import use_kwargs

from database import execute_query
from helper import format_records_dict,format_records_lst

app = Flask(__name__)



@app.route('/order-price')
@use_kwargs(
    {
    "country": fields.Str(
        missing=None,
        validate=validate.Length(min=1,max=20)
        )
    },
    location='query'
)
def get_customers(country):
    query = 'SELECT * FROM (SELECT * FROM invoices JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId) '
    records = execute_query(query)
    dict_quantity = dict()

    for i in records:
        if i[6] not in dict_quantity:
            dict_quantity[i[6]]= i[-1]*i[-2]
        else:
            dict_quantity[i[6]] += i[-1]*i[-2]
    for i, y in dict_quantity.items():
        if country != None and country not in dict_quantity.keys():
            return 'Country not found'
        elif i == country:
            return str(i)+ ' ' + str(round(y,2))
        dict_quantity.update({i:round(y,2)})
    return format_records_dict(dict_quantity)


@app.route('/tracks-info')
@use_kwargs(
    {
    "track_id":fields.Int(
        missing=None,
        validate=[validate.Range(min=1,max=5000)]
    )
    },
    location='query'
)
def get_all_info_about_tracks(track_id):
    query = 'SELECT tracks.TrackId,tracks.Name,title,artists.Name,genres.Name,Milliseconds,Bytes,UnitPrice,media_types.Name FROM tracks JOIN media_types ON  tracks.MediaTypeId = media_types.MediaTypeId'
    query+=' JOIN albums ON tracks.AlbumId = albums.AlbumId'
    query+=' JOIN artists ON albums.ArtistId = artists.ArtistId'
    query+=' JOIN genres ON tracks.GenreId = genres.GenreId'
    records = execute_query(query)
    if track_id == None:
        return format_records_lst(records)
    for item in records:
        if item[0] == track_id:
            return str(item)
    return 'Not found'

@app.route('/tracks-len')
def tracks_len():
    query = 'SELECT * FROM tracks'
    records = execute_query(query)
    tracks_len_millis = 0
    for item in records:
        tracks_len_millis += item[6]
    return str(round(tracks_len_millis/3600000,2)) + ' Hours'


app.run(port=5001,debug=True)
