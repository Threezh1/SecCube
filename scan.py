from plugins.helper.cube import cube

import importlib

def scan(cube):
    plugin_names = [
        "plugins.poc_example",
    ]
    results = []
    for plugin_name in plugin_names:
        plugin_object = importlib.import_module(plugin_name)
        plugin = plugin_object.Index(cube)
        plugin.audit()
        scan_result = plugin.get_result()
        if scan_result["if_vuln"] == True:
            print(scan_result["cube"].get_info("url"))
    return results

if __name__ == "__main__":
    foo = cube()
    json_text = '{"method": "GET", "url": "http://www.baidu.com", "referer": "http://www.qq.com", "cookie": "a=1&b=2", "content_type": "xxx", "data": "", "headers": {"Origin": "http://www.baidu.com"}, "others": {}, "a":123}'
    foo.set_basic_info_by_json(json_text)
    scan(foo)