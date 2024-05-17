from app import db
from app.models import *

# User data for login tests
users = [
    {"username": "testuser1", "password": "securepass1", "email": "user1@example.com"},
    {"username": "testuser2", "password": "securepass2", "email": "user2@example.com"}
]

# Sample data for form submission tests
form_data = {
    "contact_form": {
        "name": "John Doe",
        "email": "john@example.com",
        "message": "Hello, this is a test message."
    },
    "registration_form": {
        "username": "newuser",
        "password": "newpassword",
        "email": "newuser@example.com"
    }
}

# Mock responses for API calls
api_responses = {
    "login_success": {"status": "success", "message": "Login successful"},
    "login_failure": {"status": "error", "message": "Invalid credentials"}
}

# Configuration settings for different test environments
config_settings = {
    "development": {"DEBUG": True, "DATABASE_URI": "sqlite:///dev.db"},
    "production": {"DEBUG": False, "DATABASE_URI": "sqlite:///prod.db"}
}
  
