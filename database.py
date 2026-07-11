import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-1b05ff08-huynhngocnamphuong-6826.h.aivencloud.com",

        port=20489,

        user="avnadmin",

        password="AVNS_Dmb0OneUoIoLTKl2-A-",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
