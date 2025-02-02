from flask import Flask

def create_app():
    app = Flask(__name__)

    """
    This block imports the blueprints for 'chat', 'upload', and 'remove' 
    routes and registers them with the app, allowing the app to handle 
    requests related to these routes.
    """
    from mainapp.routes.conversation_route import chat
    from mainapp.routes.uploadfile_route import upload
    from mainapp.routes import route

    """
    This block ensures that the Flask app is returned after registering 
    all blueprints, completing the setup of the application.
    """
    app.register_blueprint(chat, url_prefix="")
    app.register_blueprint(upload, url_prefix="")
    app.register_blueprint(route,url_prefix="")

    return app