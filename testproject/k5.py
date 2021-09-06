from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")
time.sleep(2)


init_btn = driver.find_element_by_id("init")
play_btn = driver.find_element_by_id("spin")
results = ["25", "75"]

# TC01: * Az applikáció helyesen megjelenik:
#     * A bingo tábla 25 darab cellát tartalmaz
#     * A számlista 75 számot tartalmaz


def test_tc01():
    table_numbers = driver.find_elements_by_name("number")
    assert len(table_numbers) == int(results[0])
    numbers = driver.find_elements_by_xpath('//*[@id="numbers-list"]/li')
    assert len(numbers) == int(results[1])

# TC02:  Bingo számok ellenőzrzése:
#     * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
#     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már
#     kihúzott számok közül kerültek-e ki



# TC03: * Új játékot tudunk indítani
#     * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#     * új bingo szelvényt kapunk más számokkal.

