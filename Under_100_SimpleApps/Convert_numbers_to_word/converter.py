# Dictionary to map single-digit numbers to their word representations
one_digit_words = {
    '0': ["zero"],
    '1': ["one"],
    '2': ["two", "twen"],
    '3': ["three", "thir"],
    '4': ["four", "for"],
    '5': ["five", "fif"],
    '6': ["six"],
    '7': ["seven"],
    '8': ["eight"],
    '9': ["nine"],
}

# List of word representations for two-digit numbers from 10 to 12
two_digit_words = ["ten", "eleven", "twelve"]

# Word representation for "hundred"
hundred = "hundred"

# List of word representations for large sums (e.g., thousand, million)
large_sum_words = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]

def converter(n):
    """Converts a numeric string into words."""
    word = []

    # Handle negative numbers
    if n.startswith('-'):
        word.append("(negative)")
        n = n[1:]
    
    # Add leading zeros if necessary for grouping by three digits
    if len(n) % 3 != 0 and len(n) > 3:
        n = n.zfill(3 * (((len(n)-1) // 3) + 1))

    # Group the number into chunks of three digits
    sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
    skip = False

    # Iterate over each chunk of three digits
    for i, num in enumerate(sum_list):
        if num != '000':
            skip = False
        
        # Iterate over each digit in the current chunk
        for _ in range(len(num)):
            num = num.lstrip('0')

            # Convert single-digit number to word representation
            if len(num) == 1:
                if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1 and (word[-1] in large_sum_words or hundred in word[-1]):
                    word.append("and")
                word.append(one_digit_words[num][0])
                num = num[1:]
                break

            # Convert two-digit number to word representation
            if len(num) == 2:
                if num[0] != '0':
                    if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1:
                        word.append("and")
                    if num.startswith('1'):
                        if int(num[1]) in range(3):
                            word.append(two_digit_words[int(num[1])])
                        else:
                            number = one_digit_words[num[1]][1 if int(num[1]) in range(3, 6, 2) else 0] 
                            word.append(number + ("teen" if not number[-1] == 't' else "een"))
                    else:
                        word.append(one_digit_words[num[0]][1 if int(num[0]) in range(2, 6) else 0] + ("ty " if num[0] != '8' else 'y ') + (one_digit_words[num[1]][0] if num[1] != '0' else ""))
                    break
                else:
                    num = num[1:]
                    continue
                
            # Convert three-digit number to word representation
            if len(num) == 3:
                if num[0] != '0':
                    word.append(one_digit_words[num[0]][0] + " " + hundred)
                    if num[1:] == '00': break
                num = num[1:]
 
        # Add word representation for large sums
        if len(sum_list[i:]) > 1 and not skip:
            word.append(large_sum_words[len(sum_list[i:]) - 2])
            skip = True
    
    # Join the word list into a single string
    word = " ".join(map(str.strip, word))
    
    # Capitalize the first letter and format negative numbers
    return word[0].lstrip().upper() + word[1:].rstrip().lower() if "negative" not in word else word[:11].lstrip() + word[11].upper() + word[12:].rstrip().lower()

if __name__ == "__main__":
    # Main loop to get user input and convert numbers to words
    while True:
        try:
            n = input("Enter any number to convert it into words or 'exit' to stop: ")
            if n == "exit":
                break
            int(n)
            print(n, "-->", converter(n))
        except ValueError:
            print("Error: Invalid Number!")
