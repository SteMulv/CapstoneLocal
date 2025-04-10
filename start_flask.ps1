# run this scriptby navigating to correct folder the
# .\start_flask.ps1

# Script
# Set the environment for your app
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# Create the virtual environment if it doesn't exist
if (-Not (Test-Path -Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate the virtual environment
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate.ps1

# Install the required packages (if not already installed)
Write-Host "Installing dependencies..."
pip install --upgrade pip
pip install flask

# Launch the Flask app in debug mode
Write-Host "Running Flask app in debug mode..."
flask --app app --debug run
