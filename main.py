#import the website package, grab create app function and use  to create app and run it
'''cd "/Users/ludginiedorval/Desktop/Python website"
source venv/bin/activate'''
from website import create_app #we can do that because website is a python package

app = create_app()

#we want it to run the webserve only if we run this file true
if __name__ == '__main__': #running web server
    app.run(debug=True) #run our flask app, debug=true when we make changes to our pythin code it is going to automatically rerun websercer
#in production we would not set debug=true because it would reset the web server everytime

