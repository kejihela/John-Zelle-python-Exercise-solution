def byfreq(pair):
    return pair[1]

def main():
    print("this is for word count")
    fname = input("Please, insert your file name: ")
    text = open(fname, "r").read()
    text = text.lower()
    for ch in '!"#$%&0*+,-./:;<=>?<0[\\]-_{1}-':
        text = text.replace(ch, " ")
    word = text.split()
    
    count = {}
    for w in word:
        count[w] = count.get(w,0) + 1

    n = eval(input("analysis of how many words"))
    item = list(count.items())
    item.sort()
    item.sort(key=byfreq, reverse=True)
    for i in range(n):
        word,count = item[i]
        print("{0:<15}{1:>5}".format(word,count))

if __name__ =="__main__": main()
     
