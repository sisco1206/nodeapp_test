import os
from app import create_app

app = create_app()

if __name__=="__main__":
    port = int(os.environ.get("PORT, 5000"))
    app.jinja_env.auto_reload = True
    app.Config["TEMPLATES_AUTO_RELAOD"] = True
    app.run(host="0.0.0.0", port=port)