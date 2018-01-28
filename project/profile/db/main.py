"""
Main File
Imported all the function from separate files.
Also provided test cases and type contract
"""

from .Connector import Connection
from .snew.Generator import Hasher


def guessLocation(userID):
    '''
    :param userID: userID of user who's location is being updated
    :return: top 5 choices
    '''
    conn = Connection("18.216.32.253", "root", "password", "test")
    past_choices = conn.query("Frequency", "location", conditions=["userID = {}".format(userID)], order=["frequency", "DESC"])
    return past_choices[:min(5,len(past_choices))]
