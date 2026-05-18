# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

We take the security of MY_WEBSITE seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: syed.abdul.rauf@example.com

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following information in your report:

- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

## Preferred Languages

We prefer all communications to be in English.

## Security Best Practices

When deploying this application:

1. **Environment Variables**: Never commit sensitive credentials. Use environment variables for:
   - API keys
   - Database credentials
   - Secret keys
   - Payment gateway credentials (Stripe keys, etc.)

2. **Dependencies**: Keep all Python dependencies up to date. Run `pip list --outdated` regularly.

3. **Flask Configuration**: 
   - Set `DEBUG = False` in production
   - Use a strong `SECRET_KEY`
   - Enable HTTPS in production

4. **Input Validation**: Always validate and sanitize user inputs, especially in the `/ask-ai` endpoint.

5. **Authentication**: Implement proper authentication and session management for the login functionality.

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine the affected versions
2. Audit code to find any similar problems
3. Prepare fixes for all supported versions
4. Release patches as soon as possible