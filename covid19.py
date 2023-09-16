# importing tkinter and sql connector
import mysql.connector as mys
from PIL import ImageTk, Image
from tkinter import *

# connecting database to python
mycon = mys.connect(host='localhost', user='root', passwd='1234', database='coviddb')
mycursor = mycon.cursor()
mycursor.execute('select * from c19')
mydata = mycursor.fetchall()
mydata2 = list(mydata)
mydata3 = []
for i in mydata2:
    a = list(i)
    mydata3.append(a)

# initializing tkinter
root = Tk()
# setting geometry
root.geometry("800x500")
root.resizable(False, False)
# setting title
root.title("Covid-19 ALL YOU NEED TO KNOW")
# setting image as a background
bg = PhotoImage(file="C:\Vaishnavi_old_laptop_backup_26_01_2022\Desktop\covid19\covid19.png")
# Show image using label
label = Label(root, image=bg)
label.place(x=0, y=0)


def abtvirus():
    root1 = Toplevel()
    root1.geometry("800x700")
    root1.title("ABOUT THE VIRUS")
    # Insert Image
    img = PhotoImage(file="C:\Vaishnavi_old_laptop_backup_26_01_2022\Desktop\covid19\monamask.png")
    label1 = Label(root1, image=img)
    label1.place(x=0, y=200)
    root1.resizable(False, False)
    text = Text(root1, height=15, width=100, bg="brown", fg="white", font="Consolas 11 bold")
    text.tag_configure("center", justify='center')
    text.pack()
    text.insert('1.0', """ABOUT THE VIRUS\nCoronavirus disease (COVID-19) is an infectious disease
caused by the SARS-CoV-2 virus. Most people infected with the virus will
experience mild to moderate respiratory illness and recover without requiring
special treatment. However, some will become seriously ill and require
medical attention.
Older people and those with underlying medical conditions like cardiovascular
disease, diabetes, chronic respiratory disease, or cancer are more likely to
develop serious illness. Anyone can get sick with COVID-19 and become seriously
ill or die at any age. The virus can spread from an infected person's mouth
or nose in small liquid particles when they cough, sneeze, speak, sing or
breathe.These particles range from larger respiratory droplets to smaller
aerosols. It is important to practice respiratory etiquette, for example by
coughing into a flexed elbow, and to stay home and
self-isolate until you recover if you feel unwell.""")
    text.tag_add("center", "0.5", "end")
    mainloop()


def symptoms():
    root3 = Toplevel()
    root3.geometry("800x550")
    root3.title("SYMPTOMS")
    root3.resizable(False, False)
    text = Text(root3, height=20, width=100, bg="white", fg="dark red", font="Consolas 11 bold")
    text.pack()
    text.insert('1.0', """SYMPTOMS\nCOVID-19 affects different people in different ways.
Most infected people will develop mild to moderate illness and recover without hospitalization.

Most common symptoms:
Fever, Cough, Tiredness, Loss of taste or smell.

Less common symptoms:
Sore throat, Headache, Aches and Pains, Diarrhoea, A rash on skin, or discolouration
of fingers or toes, Red or irritated eyes.

Serious symptoms:
Difficulty breathing or shortness of breath, Loss of speech or mobility, or confusion, Chest pain.

Seek immediate medical attention if you have serious symptoms. Always call before visiting your
doctor or health facility. People with mild symptoms who are otherwise healthy should manage their
symptoms at home.On average it takes 5–6 days from when someone is infected with the virus
for symptoms to show, however it can take up to 14 days.
""")
    text.tag_add("center", "0.5", "end")
    global img
    img = ImageTk.PhotoImage(file="C:\Vaishnavi_old_laptop_backup_26_01_2022\Desktop\covid19\symtops.jpg")
    panel = Label(root3, image=img).place(x=-3, y=330)


def precautions():
    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('PRECAUTIONS')
    global img
    img = ImageTk.PhotoImage(file="C:\Vaishnavi_old_laptop_backup_26_01_2022\Desktop\covid19\precautions.png")
    panel = Label(root2, image=img)
    panel.pack(side="bottom", fill="both")
    root2.resizable(False, False)
    text = Text(root2, height=23, width=75, bg="dark blue", fg="white", font="Consolas 11 bold")
    text.tag_configure("center", justify='center')
    text.pack()
    text.insert('1.0', """PRECAUTIONS\nTo prevent infection and to slow transmission of COVID-19,
do the following:
1. Get vaccinated when a vaccine is available to you.
2. Stay at least 1 metre apart from others,
even if they don’t appear to be sick.
3. Wear a properly fitted mask when physical distancing
is not possible or when in poorly ventilated settings.
4. Choose open, well-ventilated spaces over closed ones.
Open a window if indoors.
5. Wash your hands regularly with soap and water or clean
them with alcohol-based hand rub.
6. Cover your mouth and nose when coughing or sneezing.
7. If you feel unwell, stay home and self-isolate until you recover.
""")
    text.tag_add("center", "0.5", "end")


