"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 7.10 - Scoring the Dancing Games:
 Implement the function calculate_average, which takes the dict as a
  parameter and calculates the average from the song percentage values,
  which is also the return value of the function.

Learning Goals:
 Getting acquainted with Python's documentation for dict.
"""

SONG_RESULT = {"Bubble dancer": 93.4, "The Game": 92.03, "Vertex": 75.3,
               "Lemmings on the Run": 86.2, "Da Roots": 96.02,
               "Charlene": 75.3, "Disconnected": 86.3, "Fly away": 87.32,
               "Hybrid": 63.9, "My favourite game": 89.45, "Oasis": 59.5,
               "Remember December": 96.3, "The beginning": 90.45,
               "Tribal Style": 87.45, "Why Me": 97.38, "Xuxa": 63.84,
               "Zodiac": 83.43, "Queen of Light": 75.12, "Mouth": 98.34,
               "Pandemonium": 79.31}

def calculate_average(result):
    """Calculate the average from the song percentage values.

    :param result: A dict of song names and their percentage values.

    :return: The average from the song percentage values.
    """
    total = sum(result.values())
    # Check if the dict is empty to avoid division by zero.
    if len(result) == 0:
        return 0
    return total / len(result)


def main():
    print(calculate_average(SONG_RESULT))

if __name__ == "__main__":
    main()