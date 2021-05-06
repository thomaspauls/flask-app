import flask
import pyodbc
server = 'intel1.database.windows.net'
sdatabase = 'intel'
ddatabase = 'intel'
username = 'intel'
password = 'paat@123'
driver = '{ODBC Driver 17 for SQL Server}'

src = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + sdatabase + ';UID=' + username + ';PWD=' + password)
dest = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + ddatabase + ';UID=' + username + ';PWD=' + password)
scursor = src.cursor()
dcursor = dest.cursor()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/migrate', methods=['GET'])
def migrate():
    scursor.execute("SELECT * FROM dbo.MOCK_DAT")
    srow = scursor.fetchone()
    while srow:
        dcursor.execute("INSERT INTO dbo.Person3 (Name) Values ('" + srow[0] + "')")
        dest.commit()
        srow = scursor.fetchone()


app.run(host='0.0.0.0', port=5000)