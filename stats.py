#Accepts a string of text and returns a int
def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    ch_dict = {}

    for ch in lower_text:
        if ch not in ch_dict:
            ch_dict[ch] = 0
        ch_dict[ch] += 1
    
    return ch_dict

def sort_on(char_data):
    return char_data["count"]

def sorted_list(ch_dict):
    ch_list = []

    for char_key in ch_dict:

        sorted_ch = {
            "char": "",
            "count": 0
        }

        sorted_ch["char"] = char_key
        sorted_ch["count"] = ch_dict[char_key]
        ch_list.append(sorted_ch)



    ch_list.sort(reverse=True, key=sort_on)

    return ch_list

        
        

    
