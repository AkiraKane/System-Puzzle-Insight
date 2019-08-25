import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    results = []
 
    qry = db_session.query(Items)
    results = qry.all()

    # Return the most recent record 
    #item = results[-1]
    #results_string = "Name {}, Quantity {}, Description {}".format(item.name, item.quantity, item.description)

    # Return everything saved in the database 
    list_strings = ["Name {}, Quantity {}, Description {}".format(item.name, item.quantity, item.description) for item in results]
    results_string = ' | '.join(list_strings)

    return results_string
  

if __name__ == '__main__':
    app.run(host='0.0.0.0')
