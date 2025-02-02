from mainapp import create_app



"""
The `create_app` function is responsible for initializing and configuring 
the Flask application instance. It sets up the necessary components, such as:

- Configurations for the application.
- Integration of extensions.
- Registration of blueprints for modular routing.
"""
app=create_app()
if __name__ == "__main__":
    app.run(debug=True)


  