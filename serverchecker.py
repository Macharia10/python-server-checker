import socket

def is_running(site):
    """the fuction attempt to connect to any given server using socket, return: whether or not it was able to connect to the server."""

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True

    except:
        return False

if __name__ == "__main__":
    while True:
        site = input('website to check: ')
        if is_running(f"{site}.com"):
            print(f"{site}.com is running.")

        else:
            print(f'There is a problemm with {site}.com!')

        if input("Would you like to check another website(Y/N)? ") in {'n', 'N'}:
            break