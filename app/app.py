from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "1.0")
    environment = os.getenv("ENVIRONMENT", "development")

    return f"""
    <html>
        <head>
            <title>DevOps Application</title>
        </head>
        <body>
            <h1>🚀 DevOps CI/CD Platform</h1>
            <h2>Application is Running!</h2>
            <p>Version: {version}</p>
            <p>Environment: {environment}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    return os.getenv("APP_VERSION", "1.0")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
