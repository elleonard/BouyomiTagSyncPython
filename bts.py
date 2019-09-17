import config
import replacetag
import fileinput

settings = config.config()
REPLACE_FILE = "./config/replace.txt"

# replace.txt読み込み
def load_replace_list():
  replace_list = {}
  with open(REPLACE_FILE, "r", encoding="utf-8") as replace:
    lines = replace.readlines()
    for line in lines:
      if line.startswith("//") or line.startswith("#"):
        continue
      tag_path = line.split("\t")
      if len(tag_path) > 1:
        replace_list[tag_path[0]] = replacetag.replace_tag(tag_path[0], settings.get_sound_root() + "\\" + tag_path[1])
  return replace_list

def tag_sync():
  replace_list = load_replace_list()
  # 既存行の更新
  updateLines = []
  with open(settings.get_bouyomi_replace_path(), "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
      line_data = line.split("\t")
      if len(line_data) > 3 and line_data[2] in replace_list:
        updateLines.append(make_line(line_data[2], replace_list[line_data[2]].path.strip()))
        replace_list[line_data[2]].isNew = False
        print("update "+line_data[2])
      else:
        updateLines.append(line)
  # 新規行の追加
  addLines = []
  for replace in replace_list.values():
    if replace.isNew:
      addLines.append(make_line(replace.text, replace.path.strip()))
      print("add "+replace.text)
  with open(settings.get_bouyomi_replace_path(), "w", encoding="utf-8") as file:
    for updateLine in updateLines:
      file.write(updateLine)
    for addLine in addLines:
      file.write(addLine)

def make_line(text, path):
  return ""+str(len(text))+"\tN\t"+text+"\t(SoundW "+path+")\n"

tag_sync()
