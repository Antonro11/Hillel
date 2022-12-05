from flask import Flask

from  webargs import fields,validate
from webargs.flaskparser import use_kwargs

from database import execute_query
from helper import format_records_dict,format_records_lst

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/order-price')
@use_kwargs(
    {
    "city": fields.Str(
        missing=None,
        validate=validate.Length(min=1,max=20)
        )
    },
    location='query'
)
def get_customers(city):
    query = 'SELECT BillingCity,count(*)*(Quantity*UnitPrice) FROM invoices JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId '
    if city != None:
        query += ' WHERE BillingCity="' + city + '" GROUP BY BillingCity'
    else:
        query += ' GROUP BY BillingCity'
    records = execute_query(query)
    if len(records)==0:
        return 'City is not found'
    return format_records_lst(records)


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
    query = 'SELECT DISTINCT tracks.Name,albums.Title,artists.Name as Artist,genres.Name as Genre,Milliseconds as TimeMillis,Bytes as MemoryUsed,UnitPrice as Price,media_types.Name as MediaType,playlists.Name as Playlist FROM tracks '
    query+=' JOIN media_types ON  tracks.MediaTypeId = media_types.MediaTypeId'
    query+=' JOIN albums ON tracks.AlbumId = albums.AlbumId'
    query+=' JOIN artists ON albums.ArtistId = artists.ArtistId'
    query+=' JOIN genres ON tracks.GenreId = genres.GenreId'
    query+=' JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId'
    query+=' JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId'
    if track_id != None:
        query+=' WHERE tracks.TrackId='+str(track_id)
    records = execute_query(query)
    if len(records)==0:
        return 'No such TrackID'
    return format_records_lst(records)

@app.route('/tracks-len')
def tracks_len():
    query = 'SELECT sum(Milliseconds) FROM tracks'
    records = execute_query(query)
    return str(round(records[0][0]/3600000,2)) +' Hours'



app.run(port=5001,debug=True)
