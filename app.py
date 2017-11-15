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
# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
