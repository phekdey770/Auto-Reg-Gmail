# main.py

import time
from driver_config import DriverConfig
from chrome_actions import ChromeActions

class Main:
    def __init__(self, driver_config: DriverConfig, target_open: int, delay_between_windows: int):
        self.driver_config = driver_config
        self.target_open = target_open
        self.delay_between_windows = delay_between_windows
    
    def run(self):
        drivers = []
        for i in range(self.target_open):
            window_position = (i * self.driver_config.window_size[0], 0)
            driver = self.driver_config.create_driver(window_position)
            chrome_action = ChromeActions(driver)
            drivers.append(chrome_action)
            
            # Call the perform_action method after initializing the ChromeActions instance
            chrome_action.perform_action()
            
            if i < self.target_open - 1:
                time.sleep(self.delay_between_windows)
        
        input("Press Enter to close all browsers...")
        
        for action in drivers:
            action.close_browser()


if __name__ == "__main__":
    CHROMEDRIVER_PATH = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    MOBILE_USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    WINDOW_SIZE = (310, 740)
    
    APP_URL = "https://www.google.com/gmail/about/"
    TARGET_OPEN = 1
    DELAY_BETWEEN_WINDOWS = 3
    
    driver_config = DriverConfig(CHROMEDRIVER_PATH, MOBILE_USER_AGENT, WINDOW_SIZE, APP_URL)
    main = Main(driver_config, TARGET_OPEN, DELAY_BETWEEN_WINDOWS)
    main.run()
