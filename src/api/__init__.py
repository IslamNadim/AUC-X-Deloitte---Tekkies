from .inventory import inventory_bp
from .predict import predict_bp
from .menu import menu_bp
from .shifts import shifts_bp

def register_routes(app):
    app.register_blueprint(inventory_bp, url_prefix="/api/inventory")
    app.register_blueprint(predict_bp, url_prefix="/api/inventory")
    app.register_blueprint(menu_bp, url_prefix="/api/menu")
    app.register_blueprint(shifts_bp, url_prefix="/api/shifts")
