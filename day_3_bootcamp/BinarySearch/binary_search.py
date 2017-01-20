class BinarySearch(list):
    #length and step
  def __init__(self,a,b):
    super(BinarySearch, self).__init__(range(0, (a*b)+1, b)[1:])
    self.length = a
    #searchmethod
    def search(self,arg):
        first = 0
        last = len(self) - 1
        found = False
        count = 0
        dict_ = {}
        while not found and first <= last:
            count +=1
            midpoint = (first + last)//2
            if self[last] == arg:
                found = True
            elif self[midpoint] > arg:
                last = midpoint- 1
            elif self[midpoint] < arg:
                first = midpoint+ 1
            else:
                found = True
                   
            if first == last:
                found = True
                #adding count and index to dictionary
                dict_[count] = count
                dict_[index] = -1
                return dict_

	
