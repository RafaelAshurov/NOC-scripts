from tkinter.filedialog import askopenfilename
import re


def getSubstringOutOfLogList(logList: list, leftIndicator: str, rightIndicator: str) -> list:
    """
    Searches for the substring at every item from the given list according the indicators
    :param list logList: A list of all the log file split by rows '\n'
    :param str leftIndicator: The string it needs to match that after that string the required substring begins
    :param str rightIndicator: The string it needs to match that before that string the required substring ends
    :return list substringsList: A list with the substring matched at each row
    """
    substringsList = []
    for row in logList:
        substring = re.search(f'{leftIndicator}(.+?){rightIndicator}', row)
        if substring:
            substring = substring.group(1)
            if substring not in substringsList:
                substringsList.append(substring)
    return substringsList


def main() -> None:
    """
    Gets a log file, separates it to list after every line break.
    Creates a txt file named the same as the imported log file with '.id' in the end.
    File location is the same as the log file location in your computer.
    with all the ids writen in it.
    """
    filename = askopenfilename()
    with open(filename, 'r') as data:
        logRowsList = data.read().split('\n')
        leftSide = input("Enter the string we need to match that after that string the required substring begins:")
        rightSide = input("Enter the string we need to match that before that string the required substring ends:")
        qIdsList = getSubstringOutOfLogList(logRowsList, leftSide, rightSide)

    with open(f"{filename}.ids.txt", "a+") as file:
        file.write(','.join(qIdsList))


main()
