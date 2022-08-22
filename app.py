from flask import Flask, request, jsonify
from dbhandler import deleteData, getData, getAllData, insertData, getDatabyID, updateData
import jwt
from getenv import getKEY
SECRET_KEY = getKEY()
ACCOUNT_COLLECTION = "accounts"
TEMPLATE_COLLECTION = "templates"

app = Flask(__name__)

# Handle user register process
@app.route("/", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
def register():
    """
        This function is used to handle register end point

    """
    content_type = request.headers.get('Content-Type')
    # checking content type
    if (content_type == 'application/json'):
        jsonData = request.json
        try:
            # inserting data to db
            insertData(ACCOUNT_COLLECTION,jsonData)
        except:
            return "Unable to register user."
        return "User Registered!"
    return "Bad request"

# Handle login process
@app.route("/login", methods=['GET', 'POST'])
def login():
    """
        This function is used to handle login endpoint
        also generate jwt token.
    """
    content_type = request.headers.get('Content-Type')
    # checking content type of request
    if (content_type == 'application/json'):
        jsonData = request.json
        try:
            # user authentication
            getData(ACCOUNT_COLLECTION,jsonData)
            # generating token
            token = jwt.encode(
                payload=jsonData,
                key=SECRET_KEY
            )
        except:
            return "Unable to Login."
        return f"User Logged In!\nToken: {token}"
    return "Bad request"

# manage template endpoint
@app.route("/template", methods=['GET', 'POST'])
def manageTemplate():
    """
        This method is used to handle GET and POST requests
        at template endpoint.
        Used for inserting and getting all record.
    """
    content_type = request.headers.get('Content-Type')
    # if request method is POST
    # for inserting record
    if request.method == 'POST':
        if (content_type == 'application/json'):
            jsonData = request.json
            try:
                # inserting data
                insertData(TEMPLATE_COLLECTION,jsonData)
            except:
                return "Not Successfull"
            return "Inserted Successfully";
        return "Failed"
    # if request method is GET
    # used for getting all record
    elif request.method == 'GET':
        if (content_type == 'application/json'):
            try:
                # getting all data
                result = getAllData(TEMPLATE_COLLECTION)
            except:
                return "Not Successfull"
            return f"Get All Data Successfully\n {result}"
        return "Failed"
    # default case
    else:
        return "Bad request"

# manage template endpiont with id
@app.route("/template/<id>", methods=['GET', 'POST', 'PUT', 'DEL'])
def templates(id):
    """
        This function handle GET PUT and DEL methods.
        Used to update, get record by id, and del record.
        param: id
    """
    content_type = request.headers.get('Content-Type')
    # if request method is GET
    if request.method == 'GET':
        try:
            # getting data by id
            result = getDatabyID(TEMPLATE_COLLECTION,id)
        except:
            return "No Match"
        return f"Matched Record\n {result}"
    # if request method is DEL
    elif request.method == 'DEL':
        if (content_type == 'application/json'):
            jsonData = request.json
            try:
                # deleting data
                deleteData(TEMPLATE_COLLECTION,jsonData)
            except:
                return "Not Successfull"
            return "Get All Data Successfully";
        return "Faild"
    # if request method is PUT
    elif request.method == 'PUT':
        if (content_type == 'application/json'): 
            jsonData = request.json
            try:
                # updating data
                updateData(TEMPLATE_COLLECTION,jsonData,id)
            except:
                return "Not Successfull"
            return "Updated Successfully";
        return "Failed"
    # default case
    else:
        return "Bad request"


if __name__ == "__main__":
    app.run(debug=True)