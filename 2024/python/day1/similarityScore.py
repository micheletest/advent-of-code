import sys


class similarityScore:

    def similarity_score():
        location_file = sys.argv[1]
        with open(f"day1/{location_file}", "r") as f:
            table_left = []
            table_right = []
            for line in f:
                result = line.split()
                table_left.append(result[0])
                table_right.append(result[1])

        score = 0
        for number in table_left:
            occurrences = table_right.count(number)
            score += int(number) * occurrences
        return score
