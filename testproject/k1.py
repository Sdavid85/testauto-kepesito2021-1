import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")
time.sleep(2)

def inputs(a, b):
    a_input = driver.find_element_by_id('a')
    b_input = driver.find_element_by_id('b')
    calc_btn = driver.find_element_by_id('submit')
    a_input.clear()
    b_input.clear()
    time.sleep(1)
    a_input.send_keys(a)
    b_input.send_keys(b)
    calc_btn.click()
    time.sleep(2)

result = driver.find_element_by_id('result')
a_inputs = ["", "2", ""]
b_inputs = ["", "3", ""]
results = ["False", "10", "NaN"]

# TC01: Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <nem látszik

def test_tc01():
    a_input = ()
    b_input = ()
    assert a_input.text == a_inputs[0]
    assert b_input.text == b_inputs[0]
    assert result.is_displayed == results[0]

# TC02: Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10

def test_tc02():
    inputs(a_inputs[1], b_inputs[1])
    assert result.text == results[1]

# TC03: Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: NaN

def test_tc03():
    inputs(a_inputs[2], b_inputs[2])
    assert result.text == results[2]

# test_tc01()
# test_tc02()
# test_tc03()
# driver.close()
