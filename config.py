import os
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["APPLICATION_ROOT"] = "/"
app.debug = True


