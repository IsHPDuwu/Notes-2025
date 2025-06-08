import os
import re

def parse_md_files(directory):
    data_dict = {}
    # 正则说明：
    # (?:\{)?   : 可选的左大括号
    # (.+?)     : 惰性匹配，捕获第一部分（A）
    # (?:\})?   : 可选的右大括号
    # \s*:::\s* : 分隔符 ::: 两边允许有空白字符
    # (?:\{)?   : 可选的左大括号
    # (.+?)     : 惰性匹配，捕获第二部分（B）
    # (?:\})?   : 可选的右大括号
    # \s+       : 一个或多个空格
    # (\S+)     : 捕获 Page（非空字符）
    pattern = re.compile(r"(?:\{)?(.+?)(?:\})?\s*:::\s*(?:\{)?(.+?)(?:\})?\s+(\S+)")
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    # 跳过空行及 Markdown 标题行（以 # 开头）
                    if not line or line.startswith("#"):
                        continue
                    
                    match = pattern.match(line)
                    if match:
                        A, B, page = match.groups()
                        # 建立双向关联
                        data_dict[A] = {"data": B, "page": page}
                        data_dict[B] = {"data": A, "page": page}
    return data_dict

def output_sorted_data_dict(data_dict, output_file):
    # 使用 sorted 对字典的 key 进行字典序排序
    sorted_keys = sorted(data_dict.keys(), key=lambda x: x.strip())
    with open(output_file, "w", encoding="utf-8") as f:
        for key in sorted_keys:
            entry = data_dict[key]
            # 原始格式：A ::: B Page
            line = f"{key} ::: {entry['data']} {entry['page']}"
            f.write(line + "\n\n")

if __name__ == "__main__":
    # 请替换为你存放.md 文件的目录路径
    directory = "./"  
    output_file = "data.md"
    
    data_dict = parse_md_files(directory)
    output_sorted_data_dict(data_dict, output_file)
    print(f"已将排序后的数据输出到 {output_file}")
