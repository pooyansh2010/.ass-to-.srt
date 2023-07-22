# created by pooyan
import pysubs2
import sys


def convert(file):
    subs = load(file)
    save(subs , file)
    subs = load(filename(file)+".srt")

    overlapSameCount = overlap_same_count(subs)
    while overlapSameCount != 0 :
        previous_count = overlapSameCount
        overlap_same(subs)
        overlapSameCount = overlap_same_count(subs)
        if previous_count == overlapSameCount == 1:
            break
    
    overlapAddCount = overlap_add_count(subs)
    while overlapAddCount != 0 :
        previous_count = overlapAddCount
        overlap_add(subs)
        overlapAddCount = overlap_add_count(subs)
        if previous_count == overlapAddCount == 1:
            break

    overlapAdd2Count = overlap_add_2_count(subs)
    while overlapAdd2Count != 0 :
        previous_count = overlapAdd2Count
        overlap_add_2(subs)
        overlapAdd2Count = overlap_add_2_count(subs)
        if previous_count == overlapAdd2Count == 1:
            break

    save(subs , file)
    # sys.modules[__name__].__dict__.clear()



def load (file):
    return pysubs2.load(file, encoding="utf-8")
    
def filename(file) : 
    filename = str(file).split('.')
    filename = filename[:-1]
    filename = ".".join(filename)
    return filename

def filelocation(file) : 
    print(file)
    folder_location = str(file).split("\\")
    return folder_location[0]

def fileNameWithoutLocation(file) : 
    print(file)
    folder_location = str(file).split("\\")
    return folder_location[1]

def save (subs , file):
    subs.sort()
    subs.save(filename(file)+".srt")


def overlap_same (subs) :
    i=0
    firtRun = True
    previous_stert_time = 0
    previous_end_time = 0
    previous_text = ''
    for line in subs:
        if firtRun :
            previous_stert_time = 0
            previous_end_time = line.end
            previous_text = line.text
            firtRun =False

        if  line.start == previous_stert_time and  line.end == previous_end_time:
            subs.events[i] = pysubs2.SSAEvent(start=previous_stert_time, end=previous_end_time, text=previous_text + "\n" + line.text)
            subs.events.remove(subs.events[i-1])

                
        previous_stert_time = line.start
        previous_end_time = line.end
        previous_text = line.text
        i += 1


def overlap_add (subs) : 
    i=0
    firtRun = True
    previous_stert_time = 0
    previous_end_time = 0
    previous_text = ''
    for line in subs:
        if firtRun :
            previous_stert_time = 0
            previous_end_time = line.end
            previous_text = line.text
            firtRun =False

        if line.start < previous_end_time and  line.end < previous_end_time:
            subs.events[i] = pysubs2.SSAEvent(start=previous_stert_time, end=previous_end_time, text=previous_text + "\n" + line.text)
            subs.events.remove(subs.events[i-1]) 
                
        previous_stert_time = line.start
        previous_end_time = line.end
        previous_text = line.text
        i += 1


def overlap_add_2 (subs) : 
    i=0
    firtRun = True
    previous_stert_time = 0
    previous_end_time = 0
    previous_text = ''
    for line in subs:
        if firtRun :
            previous_stert_time = line.start
            previous_end_time = line.end
            previous_text = line.text
            firtRun =False

        if line.start < previous_end_time and  line.start >= previous_stert_time and i != 0:
            subs.events[i] = pysubs2.SSAEvent(start=previous_stert_time, end=line.end, text=previous_text + "\n" + line.text)
            subs.events.remove(subs.events[i-1]) 
                
        previous_stert_time = line.start
        previous_end_time = line.end
        previous_text = line.text
        i += 1



def overlap_same_count (subs) :
    i=0
    firtRun = True
    previous_stert_time = 0
    previous_end_time = 0
    previous_text = ''
    count = 0
    for line in subs:
        if firtRun :
            previous_stert_time = 0
            previous_end_time = line.end
            previous_text = line.text
            firtRun =False

        if  line.start == previous_stert_time and  line.end == previous_end_time:
            count +=1

                
        previous_stert_time = line.start
        previous_end_time = line.end
        previous_text = line.text
        i += 1

    return count



def overlap_add_count (subs) : 
    i=0
    firtRun = True
    previous_stert_time = 0
    previous_end_time = 0
    previous_text = ''
    count = 0
    for line in subs:
        if firtRun :
            previous_stert_time = 0
            previous_end_time = line.end
            previous_text = line.text
            firtRun =False

        if line.start < previous_end_time and  line.end < previous_end_time:
            count +=1
                
        previous_stert_time = line.start
        previous_end_time = line.end
        previous_text = line.text
        i += 1

    return count


def overlap_add_2_count (subs) : 
    i=0
    firtRun = True
    previous_stert_time = 0
    previous_end_time = 0
    previous_text = ''
    count = 0
    for line in subs:
        if firtRun :
            previous_stert_time = 0
            previous_end_time = line.end
            previous_text = line.text
            firtRun =False

        if line.start < previous_end_time and  line.start >= previous_stert_time:
            count +=1
                
        previous_stert_time = line.start
        previous_end_time = line.end
        previous_text = line.text
        i += 1

    return count

