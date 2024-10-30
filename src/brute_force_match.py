# Wade McDermott, Ronen Rosenberg, Ishan Abraham, Suri Castro


# Brute force 2D pattern matching algorithm

def match(pattern, text):
    n = len(text)
    m = len(pattern)

    # Traverse each possible top-left corner of an m x m region in the text
    for i in range(n-m+1):
        for j in range(n-m+1):
            # Assume a match til proven otherwise
            match_found = True

            # Check everything in an m x m sub-region
            for k in range(m):
                for l in range(m):
                    if text[i+k][j+l] != pattern[k][l]:
                        match_found = False
                        break

                if not match_found:
                    break

            # If a match is found return the starting coordinates
            if match_found:
                return (i,j)

    # Return None if no match is found
    return None