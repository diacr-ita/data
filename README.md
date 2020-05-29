# data


## Vertical to Flat Corpus

To turn the vertical corpus into a flat one, you can run the following script:
```
python3 vertical2corpus.py folder_in folder_out mode
```

You can choose to flat raw text, lemmas or pos tags:

Raw text
```
python3 vertical2corpus.py folder_in folder_out 0
```

Lemmas
```
python3 vertical2corpus.py folder_in folder_out 1
```

Raw text concatenated with Pos tags
```
python3 vertical2corpus.py folder_in folder_out 2
```

Lemmas concatenated with Pos tags
```
python3 vertical2corpus.py folder_in folder_out 3
```

## Accuracy

We provided the script will be used during the evaluation to compute the accuracy of your submission against the truth labels:

```
python3 accuracy.py truth.txt your_submission.txt
```

You need the sklearn package to run this script.
