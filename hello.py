from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<a href='/on'><button  style = "height:50%;cursor:pointer;display: inline-block;font-weight: 400;text-align: center;white-space: nowrap;vertical-align: middle;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;border: 1px solid transparent;padding: .375rem .75rem;font-size: 7rem;line-height: 1.5;border-radius: .25rem;transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;width: 100%;color: #fff;background-color: #007bff;border-color: #007bff;">Turn On</button></a>
    <a href='/off'><button style = "height:50%;cursor:pointer;display: inline-block;font-weight: 400;text-align: center;white-space: nowrap;vertical-align: middle;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;border: 1px solid transparent;padding: .375rem .75rem;font-size: 7rem;line-height: 1.5;border-radius: .25rem;transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;width: 100%;color: #fff;background-color: #dc3545;border-color: #dc3545;">Turn Off</button></a>"""

@app.route("/on")
def turn_on():
    return """<a href='/'><button  style = "height:100%;margin-bottom:30px;cursor:pointer;display: inline-block;font-weight: 400;text-align: center;white-space: nowrap;vertical-align: middle;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;border: 1px solid transparent;padding: .375rem .75rem;font-size: 7rem;line-height: 1.5;border-radius: .25rem;transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;width: 100%;color: #fff;background-color: #007bff;border-color: #007bff;">Back</button></a>"""

@app.route("/off")
def turn_off():
    return """<a href='/'><button  style = "height:100%;margin-bottom:30px;cursor:pointer;display: inline-block;font-weight: 400;text-align: center;white-space: nowrap;vertical-align: middle;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;border: 1px solid transparent;padding: .375rem .75rem;font-size: 7rem;line-height: 1.5;border-radius: .25rem;transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;width: 100%;color: #fff;background-color: #007bff;border-color: #007bff;">Back</button></a>"""