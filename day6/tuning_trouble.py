def find_start_of_packet(data):
    # The number of characters to look for in the datastream
    # (4 for part one, 14 for part two)
    num_chars = 14

    # Keep track of the characters we have seen so far
    seen = set()

    # Iterate through the characters in the datastream
    for i, c in enumerate(data):
        # Add the character to the set of seen characters
        seen.add(c)

        # If we have seen num_chars characters, check if they are all unique
        if len(seen) == num_chars:
            # Check if the last num_chars characters are all unique
            if len(set(data[i - num_chars + 1 : i + 1])) == num_chars:
                # If they are, return the number of characters processed so far
                return i + 1


if __name__ == "__main__":
    with open("input.txt") as file:
        datastream = file.read()
        marker = find_start_of_packet(datastream)
        print(f"marker is at {marker}")
