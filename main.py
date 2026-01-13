import requests

baseurl = "https://verkehr.autobahn.de/o/autobahn"


def main():
    r = requests.get(baseurl, timeout=20)
    r.raise_for_status()

    allroadsdict = r.json()
    allroadslist = allroadsdict['roads']
    print(allroadslist)


    for roadid in allroadslist:
        r = requests.get(f"https://verkehr.autobahn.de/o/autobahn/{roadid}/services/roadworks")
        r.raise_for_status()

        allroadworksdict = r.json()
        for i in range(len(allroadworksdict)):
            print(allroadworksdict['roadworks'][i]['title'])
            print(allroadworksdict['roadworks'][i]['description'])


    for roadid in allroadslist:
            r = requests.get(f"https://verkehr.autobahn.de/o/autobahn/{roadid}/services/parking_lorry")
            r.raise_for_status()

            allparkinglorriesdict = r.json()
            print(allparkinglorriesdict)
                

    for roadid in allroadslist:
            r = requests.get(f"https://verkehr.autobahn.de/o/autobahn/{roadid}/services/warning")
            r.raise_for_status()

            allwarningsdict = r.json()
            print(allwarningsdict)
                
    for roadid in allroadslist:
            r = requests.get(f"https://verkehr.autobahn.de/o/autobahn/{roadid}/services/closure")
            r.raise_for_status()

            allclosuredict = r.json()
            print(allclosuredict)

    for roadid in allroadslist:
            r = requests.get(f"https://verkehr.autobahn.de/o/autobahn/{roadid}/services/electric_charging_station")
            r.raise_for_status()

            chargingstationdict = r.json()
            print(chargingstationdict)
            
            
            

if __name__ == "__main__":
    main()
