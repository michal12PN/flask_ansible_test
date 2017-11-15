from chalice import Chalice
import psycopg2

app = Chalice(app_name='final_good')


@app.route('/')
def index():
    con=psycopg2.connect(dbname= 'main', host='0.0.0.0', 
    port= '5431', user= 'user', password= 'pass', connect_timeout=60)

    print('doszedlem tutaj')
    cur=con.cursor()

    cur.execute("SELECT count(*) FROM hydra.ios")
    dane = cur.fetchall()    
    return dane

    cur.close()
    con.close()
