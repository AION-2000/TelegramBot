from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/capture', methods=['GET'])
def capture():
    return render_template('capture.html')

@app.route('/submit', methods=['POST'])
def submit():
    image = request.files['image']
    location = request.form['location']
    image.save(os.path.join('uploads', image.filename))
    with open('locations.txt', 'a') as f:
        f.write(f"{location}\n")
    return 'Success'

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(port=5000, debug=True)