def analysis():
    root4 = Toplevel()
    root4.geometry("500x300")
    root4.resizable(False, False)
    global png
    png = PhotoImage(file="C:\Vaishnavi_old_laptop_backup_26_01_2022\Desktop\covid19\covid2.png")
    # Show image using label
    label1 = Label(root4, image=png)
    label1.place(x=0, y=0)
    root4.title("GET COVID-19 STATE WISE ANALYSIS")
    Label(root4, text="ENTER STATE NAME FOR\nCOVID-19 DATA", font="Consolas 15 bold", bg="red", fg="black").place(
        relx=0.26, rely=0.1, relwidth=0.50, relheight=0.2)
    Label(root4, text="NOTE:\n* If you want to see the data of multiple states\nplease enter them one after the other.",
          bg="red", fg="black").place(relx=0.26, rely=0.3, relwidth=0.50, relheight=0.2)
    global data
    data = StringVar()
    data.set("Enter State Name")
    entry = Entry(root4, textvariable=data, width=50).place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
    Button(root4, text="Get Data", bg="red", fg="white", command=showdata).place(relx=0.28, rely=0.7, relwidth=0.45,
                                                                                 relheight=0.1)


def showdata():
    # importing matplotlib which will be used to show data graphically
    from matplotlib import pyplot as plt
    # to scale the data we are importing patches
    import matplotlib.patches as mpatches
    # declaring empty lists to store different data sets
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    # using try and except to run program without errors
    try:
        # updating root
        root.update()
        # getting state name entered by the user
        global data
        states = data.get()
        # removing white spaces from the start and end of the string
        state_name = states.strip()
        # changing string to lower and capitalizing string
        state_name = state_name.lower()
        state_name = state_name.capitalize()
        # the state names are added to the list
        state_names = []
        state_names.append(state_name)
        # empty dictionary for cases
        d = {}
        # for loop to get one country data stored as dict in list cases
        for x in range(len(mydata3)):
            # appending states data one-by-one in cases list
            # the data will be stored as a dictionary
            for y in range(len(state_names)):
                if mydata3[x][1] == state_names[y]:
                    d['state_name'] = mydata[x][1]
                    d['confirmed'] = mydata[x][2]
                    d['active'] = mydata[x][3]
                    d['recovered'] = mydata[x][4]
                    d['deaths'] = mydata[x][5]
                    cases.append(d)
                    # updating the root
                    root.update()

        # for loop to get one state data stored as dict in list cases
        for y in cases:
            # storing every state's confirmed cases in the confirmed list
            confirmed.append(y["confirmed"])
            # storing every state's active cases in the active list
            active.append(y["active"])
            # storing every state's deaths cases in the deaths list
            deaths.append(y["deaths"])
            # storing every state's recovered cases in the recovered list
            recovered.append(y["recovered"])
        # marking the color information on scale using patches
        confirmed_patch = mpatches.Patch(color='green', label='confirmed')
        recovered_patch = mpatches.Patch(color='red', label='recovered')
        active_patch = mpatches.Patch(color='blue', label='active')
        deaths_patch = mpatches.Patch(color='black', label='deaths')
        # plotting the scale on graph using legend()
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
        # showing the data using graphs
        # this whole for loop section is related to matplotlib
        for x in range(len(state_names)):
            plt.bar(state_names[x], confirmed[x], color='green')
            if recovered[x] > active[x]:
                plt.bar(state_names[x], recovered[x], color='red')
                plt.bar(state_names[x], active[x], color='blue')
            else:
                plt.bar(state_names[x], active[x], color='blue')
                plt.bar(state_names[x], recovered[x], color='red')
            plt.bar(state_names[x], deaths[x], color='black')
        # setting the title of the graph
        plt.title('Current Covid Cases')
        # giving label to x direction of graph
        plt.xlabel('State Name')
        # giving label to y direction of graph
        plt.ylabel('Cases(in millions)')
        # showing the full graph
        plt.show()
        addlabels(x, y)
    except Exception as e:
        # asking user to enter correct details
        data.set('Enter correct details again')
    mainloop()    


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


headingFrame1 = Frame(root, bg="white", bd=5)
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
headingLabel = Label(headingFrame1, text="Welcome to\n COVID-19 ALL YOU NEED TO KNOW", bg='dark blue', fg='black',
                     font=('Courier bold', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
# adding buttons
btn1 = Button(root, text="ABOUT THE VIRUS", bg='dark blue', fg='white', font="Consolas 11 bold",
              command=abtvirus).place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
btn2 = Button(root, text="SYMPTOMS", bg='dark blue', fg='white', font="Consolas 11 bold", command=symptoms).place(
    relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
btn3 = Button(root, text="PRECAUTIONS", bg='dark blue', fg='white', font="Consolas 11 bold", command=precautions).place(
    relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
btn4 = Button(root, text="COVID-19 ANALYSIS", bg='dark blue', fg='white', font="Consolas 11 bold",
              command=analysis).place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)



