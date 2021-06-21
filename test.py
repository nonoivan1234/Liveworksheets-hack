text = "prompt' + document.getElementById('wswo').getAttribute('class').charAt(2) + 'd"

text += "'"
text = "'" + text
text = text.replace("document.getElementById('wswo').getAttribute('class').charAt(", "'qwertyuiopasdfghjklzxcvbnm'[")
text = text.replace(")", "]")

print(text)