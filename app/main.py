from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return jsonify(
            {
                "application": "DevSecOps Demo",
                "status": "running",
                "message": "Secure delivery starts here!"
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="127.0.0.1", port=5000, debug=False)