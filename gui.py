from tkinter import *
from tkinter import StringVar, Label, ttk, scrolledtext, filedialog, messagebox
from main_module import *


# TO verify New Student entries
def verifier():
	a = b = c = d = e = f = g = h = i = j = 0
	txt.delete(1.0, END)
	if not aa.get() or aa.get() == "SELECT":
		txt.insert(INSERT, " \n\n------------------------------>>\n\nSession  :  \n")
		a = 1
	if not admn.get() or admn.get():
		txt.insert(INSERT, "Addmission Number  :  \n")
		admnN = 1
	if not bb.get():
		txt.insert(INSERT, "Name of the Student  :  \n")
		b = 1
	if not cc.get():
		txt.insert(INSERT, "Father' Name  :  \n")
		c = 1
	if not dd.get():
		txt.insert(INSERT, "Mothers Name  :  \n")
		d = 1
	if not ee.get() or dd.get() == "SELECT":
		txt.insert(INSERT, "Class  :  \n")
		e = 1
	if not ff.get() or ee.get() == "SELECT":
		txt.insert(INSERT, "Section  :  \n")
		f = 1
	if not gg.get() or ff.get() == "SELECT":
		txt.insert(INSERT, "Gender  :  \n")
		g = 1
	if not hh.get() or gg.get() == "SELECT":
		txt.insert(INSERT, "Stream Chosen  :  \n")
		h = 1
	if not ii.get():
		txt.insert(INSERT, "DOB  :  \n")
		i = 1
	if not jj.get() or ii.get() == "SELECT":
		txt.insert(INSERT, "Mobile Number  :  \n")
		j = 1
	if not kk.get():
		txt.insert(INSERT, "Address  :  \n")
		k = 1

	if a == 1 or admnN == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1 or g == 1 or h == 1 or i == 1 or j == 1:
		return 1
	else:
		return 0


# TO verify Update Student entries
def verifier1():
	a = b = c = d = e = f = g = h = i = j = k = 0
	txt.delete(1.0, END)
	if not admn_admn1.get():
		txt.insert(INSERT, "Admission Number  :  \n")
		admnN = 1
	if not aa1.get() or aa1.get() == "SELECT":
		txt.insert(INSERT, " \n\n------------------------------>>\n\nSession  :  \n")
		a = 1
	if not bb1.get():
		txt.insert(INSERT, "Name of the Student  :  \n")
		b = 1
	if not cc1.get():
		txt.insert(INSERT, "Father' Name  :  \n")
		c = 1
	if not dd1.get():
		txt.insert(INSERT, "Mothers Name  :  \n")
		d = 1
	if not ee1.get() or dd1.get() == "SELECT":
		txt.insert(INSERT, "Class  :  \n")
		e = 1
	if not ff1.get() or ee1.get() == "SELECT":
		txt.insert(INSERT, "Section  :  \n")
		f = 1
	if not gg1.get() or ff1.get() == "SELECT":
		txt.insert(INSERT, "Gender  :  \n")
		g = 1
	if not hh1.get() or gg1.get() == "SELECT":
		txt.insert(INSERT, "Stream Chosen  :  \n")
		h = 1
	if not ii1.get():
		txt.insert(INSERT, "DOB  :  \n")
		i = 1
	if not jj1.get() or ii1.get() == "SELECT":
		txt.insert(INSERT, "Mobile Number  :  \n")
		j = 1
	if not kk1.get():
		txt.insert(INSERT, "Address  :  \n")
		k = 1

	if a == 1 or admnN == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1 or g == 1 or h == 1 or i == 1 or j == 1 or k == 1:
		return 1
	else:
		return 0


