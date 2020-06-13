from db import Db
from mode import Mode
from words import list_to_dict
from words import text_to_list
import csv
import codecs

class Learn(Mode):
        ext=""
        def validate(self, args):
                valid_args = False
                usage = 'Usage: %s learn <doc type> <file> <count>' % args[0]

                if len(args) == 5:
                        doc_type = args[2]
                        
                        file_contents = None
                        try:
                                ext = (args[3])[-3:]
                                if (ext=="csv"):
                                        f_open = codecs.open('args[3]','r',encoding='utf-8',errors='ignore') 
                                        text = list(csv.reader(f_open, delimiter=','))
                                        file_contents = ""
                                        for sen in text:
                                                file_contents = file_contents + (sen[1])
                                if (ext=="txt"):
                                     file_contents = open(args[3], 'r').read()   
                        except Exception as e:
                                raise ValueError(usage + '\nUnable to read specified file "%s", the error message was: %s' % (args[3], e))

                        count = 0
                        try:
                                count = int(args[4])
                        except:
                                raise ValueError(usage + '\nEnter an integer value for the "count" parameter')                  

                        self.file_contents = file_contents
                        self.count = count
                        self.doc_type = doc_type
                        if (ext=="csv"):
                                f_open.close()

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
