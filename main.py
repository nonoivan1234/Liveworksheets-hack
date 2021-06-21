import requests

def decode_per_ques(original):
    ans = original[0]
    ans += "'"
    ans = "'" + ans
    ans = ans.replace("document.getElementById('wswo').getAttribute('class').charAt(", '"qwertyuiopasdfghjklzxcvbnm"[')
    ans = ans.replace(")", "]")
    ans = eval(ans)
    return ans

url = input('Input the worksheet URL:\n')
r = requests.get(url)
text = r.text
ind_start = text.find("contenidojson = '[[")
ind_end = text.find("offxf = document.getElementById")
original_list = eval(text[ind_start+17:ind_end-11])
ans_list = []

for original in original_list:
    ans_list.append(decode_per_ques(original))
    
print(ans_list)