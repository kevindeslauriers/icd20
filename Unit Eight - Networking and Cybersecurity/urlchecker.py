from urllib.parse import urlparse

def print_url_components(url):
    # Parse the URL into its components
    parsed_url = urlparse(url)

    # Print the different components of the URL
    print("Scheme:", parsed_url.scheme)
    print("Netloc:", parsed_url.netloc)
    print("Path:", parsed_url.path)
    print("Params:", parsed_url.params)
    print("Query:", parsed_url.query)
    print("Fragment:", parsed_url.fragment)

# Get URL input from the user
url = input("Enter the URL: ")

# Print the components of the URL
print("\nURL Components:")
print_url_components(url)
