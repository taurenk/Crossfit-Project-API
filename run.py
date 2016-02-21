from app import create_app

app = create_app('../config_dev.py')
app.run(debug=True)