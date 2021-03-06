## DEFINING VARIABLES AND FUNCTIONS

datafile_name = "datafile.csv"  # standardised variable to refer to our csv datafile in our code
datafile_reader = open("datafile.csv", "r")

## ----------------------------------------------------------
## List of variables or class

datalist = datafile_reader.readlines()
instruments_universe = []


class Instrument:
    def __init__(self, isin, assetclass, region):
        self.isin = isin


## ----------------------------------------------------------
## List of functions

def search_instrument():
    instrument = input("Search instrument: ").strip().upper()
    while instrument not in instruments_universe:
        print("Instrument not found.")
        instrument = input("Search instrument: ").strip().upper()
    return instrument


def display_instrument(instrument):
    print()


def search_magnitude(instrument):
    magnitude = float(
        input("Search for past instances when {}'s price increased by ____ % in one day: ".format(instrument)))
    past_similar_events = []


## ----------------------------------------------------------
## Actual algorithm

instrument = search_instrument()
display_instrument(instrument)
search_magnitude(instrument)

## ----------------------------------------------------------
## closing datafile, all codes to be written above this line.
datafile_reader.close()
