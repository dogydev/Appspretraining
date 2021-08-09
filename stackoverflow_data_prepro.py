import os
import pickle
import json

if __name__ == '__main__':
    data = pickle.load(open("APPS/python_how_to_do_it_qid_by_classifier_unlabeled_single_code_answer_qid_to_code.pickle", "rb"))
    labels = pickle.load(open("APPS/python_how_to_do_it_qid_by_classifier_unlabeled_single_code_answer_qid_to_title.pickle", "rb"))
    train = True
    for id, ((k, v), (_, v1)) in enumerate(zip(labels.items(), data.items())):
        if id % 5 == 0:
            train = False
        path = "STQA/{}/{}".format("train" if train else "test", id)
        os.mkdir(path) if not os.path.exists(path) else None
        question = open(os.path.join(path, "question.txt"), "w")
        question.write(v)
        question.close()
        solution = open(os.path.join(path, "solution.json"), "w")
        v1 = [v1]
        json.dump(v1, solution)
        print(k, v, v1)
        train = True



