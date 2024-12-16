import os
from fasthtml.common import *
import requests

app, rt = fast_app()

# Define the routes and the corresponding filenames
routes = [
    ('/', 'index.html'),
    ('/miembros', 'miembros.html'),
    ('/publicaciones', 'publicaciones.html'),
]

# Set the base URL of your local server (e.g., localhost)
base_url = 'http://localhost:5001/fasthtml-deploy-test'

# Function to build static HTML for each route
def build_static_html():
    # Create a build directory to store the HTML files
    if not os.path.exists('build'):
        os.mkdir('build')

    for route, filename in routes:
        # Make an HTTP request to the app’s route
        response = requests.get(f'{base_url}{route}')
        
        if response.status_code == 200:
            # Write the HTML to a file in the 'build' folder
            with open(f'build/{filename}', 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f'Successfully saved {route} as {filename}')
        else:
            print(f'Failed to fetch {route}')

import subprocess
import time

# Start the server in the background
server_process = subprocess.Popen(['python3', 'main.py'])

# Give the server some time to start
time.sleep(2)

# Run the build process to export static HTML
build_static_html()

# Stop the server after the build is complete
server_process.terminate()