This repo serves as a basic structure for most common web projects. It uses django and customizes it with:
 - `core` app for homepage/generic pages.
 - `accounts` app with login/logout.
 - User model that replaces username field with email.
 - `Dockerfile` that uses a `uwsgi` server as the container's process.