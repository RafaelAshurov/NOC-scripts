from tkinter.filedialog import askopenfilename
from helpers import printer
from helpers.get_substring_out_of_str_list import getSubstringOutOfStrList


def getIdsOutOfLogFile() -> None:
    """
    Gets a log file, separates it to list after every line break.
    Creates a txt file with all the ids writen in it.
    The file named the same as the imported log file with '.id' in the end.
    File location is the same as the log file location in your computer.
    """
    try:
        filename = askopenfilename()
        with open(filename, 'r') as data:
            logRowsList = data.read().split('\n')
            leftSide = input(f"Enter the string we need to match that {printer.underLine}after it{printer.end} the id begins (including spaces):")
            rightSide = input(f"Enter the string we need to match that {printer.underLine}before it{printer.end} the id ends (including spaces):")
            qIdsList = getSubstringOutOfStrList(logRowsList, leftSide, rightSide)

        with open(f"{filename}.ids.txt", "a+") as file:
            file.write(','.join(qIdsList))
    except Exception as error:
        print(f"{printer.fail} {error} {printer.end}")


getIdsOutOfLogFile()
