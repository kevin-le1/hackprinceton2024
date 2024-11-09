import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from app.api import api_routes


def init_app() -> Flask:
    app = Flask(__name__, static_folder="../dist")
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # we serve the statically build react app w/ this catch-all and the static_folder
    with app.app_context():

        for blueprint in api_routes:
            app.register_blueprint(blueprint, url_prefix=f"/api/v1/{blueprint.name}/")

        @app.route("/", defaults={"path": ""})
        @app.route("/<path:path>")
        def serve(path: str):
            if app.static_folder is None:
                raise Exception("static folder not configured")
            if path != "" and os.path.exists(app.static_folder + "/" + path):
                return send_from_directory(app.static_folder, path)
            else:
                return send_from_directory(app.static_folder, "index.html")

    return app
