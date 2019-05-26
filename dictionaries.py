# dictionaries.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    '''
    - creation
    '''
    # create an empty dictionary named "dict" and print it

    dict = {}

    # open your book to p. 401
    # create the "passwd" dictionary and print it

    passwd = {'guido':'superprogrammer', 'turing':'genius', 'bill':'monopoly'}

    print (passwd)
    print ()

    '''
    - element access
    '''
    # using the square bracket notation print out the value for "turing"

    print (passwd['turing'])
    print ()

    '''
    - element updates
    '''
    # using the square bracket notation update the value for "turing" 
    # to "super genius", then print the dictionary

    passwd ['turing'] = 'super genius'
    print (passwd)
    print ()

    '''
    - element insertion
    '''
    # add a new key value pair to passwd
    # key = "new key"
    # value = "new key value"

    passwd ['new key'] = 'new key value'

    # print passwd

    print (passwd)
    print ()

    '''
    - element deletion
    '''
    # delete "turing" from passwd and print passwd

    del passwd ['turing']

    print (passwd)
    print ()

    '''
    - search
    '''
    # print the result of get("turing")

    print (passwd.get('turing'))
    print ()

    # Use the "in" keyword to search the dictionary
    # print the value returned by ' "turing" in passwd '

    print ('turing' in passwd)

    '''
    - some dictionary methods
    '''
    # print the list of keys

    print (passwd.keys())
    print ()

    # print the list of values

    print (passwd.values())
    print ()

    # print the list of items - key-value pairs

    print (passwd.items())
    print ()

    '''
    - deletion
    '''
    # delete all entries from passwd, then print it

    passwd.clear()
    
    print (passwd)
    print ()

main()