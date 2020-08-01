import requests

file = open("fuzzing.txt", "r")
content = file.read()
file.close()

header = {"Cookie": "security=low; PHPSESSID=..................."}

for i in content.splitlines():
    print(i)
    url = "http://www.google.com" + str(i)
    result = requests.get(url= url, headers= header)

    if "200" in str(result.status_code):
        print(url + " exists!")
    else:
        print("No file or directory.")
