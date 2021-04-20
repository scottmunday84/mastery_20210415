class JsonEncoder(object):
    def json(self):
        """
        Default method for JSON encoding.

        :return:
        """
        return vars(self)
