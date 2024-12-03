public class Solution {
    public string IntToRoman(int num) {
        var remainder = num;
        var sb = new StringBuilder();
        while (remainder > 0)
        {
            var subjectiveResult = HandleSubjectiveForm(remainder);
            if (subjectiveResult.Item1 != 0 && subjectiveResult.Item2 != "")
            {
                remainder -= subjectiveResult.Item1;
                sb.Append(subjectiveResult.Item2);
                continue;
            }

            var nonSubjectiveFormResult = HandleNonSubjectiveForm(remainder);
            remainder -= nonSubjectiveFormResult.Item1;
            sb.Append(nonSubjectiveFormResult.Item2);
        }

        return sb.ToString();
    }

    private (int, string) HandleSubjectiveForm(int input)
    {
        var remainder = input.ToString();
        if (remainder[0..1] == "9")
        {
            if (input >= 900) return (900, "CM");
            if (input >= 90) return (90, "XC");
            if (input >= 9) return (9, "IX");
        }
        if (remainder[0..1] == "4")
        {
            if (input >= 400) return (400, "CD");
            if (input >= 40) return (40, "XL");
            if (input >= 4) return (4, "IV");
        }

        return (0, "");
    }

    private (int, string) HandleNonSubjectiveForm(int remainder)
    {
        if (remainder >= 1000)
        {
            return (1000, "M");
        }
        else if (remainder >= 500)
        {
            return (500, "D");
        }
        else if (remainder >= 100)
        {
            return (100, "C");
        }
        else if (remainder >= 50)
        {
            return (50, "L");
        }
        else if (remainder >= 10)
        {
            return (10, "X");
        }
        else if (remainder >= 5)
        {
            return (5, "V");
        }
        else
        {
            return (1, "I");
        }
    }
}