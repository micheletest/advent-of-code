import sys


class totalDistance:

    def total_distance():
        location_file = sys.argv[1]
        with open(f"day1/{location_file}", "r") as f:
            table_left = []
            table_right = []
            for line in f:
                result = line.split()
                table_left.append(result[0])
                table_right.append(result[1])
        table_left.sort()
        table_right.sort()
        distance = 0
        for i in range(len(table_left)):
            distance += abs(int(table_left[i]) - int(table_right[i]))
        return distance
