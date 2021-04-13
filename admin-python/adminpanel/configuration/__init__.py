from app import app
import urllib

# secret key for user session
app.secret_key = "ITSASECRET"

#setting up mail
app.config['MAIL_SERVER']='p3plzcpnl459194.prod.phx3.secureserver.net' #mail server
app.config['MAIL_PORT'] = 465 #mail port
app.config['MAIL_USERNAME'] = 'tech@enrichmentlasvegas.com' #emailos.environ
app.config['MAIL_PASSWORD'] = 'L@dodger4$' #password
app.config['MAIL_USE_TLS'] = True #security type
app.config['MAIL_USE_SSL'] = True #security type

#database connection parameters
connection_params = {
    'user': 'root@enrichmentlasvegas.com',
    'password': 'L@dodger4$',
    'host': 'localhost',
    'port': '3306',
    'database': 'Enrich LV',
}

