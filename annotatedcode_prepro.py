import os
import json

if __name__ == '__main__':
    dataf = open("AnnotatedCode/all.code", "r")
    labelsf = open("AnnotatedCode/all.anno", "rb")

    data = dataf.readlines()
    labels = labelsf.readlines()

    train = True
    for id, (v, v1) in enumerate(zip(labels, data)):
        if id % 5 == 0:
            train = False
        v = v.decode("utf-8")
        path = "AnnotatedCode/{}/{}".format("train" if train else "test", id)
        os.mkdir(path) if not os.path.exists(path) else None
        question = open(os.path.join(path, "question.txt"), "w")
        question.write(v)
        question.close()
        solution = open(os.path.join(path, "solution.json"), "w")
        v1 = [v1]
        json.dump(v1, solution)
        train = True
