import json

class cube:
    def __init__(self):
        self.cube = {
            "method": "GET",
            "url": "",
            "referer": "",
            "cookie": "",
            "content_type": "",
            "data": "",
            "headers": {},
            "others": {}
        }

    def set_basic_info(self, method, url="", referer="", cookie="", content_type="", data="", headers={}, others={}):
        self.cube["method"] = method
        self.cube["url"] = url
        self.cube["referer"] = referer
        self.cube["cookie"] = cookie
        self.cube["content_type"] = content_type
        self.cube["data"] = data
        self.cube["headers"] = headers
        self.cube["others"] = others

    def set_basic_info_by_json(self, json_text):
        info_json = json.loads(json_text)
        for json_key in info_json:
            if json_key in self.cube:
                self.cube[json_key] = info_json[json_key]

    def set_info(self, info_name, info_value):
        if info_name in self.cube:
            self.cube[info_name] = info_value
            return True
        else:
            return False

    def get_info(self, info_name):
        if info_name in self.cube:
            return self.cube[info_name]
        else:
            return None

    def get_json_info(self):
        return json.dumps(self.cube)

    def get_result_info(self):
        return self.cube

if __name__ == "__main__":
    foo = cube()
    json_text = '{"method": "GET", "url": "http://www.baidu.com", "referer": "http://www.qq.com", "cookie": "a=1&b=2", "content_type": "xxx", "data": "", "headers": {"Origin": "http://www.baidu.com"}, "others": {}, "a":123}'
    foo.set_basic_info_by_json(json_text)
    result = foo.get_json_info()
    print(result)
