import json
import requests

# 从JSON文件中读取JSON对象
def read_json_objects(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_array = json.load(file)
        for json_obj in json_array:
            yield json_obj

# 发送POST请求
def post_json(url, json_obj):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json=json_obj, headers=headers)
    return response

# 将字段收集到JSON数组中
def collect_fields(json_obj):
    id_value = json_obj.get('id', None)
    request_url = json_obj.get('request', {}).get('url', None)

    if id_value is not None and request_url is not None:
        return {"id": id_value, "request.url": request_url}
    return None

# 将JSON数组写入文件
def write_json_array_to_file(file_path, json_array):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_array, file, ensure_ascii=False, indent=4)

# 主函数
def main():
    input_file_path = 'path/to/your/input.json'
    output_file_path = 'urls'
    post_url = 'https://host/jsons'

    id_request_url_pairs = []

    for json_obj in read_json_objects(input_file_path):
        response = post_json(post_url, json_obj)

        if response.status_code == 200:
            pair = collect_fields(response.json())
            if pair is not None:
                id_request_url_pairs.append(pair)
        else:
            print(f"Error posting JSON object: {response.status_code}")

    write_json_array_to_file(output_file_path, id_request_url_pairs)

if __name__ == "__main__":
    main()
