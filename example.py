import random
PRIME = 8209
N = 8193
R_WAY = 22
B_WAY = 44
NUM_HASHES =  R_WAY * B_WAY

def mapper(key, value):
    # key: None
    # value: one line of input file

    # process document to get to binary rep

    doc_arry = value.split(" ")

    doc_name_int = int(doc_arry[0].split("_")[1])

    print doc_name_int

    doc_bin_arr = [0] * N
    for num_str in doc_arry[1:]:
        num_int = int(num_str)
        doc_bin_arr[num_int] = 1

    # do 1024 minhash
    random.seed("weareawesome")

    minhash_arr = []

    for i in xrange(0,NUM_HASHES):
        a = random.randint(0, 1000000)
        b = random.randint(0, 1000000)

        # print "new hash"
        min_so_far = N
        for row in xrange(0, N):
            hashed = ((a * row + b) % PRIME) % N
            # print "hashed", hashed

            if doc_bin_arr[row] == 1:
                # print hashed
                min_so_far = min(hashed, min_so_far)

        minhash_arr.append(min_so_far)

    # output r slices of the array
    # print minhash_arr
    for i in xrange(0, NUM_HASHES, R_WAY):
        yield str(minhash_arr[i: i + R_WAY]), doc_name_int



def reducer(key, values):
    # key: key from mapper used to aggregate
    # values: list of all value for that key
    # print key, values
    values.sort()

    for idx, doc1 in enumerate(values):
        for doc2 in values[idx + 1:]:
            print "answer: ", doc1, doc2
            yield doc1, doc2