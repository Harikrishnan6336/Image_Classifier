# A dict to store the labels(keys) and its names(values)


def gen_labels():
    labels = {}
    with open("labels.txt", "r") as label:
        text = label.read()
        lines = text.split("\n")
        for line in lines:
            hold = line.split(" ", 1)
            labels[hold[0]] = hold[1]
    return labels
