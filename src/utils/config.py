
import os

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
BROWSER  = os.getenv("BROWSER", "chrome").lower()  # chrome | firefox
HEADLESS = os.getenv("HEADLESS", "0") in ("1", "true", "yes")
CI       = os.getenv("CI", "false").lower() in ("1", "true", "yes")
