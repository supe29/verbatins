from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

#ROOT_DIR = Path('../')
#MODELS_DIR = ROOT_DIR / 'models'


def Nlp(df):
    print("Nlp")
    #df = pd.read_csv("nlp.csv")
    df_processed = cleaned(df)
    #dfscore = sentiment_score(df_processed)
    datafile = Sentimentcsv(df_processed)
    return datafile

#cleaning of data

def cleaned(df):
    print("cleaned")
    df['answer'] = df['answer'].fillna("-")
    df = df.drop(['uuid'], axis=1)
    return df

    
def sentiment_score(x):
    print("sentiment_score")
    tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    #print(x)
    tokens = tokenizer.encode(x, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1

def Sentimentcsv(data):
    print("Sentimentcsv")
    data['sentiment'] = data['answer'].apply(lambda x: sentiment_score(x[:512]))
    print("data-to-csv")
    data.to_csv("sent.csv", encoding='utf-8', index=False)

