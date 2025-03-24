class Solution:
    def isNumber(self, s: str) -> bool:
        num = s.upper()

        if self.validateSymbols(num) is False:
            return False

        nums = "0123456789"
        hasNumbers = False
        for n in num:
            if n in nums:
                hasNumbers = True

        if hasNumbers is False:
            return False

        return self.isInteger(num) or self.isDecimal(num)

    def validateSymbols(self, num: str) -> bool:
        validSymbols = "+-0123456789.E"
        for n in num:
            if n not in validSymbols:
                return False
        return True

    def isInteger(self, num: str) -> bool:
        if "." in num:
            return False

        if self.hasValidSigns(num) is False:
            return False
        if self.hasValidExponent(num) is False:
            return False

        return True

    def isDecimal(self, num: str) -> bool:
        if num.count(".") != 1:
            return False
        if num == ".":
            return False

        if self.hasValidSigns(num) is False:
            return False
        if self.hasValidExponent(num) is False:
            return False

        return True

    def hasValidSigns(self, num: str) -> bool:
        if "+" not in num and "-" not in num:
            return True

        if "E" not in num:
            if num.count("+") > 1 or num.count("-") > 1:
                return False
            if "+" in num and "-" in num:
                return False
            if num.find(".") != -1 and num.find("-") > num.find("."):
                return False

        prev = num[0]
        nums = "0123456789"
        for n in num:
            if prev in nums and n == "-":
                return False
            if prev in nums and n == "+":
                return False
            if prev == "-" and n == "+":
                return False
            if prev == "+" and n == "-":
                return False
            if prev == "." and n == "-":
                return False
            if prev == "." and n == "+":
                return False
            if prev == "-" and n == "E":
                return False
            if prev == "+" and n == "E":
                return False
            prev = n

        if num.find("++") == 0:
            return False

        return True

    def hasValidExponent(self, num: str) -> bool:
        if "E" not in num:
            return True

        if num[-1] == "E":
            return False
        if num[-1] == "-":
            return False
        if num[-1] == "+":
            return False
        if num.find(".") > num.find("E"):
            return False

        hasPlus = num.find("+") > num.find("E")
        hasMinus = num.find("-") > num.find("E")
        prev = num[0]
        nums = "+-0123456789."
        for n in num:
            if n == "E" and prev not in nums:
                return False
            prev = n

        if hasMinus and hasPlus:
            return False
        if num.count("E") != 1:
            return False

        if num.find(".E") == 0:
            return False
        if num.find("+.E") == 0:
            return False

        return True
