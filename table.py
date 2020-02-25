class Table:
    def __init__(self,name='',fields=tuple(),tups=None):
      self.name = name
      self.fields = fields
      self.tups = tups

    def __str__(self):
      results = self.name
      results += str(self.fields) + '\n' + '=====' +'\n'
      for row in self.tups:
        results += str(row) +'\n'
      return results

    # Relational operations:
    def select(self,field,val):
      index = -1
      name = 'result'
      tups = []
      for curField in self.fields:
        if curField == field:
          index = self.fields.index(field)
          break
      if index == -1:
        return 'Invalid field'
      for tup in self.tups:
        if tup[index] == val:
          tups.append(tup)
      if (len(tups) > 0):
        return Table(name,self.fields,tups)
      return 'No value of ' + str(val)

    def project(self,*fields):
      name = 'result'
      tups = []
      fieldInds = []
      for tup in self.tups:
        tmpTup = []
        for field in fields:
          tmpTup.append(tup[self.fields.index(field)])
        tups.append(tuple(tmpTup))
      return Table(name,fields,[t for t in (set(tuple(i) for i in tups))])

    @staticmethod
    def join(tab1,tab2):
      name = 'result'
      keyField = ''
      fields = list(tab1.fields)
      tups = []
      for field in tab2.fields:
        if field in fields:
          keyField = field
        else:
          fields.append(field)
      for tup1 in tab1.tups:
        for tup2 in tab2.tups:
          if tup1[tab1.fields.index(keyField)] == tup2[tab2.fields.index(keyField)]:
            tup2List = list(tup2)
            tup2List.pop(tab2.fields.index(keyField))
            tup = tup1 + tuple(tup2List)
            tups.append(tup)
      return Table(name,tuple(fields),tups)
      
    def insert(self,*tup):
      if len(tup) != len(self.tups[0]):
        print('Invalid amount of inputs.')
        return
      tupl = []  
      for curTup in tup:
        tupl.append(curTup)
      self.tups.append(tuple(tupl))

    def remove(self,field,val):
      tups = self.tups.copy()
      for tup in self.tups:
        if tup[self.fields.index(field)] == val:
          tups.remove(tup)
      self.tups = tups

    # Serialization and text backup
    def store(self):
      import pickle
      fname = self.name + '.db'
      pickle.dump(self, open(fname, 'wb'))

    @staticmethod
    def restore(fname):
      import pickle
      self = pickle.load(open(fname, 'rb'))
      return Table(self.name,self.fields,self.tups)

    @staticmethod
    def read(fname):
      name = ''
      fields = tuple()
      tups = []
      with open(fname, 'r') as fTable:
        name = str(fTable.readline().strip())
        fields = tuple(fTable.readline().rstrip().split(','))
        tableData = fTable.read()
        tableData = tableData.splitlines()
        for row in tableData:
          tups.append(tuple(row.split(',')))
      return Table(name,fields,tups)

    def write(self,fname):
      with open(fname, 'w+') as f:
        results = ''
        results += self.name + '\n'
        for field in self.fields:
          results += field + ','
        results = results[:-1]
        results += '\n'
        for tup in self.tups:
          for field in tup:
            results += field + ','
          results = results[:-1]
          results += '\n'
        f.write(results)