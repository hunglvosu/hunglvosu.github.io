from fnv import *
import uuid
import string
import time


start = time.time()
inputfile = "question_150k.tsv"
outputfile = "question_sim_150k.tsv"
r = 6
s = 14      # s here is the number of hash tables, in the lecture we denote by b instead of s
x = 0.6     # the similarity threshold
p = 15373875993579943603
a = [None]*(r*s)
b = [None]*(r*s)
for i in range(r*s):    # we will need r*s hash functions
    a[i] = uuid.uuid4().int & (1<<64)-1
    b[i] = uuid.uuid4().int & (1<<64)-1

def linearhash(data: int, j: int) -> int:
    return (a[j]*data + b[j]) % p

def jaccard_sim(question1: string, question2 : string) :
    X = set(question1.split())
    Y = set(question2.split())
    intersection = X & Y
    union = X | Y
    return len(intersection) / len(union)

word_to_int = {}
def minhash_sig(question: string, i : int) -> string:  # 0 <= i <= s-1
    minhashcode = [None]*r  # the signature is an r-tuple of min-hash codes
    for j in range(r):
        minhashcode[j] = 0x7FFFFFFFFFFFFFFF
    signature = ""
    for word in question.split():
        if word not in word_to_int :
            word_in_bytes = word.encode('utf-8')
            fnv_code = hash(word_in_bytes, bits=64) # map each word into a 64-bit integer
            word_to_int[word] = fnv_code
        for j in range(r):
            hashcode = linearhash(word_to_int[word],i*r+j)
            if(hashcode < minhashcode[j]) :
                minhashcode[j] = hashcode
    for j in range (r):
        signature += str(minhashcode[j])
    return signature

def set_to_string(set) :
    set_string = ""
    for element in set :
        set_string += str(element) + ","
    return set_string.rstrip(',')

question_to_qid = {}   # this map each question to a qid
qid_to_question = {}    # this map each qid to an actual question
header = True
with open(inputfile,"r") as file:
    for line in file:
        if header :     # skip the header line
            header = False
            continue
        chunks = line.split('\t')
        if len(chunks) < 2:
            continue
        qid = chunks[0].strip()
        question = chunks[1].strip()
        question_to_qid[question] = qid
        qid_to_question[qid] = question

print("Building the locality sensitive data structure\n")
T = [None]*s
for i in range(s):
    T[i] = {}
# construct the locality sensitive data structure
linecount = 0
with open(inputfile,"r") as file:
    for line in file:
        linecount += 1
        if linecount == 1 : # skip the header
            continue
        if linecount % 10000 == 0 :
            print("Processed " + str(linecount) + " lines\n")
        chunks = line.split('\t')
        if len(chunks) < 2:
            continue
        question = chunks[1].strip()
        for i in range(s) : # fill in the i-th hashtable
            signature = minhash_sig(question, i)
            if signature not in T[i] :
                T[i][signature] = []
            T[i][signature].append(question_to_qid[question])


f = open(outputfile, "w")
f.write("qid\tsimilar-qids\n")
print("Finding similar questions\n")
linecount = 0
with open(inputfile,"r") as file:
    for line in file:
        linecount += 1
        if linecount == 1 : # skip the header
            continue
        if linecount % 10000 == 0 :
            print("Processed " + str(linecount) + " lines\n")
        chunks = line.split('\t')
        if len(chunks) < 2:
            continue
        question = chunks[1].strip()
        curr_qid = question_to_qid[question]
        simset = set()
        for i in range(s):
            signature = minhash_sig(question, i)
            if len(T[i][signature]) > 0:
                simset.update(T[i][signature])
        simset.remove(curr_qid) # remove a question from its own similarity set
        false_positives = set()
        for qid in simset :
            if(jaccard_sim(question, qid_to_question[qid])) < x :
                false_positives.add(qid)
        for qid in false_positives :
            simset.remove(qid)
        f.write(curr_qid + "\t" + set_to_string(simset)+ "\n")
f.close()
end = time.time()
print(end - start)
