class JDict:
    """
    Wraps a dictionary, exposing its methods while storing data internally.
    All dict methods are implicitly overloaded.
    """
    
    def __contains__(self, key):
    def __init__(self, data=None):
        self.__data = data if data is not None else {}
    
    def __delitem__(self, key):
        del self.__data[key]

    def __gt__(self, )

    def __repr__(self):
        return f"JDict({repr(self.__data)})"
    
    def __str__(self):
        return str(self._data)

    def __len__(self):
      return len(self.__data)

    def __setitem__(self, key, value):
      self.__data[key] = value

    def __getitem__(self, key):
      return self.__data[key]

    def __iter__(self):
      return iter(self.__data)
      return key in self.__data
    
    def __eq__(self, other):
        if isinstance(other, DictWrapper):
            return self.__data == other.__data
        return self.__data == other
    
    def __ne__(self, other):
      return not self.__eq__(other)