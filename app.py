from flask import Flask
import db_connection

app = Flask(__name__)


# check how to turn on debug mode
@app.route("/")
def home_page():
    json = {'name': 'Oz'}
    coll = db_connection.getDbConnection('test', 'test')
    return db_connection.findDocument(coll, json)['name']

    # online_users = mongo.db.users.find({"online": True})
    # return render_template("index.html",
    #     online_users=online_users)

@app.route("/oz")
def email_request():
    return 'fuck you !!!'

# def main():
#     print('hi there!')


# if __name__ == "__main__":
#     # execute only if run as a script
#     main()