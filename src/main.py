#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


import sys
import logging
import app


# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



def main():
    # bootstrap
    logging.debug('bootstrapping ...')
    app.run()


if __name__ == '__main__':
    main()
    