import requests

url = "https://verkehr.autobahn.de/o/autobahn"


def main():
    r = requests.get(url, timeout=20)
    r.raise_for_status()

    allroadsdict = r.json()
    print(allroadsdict)

if __name__ == "__main__":
    main()
