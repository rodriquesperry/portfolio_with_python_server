from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def portfolio():
    return render_template('./index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name + '.html')


def write_to_db(data):
    with open('database.txt', mode='a') as database:
          database.write(f'{str(data)}\n')
    

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # Transform whatever the data is into a dictionary
        try:
          data = request.form.to_dict()
          write_to_db(data)
          return redirect('/generic')
        except:
            return 'Did not save to db!'
    else:
        return 'something went wrong. Try again!'
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
