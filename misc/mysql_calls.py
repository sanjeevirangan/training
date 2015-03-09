import MySQLdb
import time

"""
DB module for web API.
Contains 'MySqlCalls' class.
"""


class MySqlCalls(object):
    """
    Class: MySqlCalls
    args: host='localhost', user='root', pwd='admin', db='login_test', charset_val='utf8'
    desc: Creates MySQLdb cursor objects and provides methods to execute the query, commit the db and closes it.
    The read-only property get_total_execution_time() would be invalid if called before closing the db.
    """

    def __init__(self, host='localhost', user='root', pwd='admin', db='product_relation', charset_val='utf8'):
        """
        :param host:
        :param user:
        :param pwd:
        :param db:
        :param charset_val:
        """
        self.err_list = []
        self.response = {}
        self.__is_error = False
        self.__error_list = []
        self.__execute_start = 0
        self.__execute_end = 0
        self.__commit_start = 0
        self.__commit_end = 0
        self.__close_start = 0
        self.__close_end = 0
        self.__db = MySQLdb.connect(host, user, pwd, db, charset=charset_val)
        self.__cursor = self.__db.cursor()

    def execute_query(self, query, values):
        """
        :param query: Sql query to be executed without any values
        :param values: Comma separated values internally delimited by a ';' ex: "1;a;x,2;b;y" or "1,2,3"
        """
        self.__execute_start = time.time()
        for value in values:
            try:
                args = value.split(';')
                self.__cursor.execute(query, args)
            except Exception, ex:
                self.__is_error = True
                self.__error_list.append(ex.message)
                self.response['Query-Error'] = ex.message
        self.__execute_end = time.time()
        self.response['Query-Execution-Time'] = str(self.__execute_end - self.__execute_start) + " seconds"
        self.response['Query-Execution-Count'] = str(len(values))

    def commit_db(self):
        """
        Commits the db.
        """
        try:
            self.__commit_start = time.time()
            self.__db.commit()
        except Exception, ex:
            self.__is_error = True
            self.__error_list.append(ex.message)
            self.response['DB-Commit-Error'] = ex.message
        else:
            self.__commit_end = time.time()
            self.response['DB-Commit-Time'] = str(self.__commit_end - self.__commit_start) + " seconds"

    def close_db(self):
        """
        Closes the db.
        """
        try:
            self.__db.close()
            self.__close_start = time.time()
        except Exception, ex:
            self.__is_error = True
            self.__error_list.append(ex.message)
            self.response['DB-Close-Error'] = ex.message
        else:
            self.__close_end = time.time()
            self.response['DB-Close-Time'] = str(self.__close_end - self.__close_start) + " seconds"

    def has_errors(self):
        """
        :rtype : bool
        :return:
        """
        res = False
        if self.__is_error:
            self.err_list = list(self.__error_list)
            res = True
        return res

    @property
    def get_total_execution_time(self):
        """
        :rtype : str
        :return: string of total execution time
        """
        return str(self.__close_end - self.__execute_start)
