class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validCoupons = []
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        for i,item in enumerate(code):
            if self.codeIsValid(item) == False:
                continue
            if isActive[i] == False:
                continue
            if self.businessLineIsValid(businessLine[i]) == False:
                continue
            validCoupons.append((priority[businessLine[i]], item))

        validCoupons.sort()
        #validCoupons = sorted(validCoupons, key=lambda tup:tup[0])
        #print(validCoupons)
        return [ coupon[1] for coupon in validCoupons ]

    def codeIsValid(self, code: str) -> bool:
        if code == "":
            return False

        for char in code:
            if char.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_":
                return False
        return True

    def businessLineIsValid(self, businessLine) -> bool:
        return businessLine in ["electronics", "grocery", "pharmacy", "restaurant"]