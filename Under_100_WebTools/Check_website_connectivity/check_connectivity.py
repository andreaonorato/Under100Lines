import csv
import requests

# Dictionary to store website status
status_dict = {"Website": "Status"}


def main():
    # Open the file containing website URLs
    with open("websites.txt", "r") as fr:
        # Iterate over each line in the file
        for line in fr:
            # Extract website URL from each line
            website = line.strip()
            # Get the status code of the website
            status = requests.get(website).status_code
            # Update the status dictionary based on the status code
            status_dict[website] = "working" if status == 200 else "not working"

    # Write the status dictionary to a CSV file
    with open("website_status.csv", "w", newline="") as fw:
        # Create a CSV writer object
        csv_writer = csv.writer(fw)
        # Write headers to the CSV file
        csv_writer.writerow(["Website", "Status"])
        # Write website status data to the CSV file
        for key in status_dict.keys():
            csv_writer.writerow([key, status_dict[key]])


if __name__ == "__main__":
    # Execute the main function
    main()
