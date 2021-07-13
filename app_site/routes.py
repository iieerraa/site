from app_site import app


@app.route('/')
# @app.route('/index')
def index():
    return 'Hi!'
