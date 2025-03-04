class TaggedList:
    def __init__(self,data,tags):
        self._data = data[:]
        self._tags = tags[:]
        self._tagIdx={}
        for i in range(len(tags)):
            self.tagIdx[tags[i]]=i
    
    def __len__(self):
        return len(self._data)

    def __str__(self):
        result = ""
        for i in range(len(self._data)):
            result += self._tags[i]+":"+str(self._data)
        return result

    def __contains__(self,x):
        return x in self.__data__
    
    def __getitem__(self,index):
        if isinstance(index, int):
            return self._data[index]
        elif isinstance(index,str):
            return self.__data[self. tagIdx[index]]
        else:
            raise Exception("wrong key type")
        
    def __setitem__(self,index,item):
        if isinstance(index,int):
            self._data[index]= item
        else:
            self._data[self._tagIdx[index]]= item

a = TaggedList([70,80,90,100],["语文","数学","英语","物理"])

print(len(a),78 in a, 80 in a)

print(str(a))#>>语文:70,数学:80,英语:90,物理:100，

print(a[0],a['数学'])#>>70 80 标签也可以作为下标访门

a[1]=a['物理']= 85

print(a)#>>语文:70,数学:85,英