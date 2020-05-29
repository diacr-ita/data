#Development Data

This folder contains development data for the Diacr-Ita task.

In the folder "vertical" you can find "corpus_0.txt" and "corpus_1.txt", which are namely the vertical corpus for the first period and the vertical corpus for the second period.

Both corpus and target are merely representatives of the task format. Targets are randomly selected.
Labels in the "truth.txt" file are randomly assigned.


## Vertical to Flat Corpus

To turn the vertical corpus into a flat one, you can run the following script:

python3 vertical2corpus.py folder_in folder_out label

You can choose to flat raw text, lemmas or pos tags:

Raw text
python3 vertical2corpus.py folder_in folder_out 0

Lemmas
python3 vertical2corpus.py folder_in folder_out 1

Raw text concatenated with Pos tags
python3 vertical2corpus.py folder_in folder_out 2

Lemmas concatenated with Pos tags
python3 vertical2corpus.py folder_in folder_out 3

## Accuracy

We provided the script will be used during the evaluation to compute the accuracy of your submission against the truth labels:

python3 accuracy.py truth.txt your_submission.txt

You need the sklearn package to run this script.
