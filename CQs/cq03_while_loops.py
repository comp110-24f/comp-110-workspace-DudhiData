"""While Loops Challenge Questions #3"""

__author__ = "730756130"

"""function num_instances takes two string parameters"""


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    """count variable will count the # of appearances of search_char in phrase"""
    index: int = 0
    """index variable will help us move through the full phrase and check each letter"""
    """while loop checks through full phrase, len(phrase)-1 accounts for python indices starting at 0"""
    while index <= (len(phrase) - 1):
        """conditional checks whether certain letter of phrase equals the search_char"""
        if search_char == phrase[index]:
            count = count + 1
            """search_char equals the specific phrase letter, so count increases by 1"""
        index = index + 1
        """regardless of whether search_char equals phrase, index has to increase by 1"""
    return count


print(num_instances(phrase="HelloheLLo", search_char="L"))
