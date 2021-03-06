"""
SpamX

A tool that serves the feature of instagram direct messages spamming. In other words, it sends a mass amount of messages to a requested user over your instagram account. The tool is written using python3 programming language. The tool uses various external libraries, they are listed in the dependencies list.
Dependencies :
1. selenium - external python library to control the browser's action.
2. webdriver-manager - external python library to work with the webdriver. In our case we are using the chrome browser.
3. pyautogui - A python's library to control and automate the GUI tasks including keyboard manipulation, mouse cursor manipulation, etc.
To properly set up this tool on your local machine, check out the guide in README.md file of this project. The mirror of the repository of this project is available at https://github.com/Mr-Internetix/SpamX/

Author : Ajit Yadav (https://github.com/Mr-Internetix/)
Created on : Decemeber 4, 2020

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 12, 2021

Changes made in the last modification :
1. Updating the minor error in the process of the validation of the username entered by the user. The usernames of an instagram account usually contains special characters like '_' and '.', but the if..else conditional statements that were for validating the user entered instagram usernames. Thus we removed the checking of the alphanumeric condition for the user enterted usernames. Thus, resolved the issue.

Authors contributed to this script (Add your name below if you have contributed) :
1. Ajit Yadav (github:https://github.com/Mr-Internetix/)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
    from time import sleep
    from getpass import getpass
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui
except Exception as e:
    # If there are any errors encountered during the importing of the required modules, then we display the error on the console screen and exit the script

    input(f'[ Error : {e} ]\nPress enter key to continue...')
    exit()

def InstagramLogin(username, password, victimUsername ):
    """ The function to login to the instagram website using the user provided credentials. The function requires two arguments : username, password, victimUsername. The function also loads the message conversation of the target user. Each of the tasks here are executed using the selenium and chrome driver, thus there are dependencies required for this function to execute properly. Also, for each of the tasks (wheter entering data, or switching pages), the web browser takes certain amount of time to load the pages properly, that is why we are using sleep function in the time module in order to wait properly before proceeding to the next task. """

    # Opening instagram website on the web browser
    driver.get('https://www.instagram.com/')
    sleep(2)

    # Entering the specified username and password into the input boxes of the login page
    driver.find_element_by_name('username').send_keys(username)
    sleep(1)
    driver.find_element_by_name('password').send_keys(password)

    # Pressing the login button on the web page and then saving the password into the browser / cache
    driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
    sleep(5)
    driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
    sleep(5)
    driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
    sleep(5)

    # Finding the requested user using the search bar and entering the specified victimUsername
    driver.find_element_by_xpath('//input[@type="text"]').send_keys(victimUsername)
    sleep(2)
    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(3)
    driver.find_element_by_css_selector('button.sqdOP.L3NKy._8A5w5').click()

def main():
    # Giving global access to some variables defined inside this function
    global driver

    # Displaying the heading of the tool on the console screen
    print('%s[ SpamX ]%s' %('=' * 20, '=' * 20))

    # Asking the user for the required information
    username = input('Enter your instagram username : ')
    password = getpass('Enter your instagram password : ')
    victimUsername = input('Enter the username of the victim : ')
    text = input('Enter the message to be send : ')
    count  = int(input('Enter the amount of messages to be send : '))

    # Validating the user entered information
    if len(username) < 4:
        # If the user entered username is less than 4 characters, then we display the error message on the console screen

        input(f'[ Error : Please enter a valid instagram username ]\nPress enter key to continue...')
    else:
        # If the user entered username is valid, then we continue

        if len(password) < 5:
            # If the user entered password is less than 5 characters, then we display the error message on the console screen

            input(f'[ Error : Please enter a valid password ]\nPress enter key to continue...')
        else:
            # If the user entered password is valid, then we continue

            if len(victimUsername) < 4:
                # If the user entered username of the victim is less than 4 characters, then we display the error message on the console screen

                input(f'[ Error : Please enter a valid instagram username of the victim ]\nPress enter key to continue...')
            else:
                # If the user entered username of the victim is valid, then we continue

                if count <= 0:
                    # If the user entered amount of messages is less or equal to 0, then we display the error message on the console screen

                    input(f'[ Error : Please enter the amount of atleast 1 message to be sent ]\nPress enter key to continue...')
                else:
                    # If the user entered amount of messages is more than 0, then we continue

                    # Initiliazing the selenium web driver with our script, to control the chrome web browser
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    driver.maximize_window()

                    # Calling the function to login into the user's instagram account with the provided credentials
                    InstagramLogin(username, password , victimUsername)

                    # Sending the message in a loop for the user specified amount of times
                    for i in range(count):
                        pyautogui.typewrite(text)
                        pyautogui.press("enter")
                        sleep(1)
                    driver.quit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script

        exit()
    except Exception as e:
        # If there are any errors encountered during the process, then we display the error on the console screen

        input(f'[ Error : {e} ]\nPress enter key to continue...')
        exit()
