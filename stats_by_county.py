from flask import Flask

from  webargs import fields,validate
from webargs.flaskparser import use_kwargs

from database import execute_query
from helper import format_records_dict,format_records_lst

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/stats_by_city')
@use_kwargs(
    {
    "genre":fields.Str(
        missing=None,
        validate=[validate.Length(min=1,max=30)]
        )
    },
    location='query'
)
def stats(genre):
    if genre == None:
        return 'Should have: genre'
    query = 'SELECT BillingCountry,genre,max(CNT) FROM'
    query+=' (SELECT BillingCountry,genres.Name as genre,count(genres.Name) as CNT FROM tracks JOIN invoice_items on tracks.TrackId=invoice_items.TrackId'
    query+=' JOIN genres On tracks.GenreId=genres.GenreId'
    query+=' JOIN invoices On invoices.InvoiceId=invoice_items.InvoiceId WHERE genre ="'+genre+ '" GROUP By BillingCountry)'
    records = execute_query(query)
    records = format_records_lst(records)
    if 'None' in records:
        return 'Not Found'
    return records





app.run(port=5001,debug=True)
