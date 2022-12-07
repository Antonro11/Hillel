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
        required=True,
        validate=[validate.Length(min=1,max=30)]
        )
    },
    location='query'
)
def stats(genre):
    query = 'SELECT * FROM'
    query+=' (SELECT BillingCity,genres.Name,count(BillingCity) as CNT FROM tracks JOIN invoice_items on tracks.TrackId=invoice_items.TrackId'
    query+=' JOIN invoices on invoice_items.InvoiceId = invoices.InvoiceId'
    query+=' JOIN genres on tracks.GenreId = genres.GenreId'
    query+=' WHERE genres.Name="'+genre+'" GROUP By BillingCity ORDER BY CNT DESC)'
    query += ' WHERE CNT = (SELECT MAX(CNT) FROM (SELECT BillingCity,genres.Name,count(BillingCity) as CNT FROM tracks JOIN invoice_items on tracks.TrackId=invoice_items.TrackId'
    query += ' JOIN invoices on invoice_items.InvoiceId = invoices.InvoiceId'
    query += ' JOIN genres on tracks.GenreId = genres.GenreId '
    query += ' WHERE genres.Name="'+genre+'" GROUP By BillingCity ORDER BY CNT DESC))'
    records = execute_query(query)
    if len(records) == 0:
        return 'Genre Not Found'
    return format_records_lst(records)





app.run(port=5001,debug=True)
