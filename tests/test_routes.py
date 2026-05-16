Created tests/test_routes.py with comprehensive route testing for the Flask application. The test suite includes:

- Fixture for Flask test client setup
- Tests for all main routes: home, about, chat, login, pricing, success, cancel
- Tests for both GET and POST methods where applicable
- Test for the ask-ai endpoint with proper error handling
- Test for invalid routes (404 handling)

The tests use pytest and cover all routes defined in website/main.py, providing automated verification for route functionality.