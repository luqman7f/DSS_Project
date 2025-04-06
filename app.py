from flask import Flask, render_template, request
from dss_utils import sign_message, verify_signature
import base64
import os

app = Flask(__name__)

MESSAGE_PATH = "messages/message.txt"
SIGNATURE_PATH = "signature.sig"

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    signature_b64 = ""
    verification_result = None

    if request.method == 'POST':
        action = request.form.get('action')

        with open(MESSAGE_PATH, 'r') as f:
            message = f.read()

        if action == 'sign':
            signature = sign_message(message)
            with open(SIGNATURE_PATH, 'wb') as f:
                f.write(signature)
            signature_b64 = base64.b64encode(signature).decode('utf-8')

        elif action == 'verify':
            if os.path.exists(SIGNATURE_PATH):
                with open(SIGNATURE_PATH, 'rb') as f:
                    signature = f.read()
                verification_result = verify_signature(message, signature)

    return render_template('index.html',
                           message=message,
                           signature_b64=signature_b64,
                           verification_result=verification_result)

if __name__ == '__main__':
    app.run(debug=True)
