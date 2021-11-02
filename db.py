import pymysql
from flask import jsonify




def query(querystr, returnJSON = True):
    connection = pymysql.connect(
        host= "vehicle-gatepass.cea0wclj3noo.ap-southeast-1.rds.amazonaws.com",
        user = "admin",
        password="Icandoit",
        db = "Vehicle_GatePass_CBIT",
        cursorclass=  pymysql.cursors.DictCursor
    )

    connection.begin()
    cursor = connection.cursor()
    cursor.execute(querystr)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    if returnJSON:
        return jsonify(result)
    else:
        return result

