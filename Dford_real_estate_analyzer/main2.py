# Dakota Ford Real Estate Analyzer csv thing

import csv

CSV = "RealEstateData.csv"

class RealEstateAnalyzer:
    def __init__(self, filename: str):
        self.data = self.getDataInput(filename)
        self.prices: list[float] = []
        self.city_summary: dict[str, float] = {}
        self.property_summary: dict[str, float] = {}
        self.zip_summary: dict[str, float] = {}


    def getDataInput(self, filename: str) -> list[list[str]]:
        """
        this function should return all the records in a list
        Remember the first record is the fields/columns heading so this record should not be processed.
        """

        # opens the csv file
        with open(filename, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # skip the header
            data = list(csv_reader)
        # Returns our csv data
        return data

    def getMedian(self, prices: list[float]) -> float:
        # we need to do some math magic here...

        prices.sort()
        length = len(prices) # get the length of the list
        mid_index = length // 2 # find the middle of the list

        if length % 2 == 0:

            # if its an even number of items, take the average of the two middle elements
            return (prices[mid_index - 1] + prices[mid_index] ) / 2.0
        else:
            # if its an odd number, just get the middle value
            return prices[mid_index]


    def process_data(self):
        #Processes the input data to populate the price lists and summaries

        for record in self.data:
            city = record[1]
            property = record[7]

    def display_summary(self):

        pass


def the_loop(analyzer):
    # do loop stuffs

    print(analyzer.data)

    pass


# the main loop
def maine():
    print("entered maine")
    analyzer = RealEstateAnalyzer(CSV)
    the_loop(analyzer)



if __name__ == "__main__":
    maine()