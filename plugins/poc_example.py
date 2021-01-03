from plugins.helper.cube import cube

class Index:
    def __init__(self, task_cube):
        self.cube = task_cube
        self.result = {
            "if_vuln": False,
            "cube": self.cube,
            "vuln_name": "vuln name",
            "vuln_info": "vuln info",
        }

    def assign(self):
        # 预留作特定指纹扫描
        return None

    def audit(self):
        print("doing well")
        self.result["if_vuln"] = True
        self.result["vuln_info"] = "This is a test"

    def get_result(self):
        return self.result

if __name__ == "__main__":
    foo = cube()
    json_text = '{"method": "GET", "url": "http://www.baidu.com", "referer": "http://www.qq.com", "cookie": "a=1&b=2", "content_type": "xxx", "data": "", "headers": {"Origin": "http://www.baidu.com"}, "others": {}, "a":123}'
    foo.set_basic_info_by_json(json_text)
    bar = Index(foo)
    bar.audit()
    print(bar.get_result())