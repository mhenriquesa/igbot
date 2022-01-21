import time
from instabot.Config import FBBUSINESS
from commenter import driver, _go_to
from instabot.util.getvarnpaste import getvarnpaste
from instabot.util.get_next_post import next_post_files
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _waiting(xpath):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))  # nopep8


def trypost():

    _go_to(FBBUSINESS)
    time.sleep(10)

    create_story_button = _waiting("//div[text()='Criar story']")
    create_story_button.click()
    time.sleep(3)

    add_photos_button = _waiting("//div[text()='Adicionar mídia']")
    add_photos_button.click()
    time.sleep(5)

    getvarnpaste(next_post_files())
    time.sleep(2)

    share_button = _waiting("//div[text()='Compartilhar story']")
    share_button.click()
    time.sleep(10)
