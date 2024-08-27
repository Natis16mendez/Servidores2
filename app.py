from flask import Flask, url_for, render_template

servidores2 = Flask(__name__)

@servidores2.route('/inicio')
def home():
    return render_template('plantilla.html')

if __name__ =='__main__':
    servidores2.run(debug=True) 