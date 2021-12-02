import re
from helpers import printer


def getSubstringOutOfStrList(logList: list, leftIndicator: str, rightIndicator: str) -> list:
    """
    Searches for the substring at every item from the given list according the indicators
    :param list logList: A list of all the log file split by rows '\n'
    :param str leftIndicator: The string it needs to match that after that string the required substring begins
    :param str rightIndicator: The string it needs to match that before that string the required substring ends
    :return list substringsList: A list with the substring matched at each row
    """
    substringsList = []
    for i, row in enumerate(logList):
        substring = re.search(f'{leftIndicator}(.+?){rightIndicator}', row)
        if substring:
            substring = substring.group(1)
            if substring not in substringsList:
                substringsList.append(substring)
        else:
            print(f"Line[{i}/{len(logList)-1}] {printer.warning}No math for '{leftIndicator}' or '{rightIndicator}' in that row.{printer.end}")
    return substringsList
