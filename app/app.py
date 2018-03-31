from flask import Flask
app = Flask(__name__)

@app.route("/hi")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()