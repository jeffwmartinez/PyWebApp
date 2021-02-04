from flask import Flask

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    return "PYTHON WORKS!"

if __name__ == '__main__':
    # run on app service?
    app.run(port=80)

    # Run the app server locally with Flask
    #app.run(port=5000, host='0.0.0.0')

    # run app locally without container
    #app.run('localhost', 4449) 
    
