from itertools import permutations
from string import ascii_lowercase, digits
from itertools import permutations
from typing import Generator, List
from bs4 import BeautifulSoup
import cloudscraper
import random
import requests
import os.path
import uuid

scraper = cloudscraper.create_scraper()


def get_text_from_url(url: str) -> str:
    page = scraper.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    textarea = soup.select_one('textarea#text').string
    return str(textarea)


def generator_url() -> List[str]:
    return [str(i) for i in open(f"wordsbr.txt", "r")]


def build_urls() -> List[str]:
    prefix_url = "http://dontpad.com/"
    comb_array = [prefix_url + i for i in generator_url()]
    return comb_array


def have_password(text: str) -> bool:
    list_passwords = ["password", "passwords", "senha", "senhas"]
    for i in list_passwords:
        if i in text:
            return True


def download_text():
    urls = build_urls()

    asw = input(f"{len(urls)} urls geradas, começar? (Y/n)")
    if (asw not in ['y', 'Y', '']):
        exit(0)

    for url in urls:
        name = url.split("/")[3]
        try:
            if str(get_text_from_url(url)) != "None" and have_password(get_text_from_url(url)):
                txt = open(f"senhas/{name}.txt", "a")
                txt.write(get_text_from_url(url))
                txt.close()
                print('\033[32m' + "DEU BOM" + '\033[0;0m')
                print(f"A url : {url} tinha uma senha")

            else:
                print('\033[31m' + "DEU RUIM" + '\033[0;0m')
                print(url)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    download_text()
