def importsingleCSV(self,pars):
                file_contents = ""
                count=0
                data=""       
                
                for sen in self.text:
                        if (pars):
                                punc= findSep(sen)
                                if (punc=="comma"):
                                        data=sen.split(',')
                                        file_contents = file_contents + (data[1])
                                if (punc=="space"):
                                        data=(sen).split(' ')
                                        file_contents = file_contents + (data[1])
                
                                if (punc=="semi-colon"):
                                        data=(sen).split(';')
                                        file_contents = file_contents + (data[1])
                        else:
                                file_contents = file_contents + (sen) 
                                print(data[0])
                        count = count+1 
                return [count,file_contents]
        
def importsingleTXT(self,pars):
        file_contents = ""
        count=0
        data=""
        
                
        
        for sen in self.text:
                if (pars):
                        punc= findSep(sen)
                        if (punc=="comma"):
                                data=(sen).split(',')
                                file_contents = file_contents + (data[1])
                        if (punc=="space"):
                                data=(sen).split(' ')
                                file_contents = file_contents + (data[1])
        
                        if (punc=="semi-colon"):
                                data=(sen).split(';')
                                file_contents = file_contents + (data[1])
                else:
                        file_contents = file_contents + (sen) 

                count=count+1
        return [count,file_contents]