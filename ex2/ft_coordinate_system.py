# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 21:06:28 by klucchin        #+#    #+#               #
#  Updated: 2026/02/22 18:34:42 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def calculate_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    return distance


def parse_coordinates(text):
    try:
        parts = text.split(",")

        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        return (x, y, z)

    except Exception as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)
        return None


def main():

    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    print("Position created:", position)

    origin = (0, 0, 0)

    distance = calculate_distance(origin, position)
    print("Distance between", origin, "and", position, ":", round(distance, 2))
    text = "3,4,0"
    print('\nParsing coordinates:', '"' + text + '"')

    parsed = parse_coordinates(text)

    if parsed:
        print("Parsed position:", parsed)

        distance2 = calculate_distance(origin, parsed)
        print("Distance between", origin, "and", parsed, ":", distance2)

    bad_text = "abc,def,ghi"
    print('\nParsing invalid coordinates:', '"' + bad_text + '"')

    parse_coordinates(bad_text)
    print("\nUnpacking demonstration:")

    if parsed:
        x, y, z = parsed
        print("Player at x =", x, ", y =", y, ", z =", z)
        print("Coordinates: X =", x, ", Y =", y, ", Z =", z)


if __name__ == "__main__":
    main()