def add_student():
	if verifier() == 0:
		student = {"session": aa.get(), "addmission_number": admn.get(), "name_of_the_student": bb.get(),
				   "father's_name": cc.get(), "mother's_name": dd.get(), "class": ee.get(), "section": ff.get(),
				   "gender": gg.get(), "stream_chosen": hh.get(), "dob": ii.get(), "mobile": jj.get(),
				   "address": kk.get()}

		return_data = student_create(student)
		txt.delete(1.0, END)
		for key, value in return_data.items():
			txt.insert(INSERT, "\n------------------------------>>\n")
			txt.insert(INSERT, "Details of student -->>" + "\n\nAddmission No. : " + return_data[key][
				"addmission_number"] + "\nName : " + return_data[key]["name_of_the_student"] + "\nFather's Name : " +
					   return_data[key]["father's name"] + "\nMother's Name : " + return_data[key][
						   "mother's name"] + "\nClass : " + return_data[key]["class"] + "\nSection : " +
					   return_data[key]["section"] + "\nGender : " + return_data[key]["gender"] + "\nStream : " +
					   return_data[key]["stream_chosen"] + "\nDOB : " + return_data[key]["dob"] + "\nMobile : " +
					   return_data[key]["mobile"] + "\nAddress :" + return_data[key]["address"], "\n")

		aa.delete(0, END)
		admn.delete(0, END)
		bb.delete(0, END)
		cc.delete(0, END)
		dd.delete(0, END)
		ee.delete(0, END)
		ff.delete(0, END)
		gg.delete(0, END)
		hh.delete(0, END)
		ii.delete(0, END)
		jj.delete(0, END)
		kk.delete(0, END)


# txt.insert(INSERT,"Details of student -->>"+"\n\nAdmission No. : "+admn+"\nName : "+return_data[key][
# "name_of_the_student"] + "\nFather's Name : "+return_data[key]["father's name"]+"\nMother's Name : "+return_data[
# key]["mother's name"] +"\nClass : "+return_data[key]["class"] +"\nSection : "+return_data[key]["section"] 
# +"\nGender : "+return_data[key]["gender"] +"\nStream : "+return_data[key]["stream_chosen"]+"\nDOB : "+return_data[
# key]["dob"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n") 
def view_student():
	return_data = student_list()
	txt.delete(1.0, END)
	txt.insert(INSERT, "\n Addmission No.\t\t Student Name\t\t Father's Name\t\t Mother's Name\t\t Class\t\t Section\t\t "
    "Gender\t\t Stream \t\t DOB\t\t Mobile\t\t Address\n") 
	for key, value in return_data.items():
		if return_data[key] == "This Record is Deleted from System":
			continue
		else:
			txt.insert(INSERT, "\n" + return_data[key]["addmission_number"] + "\t\t" + return_data[key][
				"name_of_the_student"] + "\t\t" + return_data[key]["father's_name"] + "\t\t" + return_data[key][
						   "mother's_name"] + "\t\t" + return_data[key]["class"] + "\t\t" + return_data[key][
						   "section"] + "\t\t" + return_data[key]["gender"] + "\t\t" + return_data[key][
						   "stream_chosen"] + "\t\t" + return_data[key]["dob"] + "\t\t" + return_data[key][
						   "mobile"] + ",\t\t" + return_data[key]["address"], "\n")


def update_student():
	if verifier1() == 0:
		student = {"session": aa1.get(), "addmission_number": admn_admn1.get(), "name_of_the_student": bb1.get(),
				   "father's_name": cc1.get(), "mother's_name": dd1.get(), "class": ee1.get(), "section": ff1.get(),
				   "gender": gg1.get(), "stream_chosen": hh1.get(), "dob": ii1.get(), "mobile": jj1.get(),
				   "address": kk1.get()}
		return_data = student_update(admnNo, student)
		txt.delete(1.0, END)
		for key, value in return_data.items():
			if key == rollNo:
				txt.insert(INSERT, "\n------------------------------>>\n")
				txt.insert(INSERT, "Updated Details of Student -->>" + "\n\nAdmission No. : " + return_data[key][
					"addmission_number"] + "\nName : " + return_data[key][
							   "name_of_the_student"] + "\nFather's Name : " + return_data[key][
							   "father's name"] + "\nMother's Name : " + return_data[key][
							   "mother's name"] + "\nClass : " + return_data[key]["class"] + "\nSection : " +
						   return_data[key]["section"] + "\nGender : " + return_data[key]["gender"] + "\nStream : " +
						   return_data[key]["stream_chosen"] + "\nDOB : " + return_data[key]["dob"] + "\nMobile : " +
						   return_data[key]["mobile"] + "\nAddress :" + return_data[key]["address"], "\n")

		aa1.delete(0, END)
		admn_admn1.delete(0, END)
		bb1.delete(0, END)
		cc1.delete(0, END)
		dd1.delete(0, END)
		ee1.delete(0, END)
		ff1.delete(0, END)
		gg1.delete(0, END)
		hh1.delete(0, END)
		ii1.delete(0, END)
		jj1.delete(0, END)
		kk1.delete(0, END)


