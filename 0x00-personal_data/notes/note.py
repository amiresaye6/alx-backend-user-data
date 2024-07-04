#!/usr/bin/env python3
"""
notes and study module
resources : 
    https://docs.python.org/3/library/logging.html


# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

"""
# myapp.py
import logging
import mylib
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO,
                        format="%(asctime)s:%(module)s:%(lineno)d:<<%(message)s>>")
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished here my frind')

if __name__ == '__main__':
    main()




# # test
# fields = ["password", "date_of_birth", 'email']
# messages = [
# "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
# "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
#     ]

# for message in messages:
#     print(filter_datum(fields, 'xxx', message, ';'))
