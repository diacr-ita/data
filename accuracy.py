import sys
import os
from sklearn.metrics import accuracy_score


def main(truth, submission):
    D_truth={}
    D_submission={}
    with open(truth,"r") as f:
         for line in f:
             line=line.split()
             D_truth[line[0]]=int(line[1])
    with open(submission,"r") as f:
         for line in f:
             line=line.split()
             D_submission[line[0]]=int(line[1])
    y_true=[]
    y_predict=[]
    for w in D_truth.keys():
        y_true.append(D_truth[w])
        y_predict.append(D_submission[w])

    print(accuracy_score(y_true,y_predict))


if __name__ == "__main__":
    args = sys.argv
    truth = args[1]
    submission = args[2]
    if not os.path.exists(truth):
       print('Truth file doesn\'t exits.')
       exit()
    if not os.path.exists(submission):
       print('Submission file doesn\'t exits.')
       exit()
    main(truth,submission)
