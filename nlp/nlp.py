import gensim
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from sklearn.metrics import jaccard_score
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk import sent_tokenize
import re , string
from django.conf import settings
import numpy as np
from scipy import spatial
from gensim.models.word2vec import Word2Vec
from string import punctuation
import language_check
import spacy
from .models import WModels


model=None

try:
    nlp = spacy.load("en_core_web_sm")
    tool = language_check.LanguageTool('en-US')
    print("en_core_web_sm is Loaded")
except:
    print("Not able to en_core_web_sm")
    pass



def process_text(data):
    total_error = 0;correct=[];errors=[]
    for line in data:
        line = re.sub("[^a-zA-z+$+\d]"," ", line)
        matches = tool.check(line.lower());
        for mistake in matches:
            try:
                error = mistake.context[mistake.contextoffset:mistake.contextoffset+mistake.errorlength]
                replacer = mistake.replacements[0]
                line=(line.replace(error,replacer))
                errors.append(mistake.category)
            except:
                pass
        correct.append(line)

        for i in list(set(errors)):
            if not i =="Possible Typo" or i == "Capitalization":
                total_error=total_error+1
        print(total_error,list(set(errors)))

    return({"correct":correct,"len":len(correct),"error":total_error,"errortypes":list(set(errors))})



def preproc_data(sent, model):
    vec_sent = []
    for i,word in enumerate(sent):
        try:
            vec_sent.append(model.wv[word])
        except:
            pass
    vec_sent = sum(np.asarray(vec_sent))
    result = vec_sent.reshape(1,-1)
    return result



def remove_noise(tweet_tokens,stop_words):
    cleaned_tokens = [];
    for token, tag in pos_tag(tweet_tokens):
        token = re.sub("[^a-zA-z+.+$+\d]"," ", token)

        if len(token)<=1 : token='' 
        
        if tag.startswith("NN"): 
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        
        lemmatizer = WordNetLemmatizer()      
        token = lemmatizer.lemmatize(token, pos)
            
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())

    return cleaned_tokens


def getallmodels(_subj):
    for i in WModels.objects.all().order_by(-id).values():
        if i['subj_id'] == _subj:
            print({"subj":i['subj_id'],"file":i['file']})
            return({"subj":i['subj_id'],"file":i['file']})
    return False


def loadModel(subj):
    if len(subj)>0:
        print(subj[0].subject)
        name=getallmodels(subj[0].subject)
        if name:
            model = gensim.models.Word2Vec.load(settings.MEDIA_ROOT+'\\'+name['file'])
            print("Model Load "+settings.MEDIA_ROOT+'\\'+name['file'])
        else:
            print("No Model Founded so default spacy model is loaded ")
            return False
    else:
        print("No Model Founded so default spacy model is loaded ")
        return False


def simalarity(sent1,sent2,*subj):
    Word2Vec=0;jaccard=0;WordMover=0;doc_sim=0;_stopwords=False;_stopword=stopwords.words('english')

    sent1_token=sent_tokenize(sent1)
    sent2_token=sent_tokenize(sent2)

    sent1_correct=process_text(sent1_token)
    sent2_correct=process_text(sent2_token)


    sen1=remove_noise(sent1_correct['correct'][0].split(),_stopword)
    sen2=remove_noise(sent2_correct['correct'][0].split(),_stopword)


    try:
        ling1=lingustic_features(nlp(sent1_correct['correct'][0]))
        ling2=lingustic_features(nlp(sent2_correct['correct'][0]))
    except:
        pass

    try:
        if loadModel(subj):
            w2v_sent1 = preproc_data(sen1,model)
            w2v_sent2 = preproc_data(sen2,model)
            Word2Vec=cosine_similarity(w2v_sent1,w2v_sent2)[0][0]
        else:
            w2v_sent1 = nlp(" ".join(sen1))
            w2v_sent2 = nlp(" ".join(sen2))
            Word2Vec=w2v_sent1.similarity(w2v_sent2)
    except:
        pass    

    try:
        jaccard=1-gensim.matutils.jaccard(sen1,sen2)
    except:
        pass

    for token in stopwords.words('english'):
        if token in sent2_correct['correct'][0].split():
            _stopwords=True


    data=({"Word2vec_sim":Word2Vec,"jaccard_sim":jaccard,
    "sent1":sent1_correct,"sen2":sent2_correct,
    "clean_sen1":sen1,"clean_sen2":sen2,
    "lingustic_features_sent1":{"NER":ling1[0]},
    "lingustic_features_sent2":{"NER":ling2[0]},
    "stopwords":_stopwords })

    return data



def lingustic_features(doc):
    try:
        noun=[chunk.text for chunk in doc.noun_chunks];ner=[]
        verb=[token.lemma_ for token in doc if token.pos_ == "VERB"]

        for token in doc.ents:
            ner.append(str(token))
    except:
        pass

    return ner,noun,verb
