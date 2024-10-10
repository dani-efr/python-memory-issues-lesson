import csv


def highscore():
    measure = "Pedestrians"

    with open("data/result.csv", "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        filtered_results = [line for line in reader if line[2] == measure]
        filtered_results.sort(key=lambda x: x[3], reverse=True)
        top_five = filtered_results[:5]

    with open("data/top_5.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(top_five)


if __name__ == "__main__":
    highscore()

