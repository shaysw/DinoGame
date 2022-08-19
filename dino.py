from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image
import io

X_SCAN_RANGE = 550
X_SCAN_START = 750

Y_SCAN_RANGE = 20
Y_SCAN_START = 570

def should_jump():    
    screenshot_as_png = driver.get_screenshot_as_png() 
    screenshot_as_bytes = io.BytesIO(screenshot_as_png)
    screenshot_as_bytes.seek(0)
    screenshot_as_bytes = io.BytesIO(screenshot_as_bytes.read())

    screenshot_image = Image.open(screenshot_as_bytes)
    screenshot_image_as_rgb = screenshot_image.convert('RGB')
    
    for x in range(X_SCAN_RANGE):
        for y in range(Y_SCAN_RANGE):
            r, g, b = screenshot_image_as_rgb.getpixel((X_SCAN_START - x * 1, Y_SCAN_START - y * 1))
            if r != 255 or g != 255 or b != 255:
                return True          

    return False


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    try:
        driver.get("chrome://dino/")
    except:
        pass

    element = driver.find_element(By.TAG_NAME, "body")
    element.send_keys(Keys.SPACE)

    while 1:
        if should_jump():        
            element.send_keys(Keys.SPACE)

