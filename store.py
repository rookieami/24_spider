#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from os import path

from mysql.connector.pooling import MySQLConnectionPool
config = configparser.ConfigParser()
config.read(path.join(path.dirname(path.realpath(__file__)), './config.ini'))




if __name__=='__main__':
    for s, kv in config.items():
        print(s)
        for k, v in kv.items():
            print('\t', k, '=', v)
ds=MySQLConnectionPool(pool_size=2,**config['database'])
req_url=config.get('server','url')