import time

def decoarator(way):
     def dec(function):
         def wrapp(*args, **kwargs):
             start = time.time()
             ans = function(*args, **kwargs)
             finish = time.time()
             time_of_work = finish - start
             file_to_write = []
             file_to_write.append(time.ctime(start))
             file_to_write.append('\n')
             if args:
                 for i in args:
                     file_to_write.append((str(i)+' '))
                 file_to_write.append('\n')
             if kwargs:
                 for key in kwargs.keys():
                     file_to_write.append(str(kwargs[key] + ' '))
             if ans:
                 file_to_write.append(str(ans))
                 file_to_write.append('\n')
             else:
                 file_to_write.append('-')
                 file_to_write.append('\n')
             file_to_write.append(time.ctime(finish))
             file_to_write.append('\n')
             file_to_write.append(str(time_of_work))
             file_to_write.append('\n')
             cout = open(way, 'w')
             wr(file_to_write, cout)
             return ans
         return wrapp
     return dec
