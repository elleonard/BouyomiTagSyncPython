import config

settings = config.config()

REPLACE_FILE = "./config/replace.txt"
OUTPUT_FILE = settings.get_output_md_path()

def load_replace_list():
  line_list = []
  with open(REPLACE_FILE, "r", encoding="utf-8") as replace:
    lines = replace.readlines()
    for line in lines:
      if line.startswith("//") or line == "\n":
        continue
      line_list.append(line)
  return line_list

def output_md():
  with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write('''---
title: ニコ生登録済み効果音
date: 2016-06-12 10:05:14
tags: [niconico, ニコ生]
category:
  - niconico
---
棒読みちゃんに登録したSE一覧

<!-- more -->

''')
    line_list = load_replace_list()
    for line in line_list:
      if "\t" in line:
        file.write("* "+line.split("\t")[0]+"\n")
      else:
        file.write("\n"+line+"\n")

output_md()
