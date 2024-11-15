### Gist API Flask Application
## Building and running your application

This Flask application provides a simple API to retrieve public Gists from GitHub users.
Features
    Retrieves public Gists for a given GitHub username
    Displays Gist information including id, URL, and description
    Handles API errors gracefully

## Setup
Compile the following files:
- requirements.txt
- README.md
- Dockerfile
- app.py

## Usage
The application provides two endpoints:
    GET /: Returns a welcome message
    GET /<username>: Retrieves public Gists for the specified GitHub username
    Open http://localhost:5000 in your browser. [Port can be any of your choice mapped to 5000 the port Flask listens on]

GET /<username>
Returns:
    A JSON object containing an array of gist objects:
{
  "gists": [
    {
      "id": "gist_id",
      "url": "gist_url",
      "description": "gist_description"
    },
    ...
  ]
}

### Acknowledgments
    This application uses Flask as the web framework
    It relies on the Python requests library for making HTTP requests to the GitHub API

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)