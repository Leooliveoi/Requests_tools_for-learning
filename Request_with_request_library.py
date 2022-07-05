import requests  # <> pip install requests

# To Develop in future a terminal integration

try:
    # You can place here some headers attributes.
    # You can get this in a "Request Header"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.81 Safari/537.36",

        "Cookie": "cf_chl_prog=a8; "
                  "cf_clearance=1bdbb220bb2a2c7e1ef2fb7fbfdfde3447a6a22e-1634652188-0-150",
    }

    # Use Fingerprinting in Target for form variables discovery.
    # You can place here some Form Variables and Values
    data = {
        "user": "admin",
        "password": "senhafoda",
    }

    # Use requests.get() for create a web request with "get method"
    # Apply a "headers=" for use a personal header in request
    getAnswer = requests.get("http://www.bancocn.com/", headers=header)
    print("______________________________________")
    print("GET METHOD: \n"
          "{}\n"
          "Use <.text> for html read".format(getAnswer))

    # Use request.post() for create and send a web request with "post method"
    # Apply a "headers= or/and data=" for use a personal header or send a form variables in web request
    postAnswer = requests.post("http://www.bancocn.com/admin/index.php", headers=header, data=data)
    print("______________________________________")
    print("POST METHOD: \n"
          "{}\n"
          "Use <.text> for html read".format(postAnswer))

except Exception as e:
    print(e)
