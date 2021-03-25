# Python requests package
# Let's connect to live web
# We will connect to www.bbc.co.uk and check if the web is live

import requests

responses = requests.get('http://www.bbc.co.uk/')
def check_status():
    if responses: # thecondition was true
        print("Success and the status code " + str(responses.status_code))
    elif responses:
        print("failure ")
    elif responses:
        print("")
print(check_status())
# requests goes one step further in simplifying this process for us
# if you use response instance in a condition expression
# it will evaluate to True if the status code was between 200 and 400, False otherwise
# therefore, you can simplify the last example by rewriting the if statement as above








# responses = requests.get('http://www.bbc.co.uk/')
# print(responses.status_code)
# # status 200 which a success means the website is live running
# # status 400 or 484 means not working
#
# # create a function called status code check
# # function should return status code with appropiate message
# if responses.status_code == 200:
#     print("The website is up and running " + str(responses.status_code))
# else:
#     print("OOPs something went wrong")
#
# def status_code_check():
#
#         responses = input(requests.get('http://www.bbc.co.uk/'))
#         print(responses.status_code)
#         if responses.status_code == 200:
#             print("The website is up and running " + str(responses.status_code))
#         elif responses.status_code == 404:
#             print("This website is unavailable" + str(responses.status_code))
#         else:
#             print("oh no something went wrong!" +str(responses.status_code))
# status_code_check()

#
# def status_code_check():
#
#
#     website = input("Please enter your website")
#     responses = requests.get(website)
#     print(responses.status_code)
#     if responses.status_code == 200:
#         print("The website is up and running " + str(responses.status_code))
#     elif responses.status_code == 404:
#         print("This website is unavailable" + str(responses.status_code))
#     else:
#         print("oh no something went wrong!" + str(responses.status_code))
#
#
# status_code_check()




















