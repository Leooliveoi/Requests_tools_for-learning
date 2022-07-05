from urllib import request

try:
    # You can place here some headers attributes.
    # You can get this in a "Request Header"
    header = {
        "User-Agent": "Chrome",
        "Cookie": "Nothing"
    }

    # Use Fingerprinting in Target for form variables discovery.
    # You can place here some Form Variables and Values
    data = {
        "user": "",
        "password": "",
    }

    # Method "request.Request()" for create and send a request
    # Apply a header using "headers=" attribute in request
    # Apply a "POST Method" using "data=" attribute in request
    requestVar = request.Request("http://www.bancocn.com", headers=header)

    # Method "urlopen()" for receive a answer
    answer = request.urlopen(requestVar)

    # ".read()" for read a answer
    html = answer.read()

    print(html)
except Exception as e:
    print(e)
    # For "403: Forbidden code", apply a bypass Cookie.
