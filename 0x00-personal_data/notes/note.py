#!/usr/bin/env python3
"""
notes and study module
resources : 
    https://docs.python.org/3/library/logging.html

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
