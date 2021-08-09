import os
import json

from tqdm import tqdm

if __name__ == '__main__':
    dataf = open("CONALA/conala-mined.jsonl", "r").readlines()

    train = True
    for id, line in enumerate(tqdm(dataf)):
        obj = json.loads(line)
        v = obj["intent"]
        v1 = obj["snippet"]
        if id % 5 == 0:
            train = False
        path = "CONALA/{}/{}".format("train" if train else "test", id)
        os.mkdir(path) if not os.path.exists(path) else None
        question = open(os.path.join(path, "question.txt"), "w")
        question.write(v)
        question.close()
        solution = open(os.path.join(path, "solution.json"), "w")
        v1 = [v1]
        json.dump(v1, solution)
        train = True
