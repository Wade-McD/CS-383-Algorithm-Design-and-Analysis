
# Wade McDermott


class HorspoolStringMatcher:
    def __init__(self, pattern):
        # Store the pattern and build the shift table
        self.pattern = pattern
        self.shift_table = self._create_shift_table(pattern)


    def _create_shift_table(self, pattern):
        # Create the shift table based on the given pattern
        shift_table = {}
        pattern_length = len(pattern)

        # Fill shift values for all characters in the pattern except the last one
        for i in range(pattern_length - 1):
            shift_table[pattern[i]] = pattern_length - 1 - i

        # If a character isn't in the pattern, set its shift value to the pattern length
        return shift_table

    def _get_shift(self, char):
        # Return the shift value for the given character, default to the pattern length
        return self.shift_table.get(char, len(self.pattern))

    def match(self, text):
        # Find the first index of the pattern in the given text using Horspool's algorithm
        pattern_length = len(self.pattern)
        text_length = len(text)

        if pattern_length > text_length:
            return -1

        i = pattern_length - 1  # Start comparing from the end of the pattern

        while i < text_length:
            # Check for a match
            k = 0
            while k < pattern_length and self.pattern[pattern_length - 1 - k] == text[i - k]:
                k += 1

            if k == pattern_length:
                return i - pattern_length + 1  # Pattern found

            # If no match, use the shift table to skip characters
            i += self._get_shift(text[i])

        return -1  # Pattern not found

