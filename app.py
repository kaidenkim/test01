"""
A sample Hello World server.
"""
import os
import requests

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!!!!!!!!!!!! v10"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

@app.route('/serverless')
def serverless():
    # Get environment variables, BACKEND_URL
    backend_url = os.environ.get('BACKEND_URL', 'Unknown URL')

    # Call a REST API
    response1 = requests.get("{}/backend1".format(backend_url))
    message1 = response1.text

    response2 = requests.get("{}/backend2".format(backend_url))
    message2 = response2.text

    """Return a friendly HTTP greeting."""
    message = "Serverless VPC Connector Test: URL={}\nBACKEND1={}\nBACKEND2={}".format(backend_url, message1, message2)

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('serverless.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
