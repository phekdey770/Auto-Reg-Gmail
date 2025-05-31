# driver_config.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

class DriverConfig:
    def __init__(self, driver_path: str, user_agent: str, window_size: tuple, app_url: str):
        self.driver_path = driver_path
        self.user_agent = user_agent
        self.window_size = window_size
        self.app_url = app_url
    
    def create_driver(self, window_position: tuple) -> WebDriver:
        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={self.user_agent}")
        chrome_options.add_argument(f"--window-size={self.window_size[0]},{self.window_size[1]}")
        chrome_options.add_argument(f"--window-position={window_position[0]},{window_position[1]}")
        chrome_options.add_argument(f"--app={self.app_url}")
        
        service = Service(self.driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
