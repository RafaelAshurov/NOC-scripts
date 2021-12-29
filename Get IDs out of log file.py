from tkinter.filedialog import askopenfilename
from helpers.get_substring_out_of_str_list import getSubstringOutOfStrList
import tkinter as tk
from tkinter import simpledialog
from helpers import printer
from datetime import datetime

def getIdsOutOfLogFile() -> None:
    """
    Gets a log file, separates it to list after every line break.
    Creates a txt file with all the ids writen in it.
    The file named the same as the imported log file with '.id' in the end.
    File location is the same as the log file location in your computer.
    """
    try:
        ROOT = tk.Tk()
        ROOT.withdraw()
        leftSide = simpledialog.askstring(title="Left delimiter", prompt="Enter the string we need to match that after it "
                                                               "the id begins (including spaces):")
        rightSide = simpledialog.askstring(title="Right delimiter", prompt="Enter the string we need to match that before it "
                                                                "the id ends (including spaces):")
        dateTimeString = simpledialog.askstring(title="Date and time", prompt="Enter date and time (DD-MM-YYYY HH:MM:SS):")
        dateTime = datetime.fromisoformat(dateTimeString)
        print(dateTime)
        filename = askopenfilename()
        with open(filename, 'r') as data:
            logRowsList = data.read().split('\n')
            qIdsList = getSubstringOutOfStrList(logRowsList, leftSide, rightSide)

        with open(f"{filename}.ids.txt", "a+") as file:
            print(len(qIdsList))
            file.write(','.join(qIdsList))
    except Exception as error:
        print(f"{printer.fail} {error} {printer.end}")


getIdsOutOfLogFile()
