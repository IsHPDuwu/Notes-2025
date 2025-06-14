import os
import re
import locale

# 设置 locale 用于中文排序（系统需支持 zh_CN.UTF-8）
locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')

def parse_md_files(directory, output_basename):
    """
    遍历指定目录下所有 .md 文件，解析行格式：
      A ::: B Page
    每行生成两个条目：
      对于 A：{"data": B, "page": "<文件名>:Page"}
      对于 B：{"data": A, "page": "<文件名>:Page"}
    忽略空行、Markdown 标题行（# 开头）、以及包含 ":-:" 的行。
    若同一键出现多次，则在字典中以列表形式保存所有重复条目。
    注意：directory中若有文件名与 output_basename 相同的文件，将不会被处理。
    """
    data_dict = {}
    # 正则表达式：
    # (?:\{)?(.+?)(?:\})?    匹配 A（允许有或无大括号）
    # \s*:::\s*              匹配分隔符 " ::: "（两边允许空白）
    # (?:\{)?(.+?)(?:\})?    匹配 B
    # \s+(\S+)               匹配 Page（至少一个空格后的非空字符）
    pattern = re.compile(r"(?:\{)?(.+?)(?:\})?\s*:::\s*(?:\{)?(.+?)(?:\})?\s+(\S+)")
    
    # 如果指定的 directory 不目录，则使用脚本所在的目录
    if not os.path.isdir(directory):
        directory = os.path.dirname(os.path.abspath(__file__))
    
    for filename in os.listdir(directory):
        cnt = 0
        # 跳过输出文件（如 "data.md"）
        if filename == output_basename:
            continue
        if not filename.endswith(".md"):
            continue
        
        # 获取去掉扩展名的文件名，用于附加在 Page 字段前
        fname = os.path.splitext(filename)[0]
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                # 忽略空行及 Markdown 标题行
                if not line or line.startswith("#"):
                    continue
                # 忽略包含 ":-:" 的行
                if ":-:" in line:
                    continue
                match = pattern.match(line)
                # print(f"Processing line:, match {match}")  # 调试输出
                if match:
                    cnt += 1
                    A, B, page = match.groups()
                    new_page = f"{fname}:{page}"
                    # 为 A 添加条目（字典中以列表保存重复项）
                    data_dict.setdefault(A, []).append({"data": B, "page": new_page})
                    # 为 B 添加条目
                    data_dict.setdefault(B, []).append({"data": A, "page": new_page})
        print(f"{filename} Processed {cnt} entries from {len(data_dict)} unique keys.")
    return data_dict

def output_sorted_data_dict(data_dict, output_file, reverse_sort=False):
    """
    对 data_dict 的所有键按 locale 排序，然后分组输出：
      1. 根据键首字符（去除空白后的第一个字符，若为字母则转大写）进行分组，
         每组输出 Markdown 大标题（例如 "# A" 或 "# 创"）。
      2. 同一组内每个键对应的所有条目，均按 "index ::: data page" 格式输出，
         其中 page 内已包含文件名信息。
    """
    sorted_keys = sorted(data_dict.keys(), key=locale.strxfrm, reverse=reverse_sort)
    
    with open(output_file, "w", encoding="utf-8") as f:
        current_initial = None
        for key in sorted_keys:
            key_str = key.strip()
            if not key_str:
                continue
            first_char = key_str[0]
            header = first_char.upper() if first_char.isalpha() else first_char
            if header != current_initial:
                # 输出 Markdown 分组大标题，组间插入空行便于阅读
                f.write(f"\n# {header}\n\n")
                current_initial = header
            # 输出每个键下所有条目
            for entry in data_dict[key]:
                line = f"{key} :: {entry['data']} {entry['page']}"
                f.write(line + "\n\n")

if __name__ == "__main__":
    # 请将目录路径替换为你的 .md 文件所在目录，
    # 如果留空或指定的不目录，则将使用当前脚本所在目录。
    directory = "."
    output_file = "data.md"
    
    # 注意：传递 output_file 的 basename 以确保扫描时跳过该文件
    data_dict = parse_md_files(directory, os.path.basename(output_file))
    output_sorted_data_dict(data_dict, output_file, reverse_sort=False)
