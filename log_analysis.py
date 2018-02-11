# TUT 1 ##############################

# log = open('loglistener2.txt', 'r')
# send = "send"
# receive = "recv"
# sent = 0.0
# received = 0.0
# line = 0.0
# for lines in log:
#     line += 1
#     if send in lines:
#         sent +=1
#     elif receive in lines:
#         received +=1
# ratio = received/sent
# print("PDR: " + str(ratio))

# TUT 2 ##############################

log = open('loglistener(tut2).txt', 'r')

for lines in log:
    line = lines.split()

    if line[0] < "05:00.000":
        continue
