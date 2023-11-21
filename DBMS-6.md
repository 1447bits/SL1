
# TITLE :

Database Connectivity: Write a program to implement MySQL/Oracle database connectivity with any front end language to implement Database navigation operations (add, delete, edit).


<hr/>

Run the Python script, and your application will be accessible at http://127.0.0.1:5000/. This example allows you to add, delete, and edit records in a MySQL database through a simple web interface.

<hr/>




CODE:

pyhon.py 

```python
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'your_username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'
app.config['MYSQL_DATABASE_DB'] = 'your_database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

# Route for displaying and navigating the data
@app.route('/')
def index():
    # Fetch data from the database
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

# Route for adding new data
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        name = request.form['name']

        cursor = mysql.get_db().cursor()
        cursor.execute("INSERT INTO your_table (Roll_no, Name) VALUES (%s, %s)", (roll_no, name))
        mysql.get_db().commit()

    return redirect('/')

# Route for deleting data
@app.route('/delete/<int:roll_no>')
def delete(roll_no):
    cursor = mysql.get_db().cursor()
    cursor.execute("DELETE FROM your_table WHERE Roll_no = %s", (roll_no,))
    mysql.get_db().commit()

    return redirect('/')

# Route for editing data
@app.route('/edit/<int:roll_no>')
def edit(roll_no):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM your_table WHERE Roll_no = %s", (roll_no,))
    data = cursor.fetchone()
    return render_template('edit.html', data=data)

# Route for updating data
@app.route('/update/<int:roll_no>', methods=['POST'])
def update(roll_no):
    if request.method == 'POST':
        new_name = request.form['name']

        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE your_table SET Name = %s WHERE Roll_no = %s", (new_name, roll_no))
        mysql.get_db().commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

```

<hr/>
####################################################################################
<hr/>


templates/index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Navigation</title>
</head>
<body>
    <h1>Database Navigation</h1>
    <table border="1">
        <tr>
            <th>Roll No</th>
            <th>Name</th>
            <th>Action</th>
        </tr>
        {% for row in data %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>
                <a href="/edit/{{ row[0] }}">Edit</a>
                <a href="/delete/{{ row[0] }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
    <form action="/add" method="post">
        <label for="roll_no">Roll No:</label>
        <input type="text" name="roll_no" required>
        <label for="name">Name:</label>
        <input type="text" name="name" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>
```


<hr/>
############################################################################################
<hr/>



templates/edit.html:


```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Data</title>
</head>
<body>
    <h2>Edit Data</h2>
    <form action="/update/{{ data[0] }}" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" value="{{ data[1] }}" required>
        <button type="submit">Update</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>

```










