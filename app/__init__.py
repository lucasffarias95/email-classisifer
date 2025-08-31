from flask import Flask

def create_app():
    app = Flask(__name__, 
    static_folder='static',template_folder='templates') 
    
    from .web.api import api
    app.register_blueprint(api, url_prefix='/api')
    
    from .web.routes import web
    app.register_blueprint(web)
    
    return app