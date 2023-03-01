# Function to convert number into word
def convert_number_to_word(number):
    # Dictionary to store the conversion of numbers into words
    num_words = {1 : 'một', 2 : 'hai', 3 : 'ba', 4 : 'bốn', 5 : 'năm', 
                 6 : 'sáu', 7 : 'bảy', 8 : 'tám', 9 : 'chín'} 
  
    # If number is single digit, return the corresponding word 
    if(number in num_words): 
        return num_words[number] 

    # Find the quotient and remainder and recur  
    else: 
        quotient = number // 10
        remainder = number % 10

        # If quotient is 0, return the corresponding word for remainder  
        if(quotient == 0):  
            return num_words[remainder]  

        # If remainder is 0, return the corresponding word for quotient  
        elif(remainder == 0):  
            return num_words[quotient] + " mươi"

        # If both quotient and remainder are non-zero, return corresponding words for both of them. 												 
        else: 
            return num_words[quotient] + " mươi " + num_words[remainder]
