class Roman:
    def to_roman(self, num):
        roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        res = ''
        for val, sym in sorted(roman.items(), reverse=True):
            while num >= val:
                res += sym
                num -= val
        return res

r = Roman()
try:
    n = int(input("Num: "))
    print(r.to_roman(n))
except ValueError:
    print("Invalid Input")