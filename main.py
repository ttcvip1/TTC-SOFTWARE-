import requests

# Function to display a white banner
def display_banner():
    # Define ANSI escape codes for colors and reset
    WHITE = "\033[97m"
    RESET = "\033[0m"

    # ASCII art in white
    ascii_art = rf"""
    {WHITE}
 _______ _______  _____ 
|__   __|__   __|/ ____|
   | |     | |  | |    
   | |     | |  | |    
   | |     | |  | |____
   |_|     |_|   \_____|
   {RESET}
    """
    print(ascii_art)
    print(f"{WHITE}Welcome to the Signal Generator!{RESET}\n")

def login_system():
    # Hardcoded email and password (for demonstration purposes)
    stored_email = "titanictradingcommunity@gmail.com"
    stored_password = "@ttc"

    # Get user input for email and password
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    # Check if the email and password match
    if email == stored_email and password == stored_password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials, please try again.")
        return False

def gather_params():
    display_banner()  # Show banner before gathering inputs

    # Define green color for inputs
    GREEN = "\033[92m"
    RESET = "\033[0m"

    # Collect user inputs in green
    start_time = input(f"{GREEN}Enter start time (e.g., 09:00): {RESET}").strip()
    end_time = input(f"{GREEN}Enter end time (e.g., 18:00): {RESET}").strip()
    days = input(f"{GREEN}Enter number of days (e.g., 5): {RESET}").strip()
    pairs = input(f"{GREEN}Enter currency pairs (comma-separated, e.g., BRLUSD_otc,USDPKR_otc): {RESET}").strip()
    mode = input(f"{GREEN}Enter mode (e.g., blackout or normal): {RESET}").strip()
    min_percentage = input(f"{GREEN}Enter minimum percentage (e.g., 50 or 50+): {RESET}").strip()
    filter_value = input(f"{GREEN}Enter filter value (e.g., 1 or 2): {RESET}").strip()
    separate = input(f"{GREEN}Enter separate (e.g., 1): {RESET}").strip()

    params = {
        'start_time': start_time,
        'end_time': end_time,
        'days': days,
        'pairs': pairs,
        'mode': mode,
        'min_percentage': min_percentage,
        'filter': filter_value,
        'separate': separate
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    return params, headers

def send_request():
    # Define green color for output
    GREEN = "\033[92m"
    RESET = "\033[0m"

    url = "https://alltradingapi.com/signal_list_gen/qx_signal.js"
    params, headers = gather_params()
    
    print(f"\n{GREEN}Sending request to the server...{RESET}")
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        print(f"{GREEN}Request successful.{RESET}")
        try:
            data = response.json()
            print(f"{GREEN}Response Data:{RESET}")
            print(data)
        except ValueError:
            print(f"{GREEN}Response content is not in JSON format.{RESET}")
            print(response.text)
    else:
        print(f"{GREEN}Request failed with status code {response.status_code}{RESET}")
        print(response.text)

if __name__ == "__main__":
    if login_system():  # If login is successful
        send_request()
