from flask import Blueprint, render_template, request, jsonify, redirect, url_for
#store connections here

#initialise the blueprint
views = Blueprint(__name__, "views")

#@Blueprint
@views.route("/")
def home():
    return render_template("index.html", name="Daffa")

#@reder_template, request
@views.route("/profile")
def profile():
    #for URL query
    args = request.args
    username = args.get('name')
    # from index.html
    return render_template("profile.html", name=username)

#@jsonify
@views.route("/json")
def get_json(): 
    return jsonify({'name':'tim', 'coolness':10})

#how to access json data
#@request
@views.route("/data")
def get_data():
    data = request.json()
    return jsonify(data)

#redirect to a different page
#@redirect, url_for
@views.route("/reroute")
def activities():
    return redirect(url_for("views.home"))