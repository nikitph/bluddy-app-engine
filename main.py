from flask import Flask, render_template, request
from emailassistant import EmailAssistant

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/contactus')
def contact_us_form():
    return render_template('contact.html')


@app.route('/contactus', methods=['POST'])
def contact_us_form_post():
    # Dump request in DB
    email = EmailAssistant()
    email.emailer('alpha@nikitph.com', 'nikitph@gmail.com', request.form['email'], request.form['message'])
    return render_template('confirmation.html', message='Successfully sent')


@app.route('/scheduler')
def scheduler_form():
    return render_template('scheduler.html')


@app.route('/scheduler', methods=['POST'])
def scheduler_form_post():
    document = {'message': request.form}
    body = 'Appointment confirmed for ' + request.form['name'] + ' Resident of: ' + request.form['address'] + ' on ' + \
           request.form['date'] + ' at ' + request.form['time']
    email = EmailAssistant()
    email.emailer('alpha@nikitph.com', request.form['email'], 'Your appointment confirmation from Bluddy', body)
    return render_template('confirmation.html',
                           message='Appointment confirmed for ' + request.form['name'] + ' Resident of: ' +
                                   request.form['address'] + ' on ' + request.form['date']
                                   + ' at ' + request.form['time'])
