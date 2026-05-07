from pyscript import document, display
import matplotlib.pyplot as plt
import numpy as np

attendance={
"Monday":0,
"Tuesday":0,
"Wednesday":0,
"Thursday":0,
"Friday":0
}

def add_data(event):
    day=document.getElementById("day").value
    absences=document.getElementById("absences").value

    if absences:
        attendance[day]=int(absences)
        draw_graph()

def reset_data(event):
    for day in attendance:
        attendance[day]=0
    draw_graph()

def draw_graph():
    plt.clf()
    plt.figure(figsize=(6,4))
    plt.plot(list(attendance.keys()),list(attendance.values()),marker='o')
    plt.title("Weekly Attendance")
    plt.grid(True)

    display(plt,target="plot",append=False)

draw_graph()