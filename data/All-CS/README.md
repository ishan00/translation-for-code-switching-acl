## All-CS
The All-CS.json file contains the All-CS data as mentioned in our work - "From Machine Translation to Code-Switching: Generating Realistic Code-Switched Text"

Each entry in the file contains the following fields :

1. dataset - This field can either be "moviecs" or "treebankcs", to signify whether the entry comes from the moviecs dataset or the treebankcs dataset.
2. id - This field signifies the id (identifier) of the field. The id is different for moviecs and treebankcs datasets.
3. split - This field denotes the part of the split which the entry is a part of. It can either be "train", "test" or "valid".
4. mono_raw - This is the original monolingual sentence.
5. mono - This is the monolingual sentence labelled with named entity tags. The named entities are identified by a "/NE/" label appended at the end of the word.
6. mturk - This field contains the responses obtained from Amazon Mechanical Turk, labelled with named-entity tags. 
7. gold - This field contains the gold response obtained by the professional annotation company. It is only available for the moviecs dataset.
8. eng_google - This field contains the english translation of the monolingual sentence obtained using Google Translate. Named-Entity tags have been provided in each sentence.

## All-CS-With-Synthetic
We also generated synthetic code-switched sentences using the monolingual Hindi lines from All-CS (Used to Human Evaluation, BERTScore, Classifier Experiments). We generate 5 sentences for each of the 4 methods - LEX, EMT, TCS(U) and TCS(S). In the file All-CS-With-Synthetic.json you can file additional fields for LEX, EMT, TCS(U) and TCS(S) along with the fields from above.

## Converting All-CS to {hi/en}.{train/test/valid} files

For running TCS model, we need the data to be in the following format (6 files) - hi.train, hi.test, hi.valid, en.train, en.test, en.valid. There files are already added in the folder but can be generated again from All-CS by running extract.py

The same test and valid files (en.test and en.valid) are used for future experiments too (LM, BertScore etc)

Understanding extract.py
=> For test and valid sentences we use gold label if available in the data else we use the first mturk sentence as the gold.
=> For train sentences we use gold and all of mturk data. The train data is shuffled.