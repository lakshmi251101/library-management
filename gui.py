from tkinter import *
import psycopg2
from datetime import datetime


root = Tk()
root.title('postgres')
root.geometry("500x550")

def clear():
	f_name.delete(0, END)
	l_name.delete(0, END)

def query():
	conn = psycopg2.connect(
		host = "localhost", 
		database = "project",
		user = "postgres",
		password = "Pes@123", 
		port = "5432",
		)

	c = conn.cursor()

	c.execute('''CREATE TABLE IF NOT EXISTS m_reserved
		(mid char(4),book_id int,retdate DATE,issuedate DATE DEFAULT CURRENT_DATE,duedate DATE DEFAULT CURRENT_DATE +7,
                duefee  float, primary key(book_id),
                 foreign key(mid) references member,foreign key(book_id) references books);
		''')

	conn.commit()
	conn.close()

def submit():
	conn = psycopg2.connect(
			host = "localhost", 
		database = "project",
		user = "postgres",
		password = "Pes@123", 
		port = "5432",
		)
	c = conn.cursor()

	# Insert data into table
	thing1 = f_name.get()
	thing2 = l_name.get()
	c.execute('''INSERT INTO m_reserved(mid, book_id)
		VALUES (%s, %s)''', (thing1, thing2)
		)
	
	conn.commit()	
	conn.close()
		
	update()
	clear()

def delete():
        conn = psycopg2.connect(
			host = "localhost", 
		database = "project",
		user = "postgres",
		password = "Pes@123", 
		port = "5432",
		)
        c=conn.cursor()
        thing2=l_name.get()
        c.execute('''DELETE FROM m_reserved where book_id ={}'''.format(thing2))
    
        conn.commit()
        conn.close()

def updatemain():
        conn = psycopg2.connect(
			host = "localhost", 
		database = "project",
		user = "postgress",
		password = "Pes@123", 
		port = "5432",
		)
        c=conn.cursor()
        c.execute("SELECT * FROM m_reserved")
        thing1=f_name.get()
        thing2=l_name.get()
        c.execute('''update m_reserved set mid=%s where book_id =%s''',(thing1,thing2))
    
        conn.commit()
        conn.close()

def update():
	# Configure and connect to Postgres
	conn = psycopg2.connect(
			host = "localhost", 
		database = "project",
		user = "postgres",
		password = "Pes@123", 
		port = "5432",
		)

	c = conn.cursor()

	c.execute("SELECT * FROM m_reserved")
	records = c.fetchall()

	output = ''

	for record in records:
		output_label.config(text=f'{output}\n{record[0]}    {record[1]}     {record[2]}    {record[3]}    {record[4]}    {record[5]}')
		output = output_label['text']

	conn.close()
	
my_frame = LabelFrame(root, text="Library database")
my_frame.pack(pady=20)

f_label = Label(my_frame, text="mid:")
f_label.grid(row=0, column=0, pady=10, padx=10)

f_name = Entry(my_frame, font=("Helvetica, 18"))
f_name.grid(row=0, column=1, pady=10, padx=10)

l_label = Label(my_frame, text="book_id:")
l_label.grid(row=1, column=0, pady=10, padx=10)

l_name = Entry(my_frame, font=("Helvetica, 18"))
l_name.grid(row=1, column=1, pady=10, padx=10)


submit_button = Button(my_frame, text="submit", command=submit)
submit_button.grid(row=3, column=0, pady=10, padx=10)

update_button = Button(my_frame, text="record", command=update)
update_button.grid(row=3, column=1, pady=10, padx=10)

delete_button = Button(my_frame, text="delete", command=delete)
delete_button.grid(row=3, column=2, pady=10, padx=10)

clear_button = Button(my_frame, text="clear", command=clear)
clear_button.grid(row=4, column=2, pady=10, padx=10)

update_button = Button(my_frame, text="Update", command=updatemain)
update_button.grid(row=4, column=0, pady=10, padx=10)




output_label = Label(root, text="")
output_label.pack(pady=50)



query()

root.mainloop()
