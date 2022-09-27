from flask import Flask, render_template

app = Flask(__name__)

#@app.route('/')
#def tablero():
#	return render_template('index.html')

@app.route('/', defaults={'numero1': 8, 'numero2': 8, 'color1': '#000000', 'color2': '#f00'})
@app.route('/<int:numero1>', defaults={'numero2': 8, 'color1': '#000000', 'color2': '#f00'})
@app.route('/<int:numero1>/<int:numero2>', defaults={'color1': '#000000', 'color2': '#f00'})
@app.route('/<int:numero1>/<int:numero2>/<color1>', defaults={'color2': '#f00'})
@app.route('/<int:numero1>/<int:numero2>/<color1>/<color2>')
def plantilla(numero1, numero2, color1, color2):
	return render_template("index.html", num1=numero1, num2=numero2, color1=color1, color2=color2)

if __name__=="__main__":
	app.run(debug=True)