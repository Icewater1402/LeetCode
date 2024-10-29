from typing import List
class Solution:


# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.

    def encode(strs: List[str]) -> str:
        encoded_dict = {} 
        for i in strs:
            encoded_dict[i] = 0
        encoded_str = ""
        for key in encoded_dict:
            encoded_str += key + " "
        print(encoded_str)
        return encoded_str

    def decode(s: str) -> List[str]:
        decode_spaces = []
        decode_list = []
        word = ""
        
    #problem with this is knowing what the original array looked like after encoding it the first time 
    # i want to use a dictionary to keep track of existing indices but its unaccessible by the decoder 
    


    encoded = encode(["The quick brown fox", "jumps over the", "lazy dog", "1234567890", "abcdefghijklmnopqrstuvwxyz"])
    #print(decode(encoded))