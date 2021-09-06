from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
time.sleep(2)
chr_data = driver.find_element_by_id("chr")
op_data = driver.find_element_by_id("op")
num_data = driver.find_element_by_id("num")
submit_btn = driver.find_element_by_id("submit")


def assemble_expression(*args):
    return "{}{}{}".format(*args)

# TC01: * Helyesen betöltődik az applikáció:
#     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

inputs = driver.find_element_by_xpath("/html/body/div/div/p[3]")

# Nem tudom aposztrófok közé tenni tenni a karaktereket, mert a szövegben is vannak aposztrófok
# def test_tc01():
#   ascii_table = "!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
#   assert inputs.text == ascii_table

# TC02: Megjelenik egy érvényes művelet:
#     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     * `op` mező vagy + vagy - karaktert tartlamaz
#     * `num` mező egy egész számot tartalamaz


# TC03: * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
#     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
#     * A `num` mezőben megjelenő mennyiségű karaktert
#     * az `result` mező helyes karaktert fog mutatni


def test_tc03():
    submit_btn.click()
    result_text = driver.find_element_by_id("result")
    ex = assemble_expression(chr_data.text, op_data.text, num_data.text)
    assert eval(ex) == result_text.text