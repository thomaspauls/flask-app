import flask
import pyodbc
import ran
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
    return "<h1>Welcome to Intellipaat Demo</h1><p>This site is a prototype API for moving data between sources. Use /migrate to start the job.</p>"


@app.route('/migrate', methods=['GET'])
def migrate():
    scursor.execute("SELECT * FROM dbo.MOCK_DATA")
    srow = scursor.fetchone()

    while srow:
        predict = ran.predict()
        dcursor.execute("INSERT INTO dbo.Person5 (Age, Income, No_of_Logins, predict) Values ('" + str(srow[0]) + "', '" + str(srow[1]) + "', '" + str(srow[2]) + "', '" + str(predict) + "')")
        dest.commit()
        srow = scursor.fetchone()
    return "<h1>Migration Done</h1>"


app.run(host='0.0.0.0', port=5000)
