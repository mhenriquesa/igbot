import time
from getvarnpaste import getvarnpaste
from ig_post_manager import next_post_files
from selenium.webdriver.common.by import By
from Robot import driver, _type_like_a_person, _go_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _waiting(xpath):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, xpath)))


def trypost():

    _go_to("https://business.facebook.com/latest/posts/published_posts?asset_id=105349341511172&business_id=502990630698560&nav_ref=bm_home_redirect")
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
    time.sleep(20)


trypost()
