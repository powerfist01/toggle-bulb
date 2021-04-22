from flask import Flask, request, render_template

app = Flask(__name__)

def get_next_state(current_state):
    '''Toggle state'''
    if(current_state == 'on'):
        return 'off'
    else:
        return 'on'

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/toggle", methods=["POST"])
def toggle_switch():
    
    print(request.json)
    current_state = request.json['current_state']
    next_state = get_next_state(current_state)
    print(current_state)
    return {
        'next_state': next_state
    }

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)