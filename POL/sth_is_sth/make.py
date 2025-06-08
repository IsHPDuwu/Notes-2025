import os
import re
import locale

# 设置 locale 用于中文排序（需要系统支持 zh_CN.UTF-8）
locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')

def parse_md_files(directory):
    data_dict = {}
    # 正则表达式说明：
    # (?:\{)?(.+?)(?:\})?    ：匹配 A（可含大括号或不含）
    # \s*:::\s*              ：匹配分隔符 :::（两边允许空白）
    # (?:\{)?(.+?)(?:\})?    ：匹配 B
    # \s+(\S+)               ：匹配 Page（至少一个空格后的非空字符）
    pattern = re.compile(r"(?:\{)?(.+?)(?:\})?\s*:::\s*(?:\{)?(.+?)(?:\})?\s+(\S+)")
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # 去除文件扩展名
            fname = os.path.splitext(filename)[0]
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    # 忽略空行和 Markdown 标题行
                    if not line or line.startswith("#"):
                        continue
                    
                    match = pattern.match(line)
                    if match:
                        A, B, page = match.groups()
                        # 在 Page 信息前附上文件名（用冒号分隔）
                        new_page = f"{fname}:{page}"
                        # 建立双向关联
                        data_dict[A] = {"data": B, "page": new_page}
                        data_dict[B] = {"data": A, "page": new_page}
    return data_dict

def output_sorted_data_dict(data_dict, output_file, reverse_sort=False):
    """
    功能说明：
    1. 使用 locale.strxfrm 进行 locale-aware 的排序（支持中文）；
    2. 按照排序后的键，依据各键的首字符分组，并以 Markdown 大标题形式输出（例如 `# A`、`# 创` 等）。
    3. 每行按原格式输出：A ::: B Page，其中 Page 字段内包含已附带的文件名信息。
    """
    sorted_keys = sorted(data_dict.keys(), key=locale.strxfrm, reverse=reverse_sort)
    
    with open(output_file, "w", encoding="utf-8") as f:
        current_initial = None
        for key in sorted_keys:
            # 取去除空白后的第一个字符
            first_char = key.strip()[0]
            # 如果是字母，则转为大写，否则保持原样
            header = first_char.upper() if first_char.isalpha() else first_char
            if header != current_initial:
                # 分组大标题行前先添加空行以便更清晰区分（可根据需要调整）
                f.write(f"\n# {header}\n\n")
                current_initial = header
            # 按原格式输出行：A ::: B Page（Page 中已包含文件名）
            entry = data_dict[key]
            line = f"{key} ::: {entry['data']} {entry['page']}"
            f.write(line + "\n\n")

if __name__ == "__main__":
    # 请将此处路径替换为存放 .md 文件的目录路径
    directory = "./"
    output_file = "data.md"
    
    data_dict = parse_md_files(directory)
    output_sorted_data_dict(data_dict, output_file, reverse_sort=False)
    print(f"已将排序并分组后的数据输出到 {output_file}")
