
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT, status TEXT)''')
conn.commit()

# Home page route
@app.route('/')
def index():
    # Fetch all tasks from the database
    tasks = c.execute('SELECT * FROM todos').fetchall()
    return render_template('index.html', tasks=tasks)

# Add a new task
@app.route('/add_task', methods=["POST"])
def add_task():
    # Get the task from the form
    task = request.form.get('task')
    # Insert the task into the database
    c.execute('INSERT INTO todos (task, status) VALUES (?, ?)', (task, 'New'))
    conn.commit()
    # Redirect to the home page
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete_task/<int:id>')
def delete_task(id):
    # Delete the task from the database
    c.execute('DELETE FROM todos WHERE id=?', (id,))
    conn.commit()
    # Redirect to the home page
    return redirect(url_for('index'))

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
