import re
import time
import random
from selenium import webdriver
from getvarnpaste import getvarnpaste
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox(executable_path='D:\Programas\geckodriver.exe')
driver = webdriver.Chrome(executable_path='D:\Programas\chromedriver.exe')


def _type_like_a_person(sentence, single_input_field):
    print("going to start typing message into message share text area")
    for letter in sentence:
        single_input_field.send_keys(letter)
        time.sleep(random.randint(1, 6) / 30)


def _waiting(xpath):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, xpath)))


def _scroll_page():
    for i in range(1, 3):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")


def _filter_of_post_links(links):
    reg = re.compile(r'https://www\.instagram\.com\/p\/')
    link_list = list(filter(reg.search, links))
    return link_list


def _get_posts_links():
    a_found = driver.find_elements_by_tag_name("a")
    a_hrefs = [elem.get_attribute("href") for elem in a_found]
    post_links = _filter_of_post_links(a_hrefs)
    return post_links


def _go_to(url, hashtag=None):
    if hashtag:
        driver.get(url + hashtag)
        time.sleep(3)
        return
    driver.get(url)
    time.sleep(3)


def comment_on_hashtags():
    hashtag = ["modapraia2021", "advogadasestilosas",
               "biquinis", "vestidoscurtos", "sandaliasplanas"]

    _go_to("https://www.instagram.com/explore/tags/", random.choice(hashtag))
    time.sleep(10)
    _scroll_page()
    hashtag_post_links = _get_posts_links()
    visited_links = []
    # comments_options = ['Lindo! amei!', 'Adorei', 'Merece um like !']
    comments_options = ["😁", "👏👏👏", "❣️❣️", "👏",
                        "❣️❣️❣️", "gostei! 😁", "ganhou meu like!👏"]

    for link in hashtag_post_links[:random.randint(5, 8)]:
        if link in visited_links:
            continue
        _go_to(link)
        time.sleep(random.randint(3, 7))
        comment_area = driver.find_element_by_class_name("Ypffh")
        if not comment_area:
            continue
        _type_like_a_person(random.choice(comments_options), comment_area)
        time.sleep(random.randint(4, 8))


def login(username, password):

    _go_to('https://instagram.com')

    pass_field = driver.find_element_by_xpath('//input[@name="password"]')
    user_field = driver.find_element_by_xpath('//input[@name="username"]')

    user_field.click()
    _type_like_a_person(username, user_field)
    pass_field.click()
    _type_like_a_person(password, pass_field)
    time.sleep(1)
    pass_field.send_keys(Keys.RETURN)


def trypost():
    # find plus sign
    plussign = _waiting("//*[@aria-label='New Post']")
    plussign.click()
    time.sleep(3)

    addbtn = _waiting(r"//*/button[text()='Select from computer']")
    addbtn.click()
    time.sleep(5)

    getvarnpaste(r"D:\images\02_54542_fewfew.jpg")
    time.sleep(2)

    nextbtn = _waiting("//button[text()='Next']")
    nextbtn.click()

    nextbtn = _waiting("//button[text()='Next']")
    nextbtn.click()

    textarea = _waiting("//*/textarea[@aria-label='Write a caption...']")

    _type_like_a_person("teste 123", textarea)

    time.sleep(60)


login("segredosdaslojas", "Mh3226572")
trypost()

input("Click")

# ---------------------------------------
# t_end = time.time() + 60 * 4

# while time.time() < t_end:
#     comment_on_hashtags()
