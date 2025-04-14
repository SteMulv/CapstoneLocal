#!/bin/bash

# Run this script by navigating to the correct folder then:
# make executable chmod +x start_flask.sh
# # ./start_flask.sh

# Set environment variables for Flask
export FLASK_APP="app.py"
export FLASK_ENV="development"

# Create the virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv ./venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source ./venv/bin/activate

# Install the required packages from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "WARNING: requirements.txt not found. Installing Flask only..."
    pip install flask
fi

# Launch the Flask app in debug mode
echo "Running Flask app in debug mode..."
flask --app app --debug run

# To stop the app, press Ctrl+C, then run:
# deactivate
