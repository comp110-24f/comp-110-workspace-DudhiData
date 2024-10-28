"""EX06 Utility Functions"""

__author__ = "730756130"


def invert(input: dict[str, str]) -> dict[str, str]:
    # if a dupe exists for a value in the dict it will create duplicate keys after inversion
    # raise KeyError if duplicate values exist in the values of the dict
    check_dupe: list[str] = []
    # creating list to hold the values of the input dict
    for key in input:
        # populating list that we created before with the input dict values
        check_dupe.append(input[key])
    for idx in range(0, len(check_dupe)):
        # iterates through the created list
        count: int = 0
        hold: str = check_dupe[idx]
        # hold variable holds the value from the list
        for idx in range(0, len(check_dupe)):
            # iterates through the list again but this time we have the first element held
            if hold == check_dupe[idx]:
                # increases count if a duplicate exists in the values of the dict
                count += 1
        if count >= 2:
            raise KeyError("Duplicate keys will be created!")
            # if count is equal or greater than 2
            # then this means that outside of the initial counting of the value, another dupe exists
    output: dict[str, str] = {}
    # initializing our return dict
    for key in input:
        # goes through each key-value pair
        store_key: str = key
        store_value: str = input[key]
        # holding the key and value pair
        output[store_value] = store_key
        # swapping the pair
    return output


def favorite_color(input_1: dict[str, str]) -> str:
    if len(input_1) == 0:
        return ""
        # checks for edge cases where the input dictionary is empty
    color_list: list[str] = []
    # initialize list that will hold the keys from the input dict
    favorite_count: dict[str, int] = {}
    # initalize dict that will hold the key-value pair of color and frequency
    for key in input_1:
        color_list.append(input_1[key])
        # populates list with keys from input dict
    for color in color_list:
        color_count: int = 0
        # initialize variable that will hold how many times a certain color appears
        for idx in range(0, len(color_list)):
            if color == color_list[idx]:
                # iterating through the list of colors and counting apperanace frequency
                color_count += 1
        favorite_count[color] = color_count
        # populating the dict with key-pair values of colors and their appearance frequencies
    color_count_hold: list[int] = []
    # initializing a list that will hold the appearance frequencies
    max_count: int = 0
    # initializing a variable that will hold the maximum appearance frequency
    for key in favorite_count:
        color_count_hold.append(favorite_count[key])
        # populating color_count_hold with appearance frequencies
    for key in favorite_count:
        # checking for each color
        for idx in range(0, len(color_count_hold)):
            # iterating through the appearance frequencies
            # checking the max value against the values in the dict
            if max_count < favorite_count[key]:
                max_count = color_count_hold[idx]
    for key in favorite_count:
        if favorite_count[key] == max_count:
            # matches the max value to a key
            return key
    exit()


def count(str_freq: list[str]) -> dict[str, int]:
    output_count: dict[str, int] = {}
    # initializing dict that will hold the string and it's appearance frequency
    for string in str_freq:
        # populates the output dict with the strings in the input list as keys
        output_count[string] = 0
    for key in output_count:
        # goes through each key
        for string in str_freq:
            # goes through each word in the list
            if key == string:
                # if the key and string match, add 1 to the value of the key
                output_count[key] += 1
    return output_count


def alphabetizer(catalog_list: list[str]) -> dict[str, list[str]]:
    lower_list: list[str] = []
    # initializing list that will hold the first letters of the words
    for word in catalog_list:
        lower_list.append(word[0])
        # populates lower_list with first letters
    alphabetized: dict[str, list[str]] = {}
    # initializing dict that will hold the first letter as a key
    # and the list of words starting with that letter as a value
    for letter in lower_list:
        # checks through each letter
        alphabetized[letter] = []
        # the letters becomes keys
        for word in catalog_list:
            # iterates through the input list of words
            if word[0] == letter:
                # if the first letter of the word is equal to the letter in the list
                # make it a value to the word's first letter
                alphabetized[letter] += [word]
            elif word[0].lower() == letter:
                # backup check for uppercase letters
                alphabetized[letter] += [word]
    return alphabetized


def update_attendance(
    days_and_students: dict[str, list[str]], day: str, student: str
) -> None:
    for key in days_and_students:
        # for each key it will initialize all of these variables
        students: list[str] = []
        # list that will hold individual student names
        count: int = 0
        # variable that will hold the number of appearances of a name
        # checks for duplicate names
        students += days_and_students[key]
        # populates list with the values from the dict
        if day == key:
            # enters when input day matches key
            for idx in range(0, len(students)):
                # iterates through list of students
                if student == students[idx]:
                    # if the input student name matches any of the names in the list
                    # adds 1 to count
                    count += 1
            if count == 0:
                # if count is 0 this means there are no dupes and adds the name
                days_and_students[key] += [student]
    count_1: int = 0
    # another count variable to check whether the day is present within the dict keys
    for key in days_and_students:
        # iterates through dict keys
        if key != day:
            count_1 += 1
    if count_1 == len(days_and_students):
        # if count equals the length of the dict
        # that means the day isn't in the dict as a key and adds the day and the student
        days_and_students[day] = [student]
