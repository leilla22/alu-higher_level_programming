#!/usr/bin/python3
import urllib.request

def fetch_status(url):
    """
    Fetches the content from the given URL and prints it with a tab.

    Args:
        url (str): The URL to fetch.
    """
    try:
        # Use a with statement to ensure the response is properly closed
        with urllib.request.urlopen(url) as response:
            # Read the entire response body
            body = response.read().decode('utf-8')
            # Print each line of the body with a tab before it
            for line in body.splitlines():
                print(f"\t- {line}")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # The URL to fetch
    target_url = "https://alu-intranet.hbtn.io/status"
    print(f"Fetching status from: {target_url}")
    fetch_status(target_url)

