import csv
import random
import math
import sys


# Phan chia tap du lieu theo class
def separate_data(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    # print(separated)
    return separated


# Phan chia tap du lieu thanh training va testing.
def split_data(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))

    return [trainSet, copy]


# tinh toan gia tri trung binh cua moi thuoc tinh
def mean(numbers):
    sum = 0.0
    for i in numbers:
        sum += float(i)
    return sum / float(len(numbers))


# Tinh toan do lech chuan cho tung thuoc tinh
def standard_deviation(numbers):
    avg = mean(numbers)
    variance = sum([pow(float(x) - avg, 2) for x in numbers]) / float(len(numbers))
    return math.sqrt(variance)


# Gia tri trung binh , do lech chuan
def summarize(dataset):
    summaries = [(mean(attribute), standard_deviation(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarize_by_class(dataset):
    separated = separate_data(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)

    return summaries


# Tinh toan xac suat theo phan phoi Gause cua bien lien tuc
def calculate_prob(x, mean, stdev):
    exponent = math.exp(-(math.pow(float(x) - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


# Tinh xac suat cho moi thuoc tinh phan chia theo class
def calculate_class_prob(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            if stdev == 0:
                stdev = 999999999999
            x = inputVector[i]
            probabilities[classValue] *= calculate_prob(x, mean, stdev)

    return probabilities


# Du doan vector thuoc phan lop nao
def predict(summaries, inputVector):
    probabilities = calculate_class_prob(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue

    return bestLabel


# Du doan tap du lieu testing thuoc vao phan lop nao
def get_predictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)

    return predictions


# Tinh toan do chinh xac cua phan lop
def get_accuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1

    return (correct / float(len(testSet))) * 100.0


def get_data_label(dataset):
    data = []
    label = []
    for x in dataset:
        data.append(x[:29])
        label.append(x[-1])
    return data, label


def main():
    dataset = [50]
    filename = 'Book5k1.csv'
    splitRatio = 0.8
    count = 0
    lines = csv.reader(open(filename, "r", ))
    dataset = list(lines)
    # print(dataset)
    for row in dataset:
        # print(' '.join(row))
        for i in row:
            dataset[count] = row
        count = count + 1
        if count > 50:
            break

    # print("len of dataset: " + str(len(dataset)))
    trainingSet, testSet = split_data(dataset, splitRatio)

    # prepare model
    summaries = summarize_by_class(trainingSet)
    get_data_label(trainingSet)

    # # test model
    predictions = get_predictions(summaries, testSet)
    accuracy = get_accuracy(testSet, predictions)
    print('Accuracy:' + accuracy.__str__())


if __name__ == "__main__":
    main()
