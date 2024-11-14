Gist API Flask Application

This Flask application provides a simple API to retrieve public Gists from GitHub users.
Features

    Retrieves public Gists for a given GitHub username
    Displays Gist information including id, URL, and description
    Handles API errors gracefully

Setup
To run this application locally:

    Install Python and pip if not already installed
    Clone this repository
    Create a new virtual environment:

python -m venv venv

    Activate the virtual environment:
        On Windows: venv\Scripts\activate
        On macOS/Linux: source venv/bin/activate
    Install required packages:

pip install flask requests
    Run the application:
python app.py

Usage
The application provides two endpoints:
    GET /: Returns a welcome message
    GET /<username>: Retrieves public Gists for the specified GitHub username

API Documentation

Welcome Endpoint
GET /
Returns a simple welcome message.
User Gists Endpoint

GET /<username>
Parameters:
    username (required): The GitHub username to retrieve Gists for
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

Error Handling
The application handles API request errors gracefully, returning an error message in JSON format if something goes wrong during the API call.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
    This application uses Flask as the web framework
    It relies on the Python requests library for making HTTP requests to the GitHub API

