import subprocess

# PyAutoGUI is required for keyboard and mouse inputs.
# WebDriver Manager is required to install the web drivers based on the version of your web browser.
# The Selenium library is used for automating tasks.

packages = ['pyautogui','selenium','webdriver-manager']

# run
for package in packages:
    subprocess.check_call(["pip", "install", package])
