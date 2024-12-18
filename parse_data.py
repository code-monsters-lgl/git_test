import json


def response(data):
    return json.dumps(data)

if __name__ == '__main__':
    print(response({"name":"test"}))