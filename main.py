import requests

def check_website(url):
    try:
        # Add http:// or https:// prefix if not already present
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url  # Default to HTTPS

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return f"'{url}' is online."
        else:
            return f"'{url}' returned status code {response.status_code}."
    except requests.RequestException as e:
        return f"'{url}' is not reachable. Error: {e}"

def main():
    results = []
    with open('websites.txt', 'r') as file:
        websites = file.read().splitlines()

    for website in websites:
        result = check_website(website)
        results.append(result)
    
    # Write results to a file
    with open('ON.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

    print("Website status check completed. Results saved to 'ON.txt'.")

if __name__ == "__main__":
    main()
  
