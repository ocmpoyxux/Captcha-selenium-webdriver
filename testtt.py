import re
from collections import Counter

in_file = "/home/v.ostrouhih/mbox(3).txt"
with open(in_file, 'r') as read_file:
    from_send = []
    subject_send = []
    from_and_time = []
    for line in read_file:
        if re.match(r'From: ', line):
            from_send.append(line)
        elif re.match(r'Subject', line):
            subject_send.append(line)
        elif re.match(r'From ', line):
            from_and_time.append(line)

end_result1 = dict(zip(from_and_time, subject_send))
for key in end_result1.keys():
    print ("%s : %s" % (key, end_result1[key]))

end_result2 = Counter(from_send)
for key in end_result2:
    print ("%s : %s" % (key, end_result2[key]))
 



    


     
         
        
            
        
        


