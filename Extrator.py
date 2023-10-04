import re
import argparse

print("""
⣿⣿⣿THE DISECTOR EMAIL/ONLY VERSION⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣁⣤⡶⠶⠶⠶⢶⣤⣈⠙⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣴⠟⠋⠀⠀⠀⠀⠀⢀⠀⠉⠳⣆⠈⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣄⠘⣧⠈⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣷⣿⡆⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⣤⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⣿⡀⢹⣷⣤⣄⣠⣤⣶⣿⣿⣿⣿⣿⣿⠁⣼⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⢿⣄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣼⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⣀⠙⠻⣿⣿⣿⣿⣿⣿⣿⠿⠋⣠⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠙⣿⣿⣷⣶⣤⣬⣍⣉⣩⣥⣴⣶⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠟⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠻⣷⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿OMZO⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

def fetcher(data):
    pack = []
    try:
        file = open(data)
        for line in file:
            line = line.strip()
            emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line)
            if len(emails) >= 1:
                i = 0
                while i < len(emails):
                    pack.append(emails[i])
                    i += 1
            else:
                pack.append(emails)
        writer(pack)
    except FileNotFoundError:
        print("make sure you are using the right path!")


def writer(data):
    file = open("result.txt", "w")
    for item in data:
        file.write(item + '\n')


def main():
    parser = argparse.ArgumentParser(description='Extract email addresses from a file.')

    parser.add_argument('-p', '--path', required=False, help='Path to the input file')

    args = parser.parse_args()

    file_path = args.path

    if file_path:
        fetcher(file_path)
    else:
        print("No file path specified. Use '-f' to specify the file path.")


if __name__ == "__main__":
    main()
