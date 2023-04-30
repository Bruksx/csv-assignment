import csv

def get_data():
    data = []
    with open("input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data.append(row)
    return data

def main():
    item_to_level = {}
    output = []

    data = get_data()
    first_item = data[0][0]
    first_collected_item = data[0][1]

    item_to_level[first_item] = 1
    output.append([first_item, first_collected_item, 1])

    for i in range(1, len(data)):
        level = 1
        item = data[i][0]
        collected_item_ = data[i][1]
        for j in range(0, i):
            collected_item = data[j][1]
            if collected_item.strip() == item:
                level += item_to_level[data[j][0]]
        item_to_level[item] = level
        output.append([item, collected_item_, level])

    return output

for i in main():
    print(i)