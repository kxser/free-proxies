import requests, json, random, colorama
from configuration import *
##This file contains the code to get fresh proxies that are relatively fast.





urls =  [
    "https://api.oproxy.ml/servers?proto=http&sort=speed_score&page=0",
    "https://api.oproxy.ml/servers?proto=http&sort=speed_score&page=1",
    "https://api.oproxy.ml/servers?proto=http&sort=speed_score&page=2",
]

def get_proxies():
    global checked_proxies
    checked_proxies = []
    for i in range(len(urls)):
        print(f"""            
-----------------------------------------------------------------------
{colorama.Fore.RED}Getting proxies from page: {i+1}{colorama.Fore.RESET}
-----------------------------------------------------------------------
        """)
        response = requests.get(urls[i]).json()
        for x in range(25):
            try:
                proxy_element = response["servers"][x]["url"].replace("https://", "").replace("http://", "")
                if "socks" in proxy_element:
                    if config["remove_socks"] == True:
                        pass
                elif response["servers"][x]["speed_score"] < config["speed_threshold"]:
                    print(f"{colorama.Fore.BLUE}Proxy found however it did not pass speed threshold.{colorama.Fore.RESET}")
                    pass
                else:
                    checked_proxies.append(proxy_element)
                    print(f"{colorama.Fore.BLUE}Proxy found: {proxy_element}{colorama.Fore.RESET}")
            except Exception:
                break


