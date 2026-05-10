from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    @staticmethod
    def getAllNodes(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """with codici_Stati as (
                    select distinct(c.state1no) as codice
                    from contiguity c 
                    where c.`year` <=%s
                    )
                    select c.StateAbb ,c.CCode, c.StateNme
                    from codici_Stati cs, country c 
                    where cs.codice = c.CCode 
"""

        cursor.execute(query, (year, ))
        for row in cursor:
            res.append(Country(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllEdges(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select c.state1no as u , c.state2no as v
                    from contiguity c 
                    where c.conttype = 1
                    and c.year <= %s
                    and c.state1no < c.state2no 
                    group by c.state1no , c.state2no """

        cursor.execute(query, (year, ))
        for row in cursor:
            res.append((row["u"], row["v"]))

        cursor.close()
        conn.close()
        return res


