js_file = ""
with open("FilianARG_no_Char_Swap.js","r") as f:
    js_file = f.read()

js_file = js_file.replace('" + "','')
js_file = js_file.replace('" + \'','')
js_file = js_file.replace('\' + "','')
js_file = js_file.replace("' + '",'')


with open("FilianARG_combine.js","w+") as f:
    f.write(js_file);

