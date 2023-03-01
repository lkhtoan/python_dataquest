def convert_number_to_words(number):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    if number < 20:
        return ones[number]
    elif number < 100: 
        return tens[number // 10] + (ones[number % 10] if (number % 10) > 0 else '') 
    else: 
        return ones[number // 100] + ' hundred' + ((' ' + convert_number_to_words(number % 100)) if (number % 100) > 0 else '') 
    
# The problem with the code was that the tens list did not include a value for zero. This was fixed by adding 'zero' to the list. 
# Additionally, the code was modified to account for numbers greater than or equal to 100, 
# by adding an additional condition that checks if the number is greater than or equal to 100 and returns a string with the appropriate value.

#Convert a number into number in word by Vietnamese0
