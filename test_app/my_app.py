from flask import Flask 
from datetime import datetime


app = Flask('__main__')

@app.route('/')
def index():
    content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Test App</title>
        </head>
        <body>
            <h1>
                Time Now : {str(datetime.now())}
            </h1>
        </body>
        </html>    
    """
    return content

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)