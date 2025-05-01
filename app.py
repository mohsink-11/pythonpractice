from flask import Flask, render_template, request, url_for, redirect
import pyodbc

app=Flask(__name__)

# Define the connection string
connection_string = (
    "Driver={SQL Server};"
    "Server=DESKTOP-IELAAGT\\SQLEXPRESS;"
    "Database=Musa;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

@app.route('/',methods=['GET','POST'])
def index():

    connection = pyodbc.connect(connection_string)

    cursor = connection.cursor()
    # # cursor.execute("""create table employees( empid int primary key,
    # #                                 empname varchar(15),
    # #                empsalary int );""")

    # cursor.execute("""insert into employees values(65,'mohsin',2000);
    #                     insert into employees values(50,'salma',3000);

                
    # """)
    if(request.method=='POST'):
        empId=request.form.get('empid')
        empName=request.form.get('empname')
        empSalary=request.form.get('empsalary')

        cursor.execute("insert into employees values(?,?,?)",(empId,empName,empSalary))
        connection.commit()
        connection.close()
        return redirect(url_for('index'))

    cursor.execute("select * from employees")
    bench=cursor.fetchall()

    rows= []

    for ben in bench:
        rows.append({
            'Id':ben.empid,
            'Name':ben.empname,
            'Salary':ben.empsalary
        })

    connection.commit()

    connection.close()

    return render_template('index.html',rows=rows)

if __name__ == '__main__':
    app.run(debug=True)