"""
"""
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home():
    """
    Used for domain verification only. Not used in Production ENV.
    """
    return """
        <html>
        <head>
        <title>Your Page Title</title>
        <meta name="google-site-verification" content="<VALUE>" />
        </head>
        </html>
          """


@app.route('/notifications/', methods=["POST"])
def attender():
    """
    :return:
    """
    headers = list(request.headers.items())
    print ("--------------------------------------", headers)
    print ("--------------------body-----------------:", request.data.decode())
    return make_response(jsonify({"status": "success"}), 200)


if __name__ == '__main__':
    app.run()


