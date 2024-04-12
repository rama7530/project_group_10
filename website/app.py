from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\ramak\OneDrive\Desktop\Project_files') # change the base path to your respective folder path
db_name = "IMDB.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index.html')
def index():
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a query to fetch data from the database
    cursor.execute('SELECT * FROM Movies')
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Pass the data to the template for rendering
    return render_template('index.html', data=data)

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
