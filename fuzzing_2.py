import requests

"""header = {"Cookie": "security=low; PHPSESSID=..................."}"""

file = open("fuzzing.txt", "r")
content = file.read()
file.close()

for i in content.splitlines():
    print(i)
    url = "http://www.google.com" + str(i)
    result = requests.get(url= url)
    
    """
    cookies = result.cookies
    a = cookies.add_cookie_header(result)
    print(a)
    """

    if "200" in str(result.status_code):
        print(url + " exists!")
    else:
        print("No file or directory.")