import subprocess

# WebDriver Manager is required to install the web drivers based on the version of your web browser.
# The Selenium library is used for automating tasks.

packages = ['selenium','webdriver-manager','pandas']

# run
for package in packages:
    subprocess.check_call(["pip", "install", package])