def delete_student():
	messagebox.showwarning("Warning", "Are you sure ?")
	data = student_delete(entry_delete.get())
	txt.delete(1.0, END)
	txt.insert(INSERT, data)


def search_by_class():
	pass


def clse():
	sys.exit()


def saveFile():
	f = filedialog.asksaveasfile(mode='w', defaultextension='.csv')
	if f != None:
		data = txt.get('1.0', END)
	try:
		f.write(data)
		txt.delete(1.0, END)
		txt.insert(INSERT, "Spreadsheet Saved Successfully !")
	except:
		messagebox.showerror(title="Oops!!", message="Unable to save file!")


def classwise():
	return_data = student_list()
	txt.delete(1.0, END)
	if combo_class.get() in ('11', '12'):
		for key, value in return_data.items():
			if return_data[key] == "This Record is Deleted from System":
				continue
			else:
				if combo_class.get() == return_data[key]["class"]:
					txt.insert(INSERT, "\n" + return_data[key]["addmission_number"] + "\t\t" + return_data[key][
						"name_of_the_student"] + "\t\t" + return_data[key]["father's_name"] + "\t\t" + return_data[key][
								   "mother's_name"] + "\t\t" + return_data[key]["class"] + "\t\t" + return_data[key][
								   "section"] + "\t\t" + return_data[key]["gender"] + "\t\t" + return_data[key][
								   "stream_chosen"] + "\t\t" + return_data[key]["dob"] + "\t\t" + return_data[key][
								   "mobile"] + ",\t\t" + return_data[key]["address"], "\n")


