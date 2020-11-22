
def get_infos(info_code, conn):

    try:

        cur= conn.cursor()
        sql="select info_desc from taux_infos where info_code = '" + info_code + "';"
        cur= conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if cur.rowcount > 0:
            return rows[0][0]
        else:
            return ""
    except Exception as e:
        print(str(e))
        return ""


