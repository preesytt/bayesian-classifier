from db import Db
from mode import Mode
from words import list_to_dict
from words import text_to_list
import csv
import codecs
import fnmatch
from findSeparator import findSep

class Learn(Mode):
        ext=""
        def validate(self, args):
                valid_args = False
                usage = 'Usage: %s learn <doc type> <file> <count>' % args[0]
                count = 0
                self.file = args[3]
                self.text=""
                self.ext = (args[3])[-3:]
                if len(args) == 4 or len(args)==5:
                        doc_type = args[2]
                        file_contents = None
                        try:
                                
                                if (self.ext=="csv"): #for single spam/ham dataset file
                                        f_open = codecs.open(self.file,'r',encoding='utf-8',errors='ignore') 
                                        self.text = list(csv.reader(f_open, delimiter=','))
                                        typeCk = self.text 
                                        #print(typeCk) 
                                        Ck=[typeCk[0][0]]                                       

                                if (self.ext=="txt"):
                                        self.text = open(args[3], 'r').read()
                                        typeCk = self.text.split()
                                        Ck=[typeCk[0][-5:]]
                                
                                
                                
                                #print(Ck)
                                filter1 = fnmatch.filter(Ck, 'spam?')
                                filter2 = fnmatch.filter(Ck, 'ham**')
                                filter3 = fnmatch.filter(Ck, 'spam')
                                filter4 = fnmatch.filter(Ck, 'ham')
                                pars = filter1 or filter2 or filter3 or filter4
                                #print(pars)
                                vals = self.importsingleData(pars)
                                count,file_contents= vals[0],vals[1]
                                                         
                                
                                        
                        except Exception as e:
                                raise ValueError(usage + '\nUnable to read specified file "%s", the error message was: %s' % (args[3], e))
                 
                        #print(file_contents)
                        self.file_contents = file_contents
                        self.count = count
                        self.doc_type = doc_type
                        # if (ext=="csv"):
                        #         f_open.close()

                else:
                        raise ValueError(usage)                          

        def execute(self):
                db = Db()
                l = text_to_list(self.file_contents)
                d = list_to_dict(l)
                db.update_word_counts(d, self.doc_type)
                db.update_doctype_count(self.count, self.doc_type)
                return self.count

        def output(self, _):
                print("Processed %s documents of type '%s'" % (self.count, self.doc_type))

        # def importsingleCSV(self,pars):
        #         file_contents = ""
        #         count=0
        #         data="" 
        #         data=self.text.split()
        #         Ck =""
        #         if (pars):
        #                 Ck = pars[-1:]
        
        #                 ls = ['spam'+Ck,'ham'+Ck]   
        #                 for word in range(0,len(data)):
        #                         punc= findSep(self)
        #                         if ((punc=="comma") or (punc=="semi-colon")):
        #                                 if (data[word]!=ls[0]):
        #                                         if (data[word]!=ls[1]):
        #                                                 #print(ls[0])
        #                                                 #print(data[word])
        #                                                 file_contents = file_contents +' '+ (data[word])
        #                                                 count=count+1
        #                         if (punc=="space"):
        #                                 if (data[word]!='spam'):
        #                                         if (data[word]!='ham'):
        #                                                 data=data.split(' ')
        #                                                 file_contents = file_contents +' '+ (data[word])
        #                                                 count=count+1

        #         else:
        #                 file_contents = file_contents + self.text
        #                 print(file_contents)
        #                 count=count+1
        #         return [count,file_contents]
        
        def importsingleData(self,pars):
                file_contents = ""
                count=0
                if (self.ext=='txt'):
                        data=self.text.split()                        
                        if (pars):
                                Ck = pars[0][-1:]
                
                                ls = ['spam'+Ck,'ham'+Ck,]   
                                for word in range(0,len(self.text.split())):
                                        punc= findSep(self)
                                        if ((punc=="comma") or (punc=="semi-colon")):
                                                if (data[word]!=ls[0]):
                                                        if (data[word]!=ls[1]):
                                                                #print(data[word]!=ls[0])
                                                                #print(data[word])
                                                                file_contents = file_contents +' '+ (data[word])
                                                                count=count+1
                                        if (punc=="space"):
                                                
                                                file_contents = file_contents +' '+ (data[word])
                                                count=count+1

                        else:
                                file_contents = file_contents + self.text
                                #print(file_contents)
                                count=len(self.text.split())
                else:
                        data=self.text 
                        #print(data)                      
                        if (pars):
                                Ck = pars[0][-1:]
                
                                ls = ['spam'+Ck,'ham'+Ck,]   
                                for word in range(0,len(self.text)):
                                                # if (data[word][1]!=ls[0]):
                                                #         if (data[word]!=ls[1]):
                                                                #print(data[word]!=ls[0])
                                                                #print(data[word])
                                                
                                        file_contents = file_contents +' '+ (data[word][1])
                                        
                                        count=count+1
                                        # if (punc=="space"):
                                                
                                        #         file_contents = file_contents +' '+ (data[word][1])
                                        #         count=count+1

                        else:
                                count=len(data[0])
                                for x in range(0,count):
                                        file_contents = file_contents + ' '+  data[0][x]
                                #print(file_contents)
                                
                        
                return [count,file_contents]

                