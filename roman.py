# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Examples

class RomanNumerals:
    def __init__(self):
        self.symbol = ''
        self.value = 0
        self.dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_roman(self, value):
        self.symbol = ''
        if value >= 1000:
            (div, value) = divmod(value, 1000)
            self.symbol += 'M' * div
        if value >= 100:
            (div, value) = divmod(value, 100)
            if div == 9:
                self.symbol += 'CM'
            elif div >= 5:
                self.symbol += 'D' + 'C' * (div - 5)
            elif div == 4:
                self.symbol += 'CD'
            else:
                self.symbol += 'C' * div
        if value >= 10:
            (div, value) = divmod(value, 10)
            if div == 9:
                self.symbol += 'XC'
            elif div >= 5:
                self.symbol += 'L' + 'X' * (div - 5)
            elif div == 4:
                self.symbol += 'XL'
            else:
                self.symbol += 'X' * div
        if value == 9:
            self.symbol += 'IX'
        elif value >= 5:
            self.symbol += 'V' + 'I' * (value - 5)
        elif value == 4:
            self.symbol += 'IV'
        else:
            self.symbol += 'I' * value
        return self.symbol

    def from_roman(self, symbol):
        self.value = 0
        temp = []
        for each in symbol:
            temp.append(self.dict[each])
        self.value += temp[-1]
        if len(temp) > 1:
            for i in range(len(temp) - 2, 0, -1):
                if temp[i] < temp[i+1]:
                    self.value -= temp[i]
                else:
                    self.value += temp[i]
            if temp[0] < temp[1]:
                self.value -= temp[0]
            else:
                self.value += temp[0]
        return self.value

RomanNumerals = RomanNumerals()


# Alternative Solution 

class RomanNumerals:
    @staticmethod
    def from_roman(s):
        X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]
        return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])
    @staticmethod
    def to_roman(i,o=' I II III IV V VI VII VIII IX'.split(' ')):
        r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC','XLCDM'))[c]for c in r(n//10))+o[n%10]
        return r(i)

