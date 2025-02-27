cities = ["Amsterdam", "Tokyo", "Rio de Janeiro", "Los Angeles"]

answer = f"I would like to visit these cities: {cities[0]}, {cities[1]}, {cities[2]}, {cities[3]}"

with open("file.csv", "a") as f:
    f.write(f"task3, {answer}\n")