if __name__ == "__main__":
	root = Tk()
	w = 1000
	h = 700
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	root.title("Student Management System")

	# ----------------------

	sess = StringVar()
	admn = StringVar()
	n = StringVar()
	fa_name = StringVar()
	mo_name = StringVar()
	cl = StringVar()
	sect = StringVar()
	gen = StringVar()
	stream = StringVar()
	dob = StringVar()
	mob = StringVar()
	ad = StringVar()

	heading = Label(root, text="New Student", font=("Arial", 12), foreground="#ee9a4d")
	label_admn = Label(root, text="Admission Number", font=("Arial", 10), width=25)
	label_a = Label(root, text="Session  :  ", font=("Arial", 10), width=10)
	label_b = Label(root, text="Name of the Student  :  ", font=("Arial", 10), width=25)
	label_c = Label(root, text="Father's Name  :  ", font=("Arial", 10), width=25)
	label_d = Label(root, text="Mothers's Name  :  ", font=("Arial", 10), width=25)
	label_e = Label(root, text="Class  :  ", font=("Arial", 10), width=25)
	label_f = Label(root, text="Section  :  ", font=("Arial", 10), width=25)
	label_g = Label(root, text="Gender  :  ", font=("Arial", 10), width=25)
	label_h = Label(root, text="Stream chosen  :", font=("Arial", 10), width=25)
	label_i = Label(root, text="DOB :  ", font=("Arial", 10), width=25)
	label_j = Label(root, text="Mobile  :  ", font=("Arial", 10), width=25)
	label_k = Label(root, text="Address  :  ", font=("Arial", 10), width=30)

	admn_admn = Entry(root, textvariable=admn, width=8)

	aa = ttk.Combobox(root, width=10)
	aa['values'] = ("SELECT", "2020-21")
	aa.current(0)

	bb = Entry(root, textvariable=n, width=30)

	cc = Entry(root, textvariable=fa_name, width=30)
	dd = Entry(root, textvariable=mo_name, width=30)

	ee = ttk.Combobox(root, width=8)
	ee['values'] = ("SELECT", 11, 12)
	ee.current(0)

	ff = ttk.Combobox(root, width=8)
	ff['values'] = ("SELECT", "A", "B", "C", "D", "E")
	ff.current(0)

	gg = ttk.Combobox(root, width=10)
	gg['values'] = ("SELECT", "Male", "Female")
	gg.current(0)

	hh = ttk.Combobox(root, width=12)
	hh['values'] = ("SELECT", "SCIENCE", "COMMERCE", "HUMANITIES", "ARTS")
	hh.current(0)

	ii = Entry(root, textvariable=dob, width=10)

	jj = Entry(root, textvariable=mob, width=10)

	kk = Entry(root, textvariable=ad, width=45)

	# ----------------------

	heading1 = Label(root, text="Update Student", font=("Arial", 12), foreground="#ee9a4d")
	label_admn1 = Label(root, text="Admission Number :", font=("Arial", 10), width=15)
	label_a1 = Label(root, text="Session  :  ", font=("Arial", 10), width=10)
	label_b1 = Label(root, text="Name of the Student  :  ", font=("Arial", 10), width=15)
	label_c1 = Label(root, text="Father's Name  :  ", font=("Arial", 10), width=15)
	label_d1 = Label(root, text="Mothers's Name  :  ", font=("Arial", 10), width=15)
	label_e1 = Label(root, text="Class  :  ", font=("Arial", 10), width=15)
	label_f1 = Label(root, text="Section  :  ", font=("Arial", 10), width=15)
	label_g1 = Label(root, text="Gender  :  ", font=("Arial", 10), width=15)
	label_h1 = Label(root, text="Stream chosen  :", font=("Arial", 10), width=15)
	label_i1 = Label(root, text="DOB :  ", font=("Arial", 10), width=15)
	label_j1 = Label(root, text="Mobile  :  ", font=("Arial", 10), width=15)
	label_k1 = Label(root, text="Address  :  ", font=("Arial", 10), width=30)

	admn1 = StringVar()
	sess1 = StringVar()
	n1 = StringVar()
	fa_name1 = StringVar()
	mo_name1 = StringVar()
	cl1 = StringVar()
	sect1 = StringVar()
	gen1 = StringVar()
	stream1 = StringVar()
	dob1 = StringVar()
	mob1 = StringVar()
	ad1 = StringVar()

	admn_admn1 = Entry(root, textvariable=admn1, width=8)

	aa1 = ttk.Combobox(root, width=10)
	aa1['values'] = ("2020-21")
	aa1.current(0)

	bb1 = Entry(root, textvariable=n, width=30)

	cc1 = Entry(root, textvariable=fa_name, width=30)
	dd1 = Entry(root, textvariable=mo_name, width=30)

	ee1 = ttk.Combobox(root, width=8)
	ee1['values'] = ("SELECT", 11, 12)
	ee1.current(0)

	ff1 = ttk.Combobox(root, width=8)
	ff1['values'] = ("SELECT", "A", "B", "C", "D", "E")
	ff1.current(0)

	gg1 = ttk.Combobox(root, width=10)
	gg1['values'] = ("SELECT", "Male", "Female")
	gg1.current(0)

	hh1 = ttk.Combobox(root, width=12)
	hh1['values'] = ("SELECT", "SCIENCE", "COMMERCE", "HUMANITIES", "ARTS")
	hh1.current(0)

	ii1 = Entry(root, textvariable=dob, width=10)

	jj1 = Entry(root, textvariable=mob, width=10)

	kk1 = Entry(root, textvariable=ad, width=45)

	# ----------------------
	admn_delete = StringVar()
	heading2 = Label(root, text="Delete Student", font=("Arial", 12), foreground="#ee9a4d")
	label_del = Label(root, text="Record", font=("Arial", 12), width=10)
	label_delete = Label(root, text="Admission Number:", font=("Arial", 12), width=10)
	entry_delete = Entry(root, textvariable=admn_delete, font=("Arial", 12), width=10)


	def addnew():
		heading.grid(row=8, column=1, columnspan=2)
		label_admn.grid(row=9, column=1)
		label_a.grid(row=10, column=1)
		label_b.grid(row=11, column=1)
		label_c.grid(row=12, column=1)
		label_d.grid(row=13, column=1)
		label_e.grid(row=14, column=1)
		label_f.grid(row=15, column=1)
		label_g.grid(row=16, column=1)
		label_h.grid(row=17, column=1)
		label_i.grid(row=18, column=1)
		label_j.grid(row=19, column=1)
		label_k.grid(row=20, column=1)

		admn_admn.grid(row=9, column=2)
		aa.grid(row=10, column=2)
		bb.grid(row=11, column=2)
		cc.grid(row=12, column=2)
		dd.grid(row=13, column=2)
		ee.grid(row=14, column=2)
		ff.grid(row=15, column=2)
		gg.grid(row=16, column=2)
		hh.grid(row=17, column=2)
		ii.grid(row=18, column=2)
		jj.grid(row=19, column=2)
		kk.grid(row=20, column=2)

		b1 = Button(root, text="ADD", command=lambda: add_student(), width=40, background='#4E7565', foreground="white",
					font=("Arial", 11))
		b1.grid(row=21, column=1, columnspan=2)


	def update():
		heading1.grid(row=8, column=3, columnspan=2)

		label_admn.grid(row=9, column=3)
		label_a1.grid(row=10, column=3)
		label_b1.grid(row=11, column=3)
		label_c1.grid(row=12, column=3)
		label_d1.grid(row=13, column=3)
		label_e1.grid(row=14, column=3)
		label_f1.grid(row=15, column=3)
		label_g1.grid(row=16, column=3)
		label_h1.grid(row=17, column=3)
		label_i1.grid(row=18, column=3)
		label_j1.grid(row=19, column=3)
		label_k1.grid(row=20, column=3)

		admn_admn1.grid(row=9, column=4)
		aa1.grid(row=10, column=4)
		bb1.grid(row=11, column=4)
		cc1.grid(row=12, column=4)
		dd1.grid(row=13, column=4)
		ee1.grid(row=14, column=4)
		ff1.grid(row=15, column=4)
		gg1.grid(row=16, column=4)
		hh1.grid(row=17, column=4)
		ii1.grid(row=18, column=4)
		jj1.grid(row=19, column=4)
		kk1.grid(row=20, column=4)

		b2 = Button(root, text="UPDATE", command=lambda: update_student(), width=40, background='#4E8975',
					foreground="white", font=("Arial", 11))
		b2.grid(row=21, column=3, columnspan=2)


	# ----------------------

	def delete():
		heading2.grid(row=8, column=5, columnspan=1)

		#   label_del.grid(row=9 , column=5 )
		label_delete.grid(row=14, column=5)
		entry_delete.grid(row=15, column=5)

		b3 = Button(root, text="DELETE", command=lambda: delete_student(), width=25, background='#4E8975',
					foreground="white", font=("Arial", 11))
		b3.grid(row=21, column=5, columnspan=1)


	# ----------------------

	dashboard = Label(root, text=" Dashboard ", font=("Arial", 16), foreground="#ee9a4d")
	dashboard.grid(row=0, column=0)

	view = Button(root, text="VIEW ALL", background='#4E8975', foreground="white", command=lambda: view_student(),
				  width=10, font=("Arial", 11))
	view.grid(row=0, column=1)

	add = Button(root, text="NEW", command=addnew, width=10, background='#4E8975', foreground="white",
				 font=("Arial", 11))
	add.grid(row=0, column=2)

	update = Button(root, text="UPDATE", command=update, width=10, background='#4E8975', foreground="white",
					font=("Arial", 11))
	update.grid(row=0, column=3)

	delete = Button(root, text="DELETE", command=delete, width=10, background='#4E8975', foreground="white",
					font=("Arial", 11))
	delete.grid(row=0, column=4)

	txt = scrolledtext.ScrolledText(root, width=120, height=10, background='#fff8dc', foreground="#4E8975",
									font=("Arial", 11))
	txt.grid(row=1, column=0, rowspan=5, columnspan=7)

	save = Button(root, text="Save As Spreadsheet", command=saveFile, width=18, background='#4E8975',
				  foreground="white", font=("Arial", 11))
	save.grid(row=5, column=2, columnspan=3)

	combo_class = ttk.Combobox(root, width=15)  # Filter Searches
	combo_class['values'] = ("SELECT", 11, 12)
	combo_class.current(0)  # set the selected item
	combo_class.grid(row=0, column=5)

	combo_class_button = Button(root, text="SEARCH", command=classwise, width=10, background='#4E8975',
								foreground="white", font=("Arial", 11))
	combo_class_button.grid(row=0, column=6)

	classroom = Button(root, text="Go to Classroom", command=lambda: classroom(), width=40, background='#4E8976',
					   foreground="white", font=("Arial", 11))
	classroom.grid(row=22, column=3, columnspan=2)

	root.mainloop()
