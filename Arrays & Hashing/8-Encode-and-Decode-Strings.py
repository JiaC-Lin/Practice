# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. 

from typing import List

class Solution:
# Need way to determine how a word has ended after the encode to know how to seperate the string
    def encode(self, strs: list[str]) -> str:
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        string = strs[0] 
        # i is index for word taking into account strs[0] is initializer
        for i in range(1, len(strs)): 
            # to account for possible strings to have :;, we make sure there is a repeat for every : and ; so "::;;" will become ":", ";" after the skip which will be made up for in the decode by getting rid of repeats and combining ":", ";" if needed
            if ":" in strs[i] or ";" in strs[i]: 
                strs[i] = strs[i].replace(":", "::")
                strs[i] = strs[i].replace(";", ";;")
            # combine the spacer and the word with string
            string += (":;" + strs[i]) 
        # print(string)
        return string
    
    def decode(self, s: str) -> List[str]:
        """
        @param: s: A string
        @return: decodes a single string to a list of strings
        """
        output, start = [], 0

        while start < len(s): # while loop to skip elements in string
            ending = start
            while (s[ending], s[ending + 1]) != (":", ";"):
                ending += 1
                check = ending + 1 # checks if s[ending + 1] will be out of range
                if check >= len(s):
                    ending += 1
                    break
            addedWord = s[start:ending]

            # first if statement fix repeats done by encode and elif checks again if its suppose to be a single word; combines :;
            indexOfLastStringElement = start - 3    # make sure within bounds
            l = s[indexOfLastStringElement]         # '.l' -> last char of last string
            f = s[start]                            # 'f.' -> first char of current string
            if ("::" in addedWord) or (";;" in addedWord):
                addedWord = addedWord.replace("::", ":")
                addedWord = addedWord.replace(";;", ";")
                output.append(addedWord)
                start = ending + 2
            elif indexOfLastStringElement > 0 and l == ":" and f == ";":
                # add this word to the end of last word in output
                output[-1] += addedWord
                start = ending + 2
            else:
                output.append(addedWord)
                start = ending + 2 # index of where the next word starts"
        # print(f"{output}")
        return output

# Uses the legnth of the string followed by delimiter (#) in front of each word to know the length within the string for decoding
    def neetEncode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def neetDecode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

test = Solution()

strs1 = ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# One possible encode method is: "we:;say:;:::;yes"

strs2 = ["the", "string", ":;", "gone"]
# Output: ["the", "string", ":;", "gone"]

strs3 = ["hey", "wh:;ats", "wrong?"]
# Output: ["hey", "wh:;ats", "wrong?"]

strs4 = ["hey", "wh:", ";ats", "wrong?"]
# Output: ["hey", "wh:", ";ats", "wrong?"]

strs5 = ["hey", ":wh", "ats:", "wrong?"]
# Output: ["hey", ":wh", "ats:", "wrong?"]

dec = test.encode(strs1)
test.decode(dec)

dec = test.encode(strs2)
test.decode(dec)

dec = test.encode(strs3)
test.decode(dec)

dec = test.encode(strs4)
test.decode(dec)

dec = test.encode(strs5)
test.decode(dec)