import http.client
import json


def print_response(response):
    print("Response: " + response.read().decode('utf-8'))
    print("Status: " + str(response.status))
    print("Reason: " + str(response.reason) + "\n")


def test_methods(method, path):
    connection = http.client.HTTPConnection('localhost', 80, timeout=10)
    connection.request(method, path)
    response = connection.getresponse()
    print_response(response)
    connection.close()


def test_json(method, path, json_data):
    conn = http.client.HTTPConnection('localhost', 80, timeout=10)
    conn.request(method, path, json_data)
    response = conn.getresponse()
    print_response(response)
    conn.close()


if __name__ == '__main__':
    json_data = json.dumps({"name": "Werka", "job": "Koderka"})

    # GET, POST, PUT
    test_methods("GET", "/get/Werka")
    test_methods('POST', '/post')

    # POST, PUT JSON
    test_json('POST', '/post/json', json_data)
    test_json('PUT', '/put/json', json_data)

    # url passing parameter
    test_methods("POST", "/Werka?text=witaj")
