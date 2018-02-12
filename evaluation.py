def evaluate():
    log = open('flooding.txt', 'r')

    # Stores the flood id and time that the flood began.
    flood_start = {}

    # Stores the flood id and time that the flood ended.
    flood_end = {}
    
    # Stores the flood id and number of nodes updated with that id.
    end_to_end_loss_rate = {}

    num_nodes = 30

    for lines in log:
        line = lines.split()

        if line[0] < "05:00.000":
            continue

        if line[3] == "message" and len(line) > 5:
            flood_id = line[5]
            flood_start[flood_id] = line[0]

        if line[3] == "recv":
            flood_id = line[10]
            flood_end[flood_id] = line[0]    

            if flood_id in end_to_end_loss_rate:
                end_to_end_loss_rate[flood_id] += 1
            else:
                end_to_end_loss_rate[flood_id] = 1

    avg_time = 0
    i = 0

    for key, value in flood_start.items():
        start_time = convert_time(value)

        # There are more ids which start floods.
        if key in flood_end:
            end_time = convert_time(flood_end[key])
        else:
            continue

        dissemination_time = end_time - start_time
        
        i += 1
        avg_time += dissemination_time

    avg_time = avg_time/i

    avg_loss_rate = 0
    for key, value in end_to_end_loss_rate.items():
        loss_rate = int(value)/num_nodes

        avg_loss_rate += loss_rate
    
    avg_loss_rate = avg_loss_rate/len(end_to_end_loss_rate)

    print("Average Dissemination Time: ", str(avg_time))
    print("Average End-to-End Loss Rate: ", str(avg_loss_rate))

def evaluate_with_powertrace():
    print("nothing yet")    
        
# Converts the time string into seconds.eg 5:00.000 becomes 300
def convert_time(time):
    time = time.split(":")
    minutes = float(time[0])
    secs = float(time[1])

    secs = (minutes * 60) + secs
    return(secs)


if __name__ == '__main__':
    evaluate()