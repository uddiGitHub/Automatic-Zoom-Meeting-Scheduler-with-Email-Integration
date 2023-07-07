import subprocess

# pyautogui require for keyboad and mouse inputs
# webdriver-manager require to install the web drivers based on the version your web-browser
# selenium library that's use for automate task

packages = ['pyautogui','selenium','webdriver-manager']

# run
for package in packages:
    subprocess.check_call(["pip", "install", package])
