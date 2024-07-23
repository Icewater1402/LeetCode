from typing import List
class Solution:

    def encode(strs: List[str]) -> str:
        combined_list = ""
        for i in strs:
            combined_list += i 
            combined_list += " "
        print(combined_list)
        return combined_list

    def decode(s: str) -> List[str]:
        decode_list = []
        word = ""
        for letter in s:
            if(letter == " "):
                decode_list.append(word)
                word = "" 
                continue
            else:
                word += letter 
                continue
        return decode_list

    encoded = encode(["hello", "how", "many", "times"])
    print(decode(encoded))