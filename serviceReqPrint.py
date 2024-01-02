from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    print("Received a request from Kong!")
    
    # Access and print request details
    print("Request Method:", request.method)
    print("Request URL:", request.url)
    print("Request Headers:", request.headers)
    print("Request Body:", request.get_data(as_text=True))
    
    return 'This is IP restriction Plugin from KONG!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
