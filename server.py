from flask import Flask

app= Flask(__name__)

@app.route('/',methods=["GET"])
def root():
	return "Welcome Bumblebee"

app.run(host="0.0.0.0",port=8000,debug=True)
