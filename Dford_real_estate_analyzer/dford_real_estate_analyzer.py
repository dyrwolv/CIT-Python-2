# Dakota Ford Real Estate Analyzer csv thing

import csv

CSV = "RealEstateData.csv"


def getDataInput(filename: str) -> list[list[str]]:
    """
    Reads the CSV file and returns a list of all records except the header row.
    """
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip the header
        data = list(csv_reader)
    return data

def getMedian(prices: list[float]) -> float:
    """
    Calculates the median of a sorted list of prices.
    """
    prices.sort()
    length = len(prices)
    mid_index = length // 2

    if length % 2 == 0:
        # If even, average the two middle elements
        return (prices[mid_index - 1] + prices[mid_index]) / 2.0
    else:
        # If odd, take the middle element
        return prices[mid_index]

def process_data(data):
    """
    Processes the data to calculate the required summaries.
    """
    prices: list[float] = []
    city_summary: dict[str, float] = {}
    zip_summary: dict[str, float] = {}
    property_type_summary: dict[str, float] = {}

    for record in data:
        city = record[1]
        zip_code = record[2]
        property_type = record[7]
        price = float(record[8])

        # Populate the main price list
        prices.append(price)

        # Update city summary
        if city in city_summary:
            city_summary[city] += price
        else:
            city_summary[city] = price

        # Update zip code summary
        if zip_code in zip_summary:
            zip_summary[zip_code] += price
        else:
            zip_summary[zip_code] = price

        # Update property type summary
        if property_type in property_type_summary:
            property_type_summary[property_type] += price
        else:
            property_type_summary[property_type] = price

    return prices, city_summary, zip_summary, property_type_summary



def display_summary(prices, city_summary, zip_summary, property_type_summary):
    """
    Calculates and displays the summaries: Min, Max, Total, Average, and Median.
    """
    # Ensure prices are sorted for median calculation
    prices.sort()

    # Calculate summary statistics
    min_price = min(prices)
    max_price = max(prices)
    total_price = sum(prices)
    average_price = total_price / len(prices)
    median_price = getMedian(prices)

    # Format values as currency with 2 decimal places
    print(f"Minimum Price: ${min_price:,.2f}")
    print(f"Maximum Price: ${max_price:,.2f}")
    print(f"Total Price: ${total_price:,.2f}")
    print(f"Average Price: ${average_price:,.2f}")
    print(f"Median Price: ${median_price:,.2f}")

    # Display city summary
    print("\nCity Summary:")
    for city, total in city_summary.items():
        print(f"{city}: ${total:,.2f}")

    # Display zip summary
    print("\nZip Code Summary:")
    for zip_code, total in zip_summary.items():
        print(f"{zip_code}: ${total:,.2f}")

    # Display property type summary
    print("\nProperty Type Summary:")
    for property_type, total in property_type_summary.items():
        print(f"{property_type}: ${total:,.2f}")


# the main loop
def maine():
    # Grab data
    data = getDataInput(CSV)

    # Process data and calculate summaries
    prices, city_summary, zip_summary, property_type_summary = process_data(data)

    # Display the summary information
    display_summary(prices, city_summary, zip_summary, property_type_summary)



if __name__ == "__main__":
    maine()