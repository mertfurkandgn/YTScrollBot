from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def scroll_to_bottom(driver, pause=2):
    """
    Scrolls to the bottom of the page and waits for new content to load.
    
    Args:
        driver: Selenium WebDriver instance
        pause (int): Time to wait between scrolls in seconds
    """
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(pause)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            print("Reached the bottom of the page.")
            break
        last_height = new_height

def main():
    """Main function to automate scrolling through YouTube liked videos."""
    options = Options()
    options.debugger_address = "127.0.0.1:9222"

    driver = webdriver.Chrome(options=options)
    url = "https://www.youtube.com/playlist?list=LL"

    driver.get(url)
    time.sleep(3)  # Wait for page load
    scroll_to_bottom(driver)
    print("Scrolling complete.")

if __name__ == "__main__":
    main()
