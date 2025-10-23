class Solution:
    def dayOfYear(self, date: str) -> int:
        daysInMonthLookup = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year = int(date[:4])
        isLeapYear = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        month = int(date[5:7])
        date = int(date[8:10])
        print(month)
        print(date)

        dayOfYear = 0
        for m in range(1, month + 1):
            daysInMonth = daysInMonthLookup[m - 1]
            if m == 2 and isLeapYear:
                daysInMonth = 29

            if m == month:
                dayOfYear += date
            else:
                dayOfYear += daysInMonth

        return dayOfYear
