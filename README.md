# From Machine Translation to Code-Switching: Generating High-Quality Code-Switched Text

full paper - https://aclanthology.org/2021.acl-long.245.pdf
poster - TODO

## Introduction

## Data



### All-CS

The dataset we collected is All-CS.json

The data for PRETRAIN, OpSub-LEX and OpSub-EMT is not uploaded on github because of size. Please contact Ishan Tarunesh (ishantarunesh@gmail.com) and Syamantak Kumar (syamantak.kumar@gmail.com) to get the data.

## Pre-Processing
Run preprocess_data.sh to download the required tools for preprocessing. 
```
Moses found in: /Users/ishan/Desktop/UnsupervisedMT/NMT/tools/mosesdecoder
fastBPE found in: /Users/ishan/Desktop/UnsupervisedMT/NMT/tools/fastBPE
fastBPE compiled in: /Users/ishan/Desktop/UnsupervisedMT/NMT/tools/fastBPE/fastBPE/fast
fastText found in: /Users/ishan/Desktop/UnsupervisedMT/NMT/tools/fastText
fastText compiled in: /Users/ishan/Desktop/UnsupervisedMT/NMT/tools/fastText/fasttext
Extracting vocabulary...
```
### Possible errors you might get on running preprocess_data.sh

```
Traceback (most recent call last):
  File "/Users/ishan/Desktop/UnsupervisedMT/NMT/preprocess.py", line 28, in <module>
    dico = Dictionary.read_vocab(voc_path)
  File "/Users/ishan/Desktop/UnsupervisedMT/NMT/src/data/dictionary.py", line 111, in read_vocab
    assert line[0] not in word2id and line[1].isdigit(), (i, line)
AssertionError: (4, ['<unk>', '1322901'])
```

=> In that case you must be running the original src/data/dictionary.py file. We slightly modified the file on line 110-112 to accomodate for <unk> token. Use the src/data/dictionary.py file from this repository.

```
Traceback (most recent call last):
  File "/Users/ishan/Desktop/UnsupervisedMT/NMT/preprocess.py", line 31, in <module>
    data = Dictionary.index_data(txt_path, bin_path, dico)
  File "/Users/ishan/Desktop/UnsupervisedMT/NMT/src/data/dictionary.py", line 132, in index_data
    assert dico == data['dico']
AssertionError
```

=> This means the vocab dictionary in your .pth files don't match vocab.all file. The .pth file must be outdated. Delete the .pth files and re-run preprocess_data.sh
=> rm -r data/*/*.pth

## Running TCS Model

## Other Experiments
