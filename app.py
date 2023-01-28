
from flask import *

import os 


def app_v1():

	app=Flask(__name__)
	app.secret_key ="QWERTY"

	@app.route("/")
	def home():
		
		return render_template('index.html')





	return app
if __name__=="__main__":
	app=app_v1()
	app.run(debug=True, port=5000)

