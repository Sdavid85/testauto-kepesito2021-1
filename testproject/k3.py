from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")
time.sleep(2)


def fill_field(title):
    title_field = driver.find_element_by_id("title")
    title_field.clear()
    time.sleep(1)
    title_field.send_keys(title)
    time.sleep(1)


error_message = driver.find_elements_by_xpath("/html/body/form/span")
inputs = ["abcd1234", "teszt233@", "abcd"]
messages = ["False", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]

# TC01: Helyes kitöltés esete:
#     * title: abcd1234
#     * Nincs validációs hibazüzenet


def test_tc01():
    fill_field(inputs[0])
    assert error_message.is_displayed == messages[0]


# TC02: Illegális karakterek esete:
#     * title: teszt233@
#     * Only a-z and 0-9 characters allewed.


def test_tc02():
    fill_field(inputs[1])
    assert error_message.get_attribute("value") == messages[1]

# TC03: Tul rövid bemenet esete:
#     * title: abcd
#     * Title should be at least 8 characters; you entered 4.


def test_tc03():
    fill_field(inputs[2])
    assert error_message.get_attribute("value") == messages[2]

# test_tc01()
# test_tc02()
# test_tc03()
# driver.close()
