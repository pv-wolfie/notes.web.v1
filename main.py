from website import create_app

app = create_app()

# only if we run this file will we execute the app.run() method
if __name__ == '__main__':
    # runs the flask app
    app.run(debug=True)