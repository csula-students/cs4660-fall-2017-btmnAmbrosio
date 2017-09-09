"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        from io import open 
        f = open(file_path, encoding='utf-8')
        for rows in f:
            self.numbers.append(rows.split())
        
        # for rows in self.numbers:
        #     for nums in rows:
        #         nums= int(nums)

        # from builtins import map
        # self.numbers = list(map(int,self.numbers))

        self.numbers=[[int(y) for y in x] for x in self.numbers]

        
        
        f.close()



        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        mean = 0.0
        mean = (sum(self.numbers[line_number])//(len(self.numbers[line_number])))
        return mean

        

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        return max(self.numbers[line_number])



    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        return min(self.numbers[line_number])

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        return sum(self.numbers[line_number])
