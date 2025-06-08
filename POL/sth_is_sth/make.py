import os
import re
import locale

# 设置 locale 用于中文排序（需系统支持 zh_CN.UTF-8）
locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')

def parse_md_files(directory):
    """
    遍历指定目录下所有 .md 文件，按行解析形如：
      A ::: B Page
    为了处理一份文件内重复的相同数据，每一匹配行均生成两个条目：
      {"data": B, "page": "<文件名>:Page"} 对应 A
      {"data": A, "page": "<文件名>:Page"} 对应 B
    最后将所有条目存入一个字典，键为 A 或 B（允许每个键存在多个条目，以列表形式保存）。
    """
    data_dict = {}
    # 正则说明：
    # (?:\{)?(.+?)(?:\})?    匹配 A（可有可无大括号）
    # \s*:::\s*              匹配分隔符 :::（两边允许空格）
    # (?:\{)?(.+?)(?:\})?    匹配 B
    # \s+(\S+)               匹配 Page（至少一个空格后的非空字符）
    pattern = re.compile(r"(?:\{)?(.+?)(?:\})?\s*:::\s*(?:\{)?(.+?)(?:\})?\s+(\S+)")
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # 获取文件名（不含扩展名）用于附在 Page 前面
            fname = os.path.splitext(filename)[0]
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    # 忽略空行和 Markdown 标题行（以 '#' 开头）
                    if not line or line.startswith("#"):
                        continue
                    
                    match = pattern.match(line)
                    if match:
                        A, B, page = match.groups()
                        # 新的 page 格式： 文件名:Page
                        new_page = f"{fname}:{page}"
                        # 为 A 添加一个条目
                        entry_A = {"data": B, "page": new_page}
                        data_dict.setdefault(A, []).append(entry_A)
                        # 为 B 添加一个条目
                        entry_B = {"data": A, "page": new_page}
                        data_dict.setdefault(B, []).append(entry_B)
    return data_dict

def output_sorted_data_dict(data_dict, output_file, reverse_sort=False):
    """
    输出要求：
      1. 将字典的键按 locale 排序（支持中文排序），允许重复条目（列表内多个条目）。
      2. 根据每个键去除空白后的首字符分组，分组在输出时以 Markdown 一级标题标记（如 "# A"，"# 创" 等）。
      3. 输出格式为：  index ::: data page
         其中 page 内含文件名信息，且相同键的所有条目都要输出。
    """
    # 对字典键进行排序
    sorted_keys = sorted(data_dict.keys(), key=locale.strxfrm, reverse=reverse_sort)
    
    with open(output_file, "w", encoding="utf-8") as f:
        current_initial = None
        for key in sorted_keys:
            key_str = key.strip()
            if not key_str:
                continue
            # 取首字符，若为字母则转为大写
            first_char = key_str[0]
            header = first_char.upper() if first_char.isalpha() else first_char
            if header != current_initial:
                # 输出 Markdown 大标题行，分组之间可插入空行便于阅读
                f.write(f"\n# {header}\n\n")
                current_initial = header
            # 对于每个键下的所有条目依次输出
            for entry in data_dict[key]:
                line = f"{key} ::: {entry['data']} {entry['page']}"
                f.write(line + "\n\n")

if __name__ == "__main__":
    # 请将此目录替换为存放 .md 文件的目录
    directory = "./"
    output_file = "data.md"
    
    data_dict = parse_md_files(directory)
    output_sorted_data_dict(data_dict, output_file, reverse_sort=False)
    print(f"已将按分组、并保留重复条目的数据输出到 {output_file}")
