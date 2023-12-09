from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
#DB_PORT = int(os.getenv("DB_PORT", 3306))
#DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}

conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
)

# Create a database engine
engine = create_engine(conn_string, connect_args=connect_args)

app = Flask(__name__)   

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/patients')
def patients():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query1 = text('SELECT * FROM patients')

        result1 = connection.execute(query1)

        # Fetch all rows of data
        patientdata = result1.fetchall()

    return render_template('patients.html', data1=patientdata)

@app.route('/physicians')
def physicians():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query2 = text('SELECT * FROM physicians')

        result2 = connection.execute(query2)

        # Fetch all rows of data
        physicisndata = result2.fetchall()

    return render_template('physicians.html', data2=physiciandata)

@app.route('/patientlabs')
def patientlabs():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query3 = text('SELECT * FROM patientlabs')

        result3 = connection.execute(query3)

        # Fetch all rows of data
        patientlabsdata = result3.fetchall()

    return render_template('patientlabs.html', data3=patientlabsdata)

if __name__ == '__main__':
    app.run(debug=True)
