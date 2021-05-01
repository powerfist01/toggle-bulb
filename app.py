from flask import Flask, request, render_template
from flask_basicauth import BasicAuth
from flask_cors import CORS

app = Flask(__name__)

CORS(app) # This will enable CORS for all routes

app.config['BASIC_AUTH_USERNAME'] = 'sujeet'
app.config['BASIC_AUTH_PASSWORD'] = 'helloworld'

basic_auth = BasicAuth(app)

def get_next_state(current_state):
    '''Toggle state'''
    if(current_state == 'on'):
        return 'off'
    else:
        return 'on'

@app.route("/")
@basic_auth.required
def main():
    return render_template('index.html')

@app.route("/tree")
@basic_auth.required
def chart():
    return render_template('d3chart.html')

@app.route("/circle")
@basic_auth.required
def circle():
    return render_template('d3circle.html')

@app.route("/toggle", methods=["POST"])
@basic_auth.required
def toggle_switch():
    
    current_state = request.json['current_state']
    next_state = get_next_state(current_state)
    return {
        'next_state': next_state
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
