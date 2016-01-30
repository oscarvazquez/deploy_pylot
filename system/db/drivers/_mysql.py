import mysql.connector
import collections

def _convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(_convert, data))
    else:
        return data

class MySQLConnection(object):
    def __init__(self, config):
        dbconfig = {
            'user': config.DB_USERNAME,
            'password': config.DB_PASSWORD,
            'database': config.DB_DATABASE_NAME,
            'host': config.DB_HOST,
            'port': config.DB_PORT,
        }
        dbconfig.update(config.DB_OPTIONS)
        self.conn = mysql.connector.connect(**dbconfig)

    def query_db(self, query, data=None):
        cursor = self.conn.cursor()
        data = cursor.execute(query, data)
        columns = tuple( [d[0].decode('utf8') for d in cursor.description] )
        if query[0:6].lower() != 'select':
            self.conn.commit()
            return
        else:
            for row in cursor:
                result.append(dict(zip(columns, row)))
            cursor.close()
            return _convert(result)

def connect(config):
    return MySQLConnection(config)
