import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    
    import sys
    oldDistrict = None
    sum = 0
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue
        thisDistrict, registered = data_mapped
        registered = int(registered)
        if oldDistrict and oldDistrict != thisDistrict:
            print '%s\t%s' % (oldDistrict, sum)
            oldDistrict = thisDistrict
            sum = 0
        oldDistrict = thisDistrict
        sum = sum + registered
    if oldDistrict != None:
        print '%s\t%s' % (oldDistrict, sum)


reducer()
