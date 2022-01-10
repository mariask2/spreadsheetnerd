import json
import os
import statistics

f = open('rkf_UIIx_mjexport.json')
data = json.load(f)
total_nr_of_texts = 0
for el in data:
    texts = el["text"].split("m\n")
    id = el["ID"]
    for nr, text in enumerate(texts):
        total_nr_of_texts = total_nr_of_texts + 1
        file_name = el["ID"] + "_" + str(nr + 1)
        file_path = os.path.join("sprak_tilltal_delat", file_name + ".txt")
        print(file_path)
        f = open(file_path, "w")
        text = text.replace("dialekt", " dialekt")
        text = text.replace("mål", " mål")
        f.write(text)
        f.close()

