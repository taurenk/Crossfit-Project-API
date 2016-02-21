from app import create_app

app = create_app(None)
app.run(debug=True)