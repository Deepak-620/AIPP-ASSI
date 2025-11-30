from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()

    # Basic server-side validation (always validate on server)
    if not username or not password:
        # For simplicity, re-render index (client-side JS should normally prevent this)
        error_msg = "Both fields required."
        return render_template('index.html', server_error=error_msg), 400

    # On successful login (demo): print username to console and show a simple success page
    print(f"Login successful for user: {username}")  # server console output

    # Render a simple success message
    return f"""
    <!doctype html>
    <html><head><title>Welcome</title></head><body>
    <h2>Login successful</h2>
    <p>Welcome, <strong>{username}</strong>!</p>
    <p><a href="{url_for('index')}">Back to home</a></p>
    </body></html>
    """

if __name__ == '__main__':
    app.run(debug=True)
