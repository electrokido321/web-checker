import requests

def check_website(url, index):
    try:
        # Add http:// or https:// prefix if not already present
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url  # Default to HTTPS

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return f"Website {index}: '{url}' is online."
        else:
            return f"Website {index}: '{url}' returned status code {response.status_code}."
    except requests.RequestException as e:
        return f"Website {index}: '{url}' is not reachable. Error: {e}"

def main():
    results = []
    with open('websites.txt', 'r') as file:
        websites = file.read().splitlines()

    for i, website in enumerate(websites, 1):
        result = check_website(website, i)
        results.append(result)
    
    # Write results to a file
    with open('ON.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

    print("Website status check completed. Results saved to 'website_status.txt'.")

if __name__ == "__main__":
    main()
