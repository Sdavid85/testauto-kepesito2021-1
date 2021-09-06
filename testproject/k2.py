import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
time.sleep(2)

random_color_name = driver.find_element_by_id("randomColorName")
random_color = driver.find_element_by_id("randomColor")
test_color_name = driver.find_element_by_id("testColorName")
test_color = driver.find_element_by_id("testColor")
start_btn = driver.find_element_by_id("start")
stop_btn = driver.find_element_by_id("stop")
all_colors = ["IndianRed", "Pink", "HotPink", "Coral", "OrangeRed", "DarkOrange", "Yellow", "DarkKhaki", "Violet",
             "MediumOrchid", "DarkMagenta", "Chartreuse", "MediumSpringGreen", "DarkGreen", "DarkCyan", "Turquoise",
             "RoyalBlue", "NavajoWhite", "SaddleBrown", "Gray", "Black", "AliceBlue", "OldLace", "Chocolate"]

def result():
    return driver.find_element_by_id('result').text

# TC01: Helyesen jelenik meg az applikáció betöltéskor:
#     * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#     <szín neve> [     ] == [     ]


def test_tc01():
    assert random_color_name.text in all_colors
    assert test_color_name.is_displayed() == "False"


# TC02: * El lehet indítani a játékot a `start` gommbal.
#     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.


def test_tc02():
    assert start_btn.is_enabled()
    start_btn.click()
    time.sleep(2)
    assert stop_btn.is_enabled()
    stop_btn.click()
    time.sleep(2)


# TC03 Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
#     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
#       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.

messages = ["Correct!", "Incorrect!"]


def test_tc03():
    start_btn.click()
    time.sleep(2)
    stop_btn.click()
    time.sleep(2)
    result_message = result()
    if random_color_name.text == test_color_name.text:
        assert result_message == messages[0]
    else:
        assert result_message == messages[1]

    driver.close()
