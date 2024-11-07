import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
import re
import pandas as pd

class findSystem():

    def __init__(self):
        self = self

    def ExtendedEuclidAlgo(a, b):
        
        # Base Case
        if a == 0 :
            return b, 0, 1

        gcd, x1, y1 = findSystem.ExtendedEuclidAlgo(b % a, a)

        # Update x and y using results of recursive
        # call
        x = y1 - (b // a) * x1
        y = x1

        return gcd, x, y

    # Function to give the distinct
    # solutions of ax = b (mod n)
    def linearCongruence(A, B, N):

        A = A % N
        B = B % N
        u = 0
        v = 0

        # Function Call to find
        # the value of d and u
        d, u, v = findSystem.ExtendedEuclidAlgo(A, N)

        # No solution exists
        if (B % d != 0):
            print(-1)
            return

        # Else, initialize the value of x0
        x0 = (u * (B // d)) % N
        if (x0 < 0):
            x0 += N

        # Print all the answers
        for i in range(d):
            print((x0 + i * (N // d)) % N, end = " ")
            return ((x0 + i * (N // d)) % N)

    def nounsVerbs(texts):
        lines=re.sub(r'[^a-zA-Z]', ' ', texts)  
        text = nltk.word_tokenize(lines)
        pos_tagged = nltk.pos_tag(text)


        freqs = nltk.FreqDist(text)
        allWords = [(k, v) for k, v in freqs.items()]
        world=pd.DataFrame(allWords)

        sum_all=sum(world[1])
        world=world.sort_values(1,ascending=True)

        #nouns
        np = list(filter(lambda x:x[1] == 'NN',pos_tagged))

        vb = list(filter(lambda x:x[1] == 'VB',pos_tagged))

        nounPhrases=pd.DataFrame([x[0] for x in np])

        verbPhrases=pd.DataFrame([x[0] for x in vb])


        # create frequency distribution
        fdist = nltk.FreqDist(nounPhrases)
        fdist = fdist.most_common()
        df_words = pd.DataFrame(data=fdist,columns=['nn','nn_occurences'])

        fdist1 = nltk.FreqDist(verbPhrases)
        fdist1 = fdist1.most_common()
        df_words1 = pd.DataFrame(data=fdist1,columns=['vb','vb_occurences'])

        # create math operation
        nn_sumup=sum(df_words["nn_occurences"])
        vb_sumup=sum(df_words1["vb_occurences"])

        equationEstimated=str(nn_sumup)+".X"+ " ≡ "+ str(vb_sumup) + " ( mod " + str(sum_all) + " )"

        #print ("\n\nSystem: ",equationEstimated)

        s = ""
        for i in df_words["nn"].head():
            s += str(i)+" + "

        s1 = ""
        for i in df_words1["vb"].head():
            s1 += str(i)+" + "

        s2 = ""
        for i in world[0].head():
            s2 += str(i)+" + "

        congruence = "[[ " +s+ "]] .X " +" ≡ " + "[[ " +s1+ "]]" + " mod ( " + "[[ " +s2+ "]]"+ " ) "

        return world, nn_sumup,vb_sumup,sum_all,s1,s2,equationEstimated,congruence

if __name__ == '__main__':
   #foo=findSystem()

   with open('articles.txt') as f:
        texts = f.readline()

   topchart, nn_sumup,vb_sumup,sum_all,s1,s2,equationEstimated,congruence = findSystem.nounsVerbs(texts)

   systemSolution=findSystem.linearCongruence(nn_sumup, vb_sumup, sum_all)

  # print (systemSolution)
