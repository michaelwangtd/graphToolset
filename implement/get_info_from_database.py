#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

if __name__ == '__main__':

    config = {

    }

    sql = 'select * from '

    conn = pymysql.connect(config)
    cursor = conn.cursor()
    cursor.execute(sql)
    resultSet = cursor.fetchall()