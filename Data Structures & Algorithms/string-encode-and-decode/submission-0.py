class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Extract exactly `length` characters
            string = s[j + 1 : j + 1 + length]
            result.append(string)

            i = j + 1 + length

        return result