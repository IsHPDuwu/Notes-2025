import os

def readtxt(file):
    with open(f'{file}.txt', 'r', encoding='utf-8') as f:
        return f.readlines()



def solvelines(lines: str):
    s1 = ""
    s2 = ""
    i = 0
    li = []
    for line in lines:
        # print(line)
        line = line.replace("\n", "")
        if (line[0].islower() or line[0]=="@"):
            pos=line.find("〔")
            if (pos!=-1):
                li.append((s1, s2))
                s1 = ""
                s2 = ""
                i = pos+1
                while (i < len(line)):
                    if (line[i] == "〕"):
                        break
                    i += 1
                s1 = line[pos+1:i]
                s2 = line[i+1:]
            else:
                s1 = "na"
                s2 = line[1:]
        else:
            s2 += line
        print(f"{s1}::{s2}")
        # print()
    return li


def output(li,file,path):
    with open(f"{path}{file}.md", "w", encoding="utf-8") as f:
        f.write(f"# {file}\n")
        f.write(f"#flashcard/{file}\n\n\n")
        for i in li:
            if(i[0]!=""):
                print(f"{i[0]} :: {i[1]}")
                f.write(f"{i[0]} :: {i[1]}\n\n")


if __name__ == "__main__":
    # raw = solvelines(readtxt("chs-kxzs"))
    # output(raw, "output")
    path = "./chs-kxzs/"
    for file in os.listdir(path):
        if file.endswith(".txt"):
            print(file)
            raw = solvelines(readtxt(path+file[:-4]))
            output(raw, file[:-4],path)
    
