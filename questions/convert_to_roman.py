def int_to_rome(x):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i = 12
    roman_numeral = ''
    while x!=0:
            if numbers[i]<= x:
                roman_numeral += roman[i]
                x = x - numbers[i]
            else:
                i -= 1

    # print(roman_numeral)
    return roman_numeral

print(int_to_rome(49))
print(int_to_rome(1890))
print(int_to_rome(2021))
