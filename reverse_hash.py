## This program calculates the inverse of a hash value

## This function calculates the hash value for a given string
def Hash(s):
    h = 7
    letters = "acdegilmnoprstuw"
    
    for i in xrange(len(s)):
        h = h * 37 + letters.find(s[i])
        
    return h
    
## This function determines the reverse hash string for a given hash
## value given the length of the string and the hash value. It takes
## advantage of the fact that as the string increases alphabetically,
## the corresponding hash value also increases. This is used to crack
## the hashing algorithm. This shows that this hashing algorithm is
## not a good one
def reverse_hash(length, hash_val):
    temp_str = ""
    letters = "acdegilmnoprstuw"
    
    for i in xrange(length):
        for j in xrange(len(letters)):
            low = temp_str + letters[j] + letters[0] * (length-\
                len(temp_str)-1)
            high = temp_str + letters[j] + letters[-1] * \
                (length - len(temp_str)-1)
            
            if((Hash(low)<=hash_val) and (Hash(high)>=hash_val)):
                temp_str += letters[j]
                break

    if (Hash(temp_str) != hash_val):
        return "Invalid hash value for this string length"
    
    return temp_str
    
def main():
    length = 9
    hash_val = 930846109532517
    
    print reverse_hash(length, hash_val)
    
if __name__ == "__main__":
    main()
    
