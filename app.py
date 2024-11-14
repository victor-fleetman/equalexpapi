# Metgod 1
from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # message = "<strong>Welcome to the Gist API!</strong>"
    # return render_template_string(message)
    return "<strong>Welcome to the Gist API!</strong>"

@app.route('/<username>')   # username to test with is 'octocat'
def get_gists(username):
    # Make a GET request to the GitHub API to fetch the user's Gists
    url = f"https://api.github.com/users/{username}/gists"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        gists = response.json()
        
        # Extract gist information
        gist_info = []
        for gist in gists:
            gist_info.append({
                "id": gist["id"],
                "url": gist["html_url"],
                "description": gist["description"]
            })
        
        return jsonify({"gists": gist_info})
    
    except requests.exceptions.RequestException as e:
        # Handle API request errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
