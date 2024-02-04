import ctypes
import os
from mbs_structures import BufferElement, CVString, FileHeader, Event, SubEvent, BufferElementHeader, Data
#import parameters
import io
import logging
import sys
import time

import operator

from data_index_constants import IndexConstants

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

start_time = time.time()

gsi_buffer_size_in_bytes = 16384
maxwords = 320

old_seconds = 0
temp_event = []
events = []

## file to read:
file_name = "r231f078_4888.lmd"

## destination file:
output_file = open('run231_078_output_Ruth.txt', 'w')
#t1 = time.time()

index_constants = dict([item.value, str(item.name)] for item in IndexConstants)
print(index_constants)

sizeof_event = ctypes.sizeof(Event())
sizeof_sub_event = ctypes.sizeof(SubEvent())
sizeof_data = ctypes.sizeof(Data())
sizeof_buffer_element = ctypes.sizeof(BufferElement)
sizeof_buffer_element_header = ctypes.sizeof(BufferElementHeader())

def process_event(file):
    logger.debug("---start processing event---")
    position_before_read = file.tell()
    logger.debug(f"File tell before reading event bytes: {position_before_read}")
    event_bytes = file.read(sizeof_event)
    event = Event.from_buffer_copy(event_bytes)

    #print(f"Trigger is: {event.trigger}")
    #if event.trigger not in [1, 2, 5]:
    #    raise ValueError(f"Trigger is: {event.trigger}")
    # print(f"File tell after reading event bytes: {file.tell()}")
    # print(f"Event:\n{event}")
    # expected_end_from_event = file.tell() + event.corrected_data_length_in_bytes
    # print(f"Expected position when done with data from event: {expected_end_from_event}")
    # print(f"---end processing event---file tell: {file.tell()}---")

    return event #, expected_end_from_event

def process_subevent(file):
    logger.debug("---start processing subevent---")
    subevent_bytes = file.read(sizeof_sub_event)
    subevent = SubEvent.from_buffer_copy(subevent_bytes)
    # print(f"File tell after reading subevent bytes: {file.tell()}")
    # print(f"Subevent:\n{subevent}")
    # expected_end_from_subevent = file.tell() + subevent.corrected_data_length_in_bytes
    # print(f"Expected position when done with data from subevent: {expected_end_from_subevent}")
    #
    # print(f"Number of subevent data elements: {subevent.number_of_data_elements}")
    # print(f"---end processing subevent---file tell: {file.tell()}---")

    return subevent #, expected_end_from_subevent


def process_data(file, subevent, range_count=None, tell_position=False):
    logger.debug("---start processing data---")
    if range_count is None:
        range_count = subevent.number_of_data_elements
        logger.debug(f"range count not set, using {range_count} from subevent")
    logger.debug(f"Number of subevent data elements to be read: {range_count}")
    # if range_count > 500:
    #     raise ValueError("Way to many subevent data elements?")
    for i in range(range_count):
        data_bytes = file.read(sizeof_data)
        data = Data.from_buffer_copy(data_bytes)
        temp_event.append(data)
        if tell_position is True:
            logger.debug(f"data tell: {file.tell()}, {i} of {range_count}")
        # print(f"subevent i : {i} file tell after reading: {file.tell()}")
        # print(f"Range Index: {i},\nData: {data}")

        if data.index >= 0 and data.index < maxwords:
            #event_data_elements[data.index] = data.data
            pass
        else:
            logger.debug(f"offending event at index: {i}")
            pass
    logger.debug(f"---end processing data---file tell: {file.tell()}---")


def analyze_event(f):
    logger.debug(f"Analyzing event.")

    logger.debug(f"sorting events")
    #print(f"before: {temp_event}")
    #temp_event.sort(key=operator.attrgetter('index'))
    #print(f"after: {temp_event}")
    #print(f"adding temp event to events")
    #events.append(temp_event)

    temp_event_dict = dict()

    detector = None
    x = None
    y = None
    front = None
    back = None
    chopper = None
    RuthE = None 
    
    all_detector = []
    all_x = []
    all_y = []
    all_front = []
    all_back = []
    ruth = []

    for part in temp_event:
        try:
            #index_name = IndexConstants(part.index).name
            index_name = index_constants[part.index]
            #if index_name.startswith('cave_1_y_strip'):
             #    detector = "C1"
              #   y = index_name.split('_')[-1]
               #  front = part.data
                # all_y.append(y)
                 #all_front.append(front)
            #lif index_name.startswith('cave_1_x_strip'):
            #     detector = "C1"
             #    x = index_name.split('_')[-1]
              #   back = part.data
               #  all_x.append(x)
                # all_back.append(back)
            #elif index_name.startswith('cave_2_front_strip'):
             #    detector = "C2"
              #   y = 31 - int(index_name.split('_')[-1])
               #  front = part.data
                # all_y.append(y)
                 #all_front.append(front)
           # elif index_name.startswith('cave_2_back_strip'):
            #     detector = "C2"
             #    x = 31 - int(index_name.split('_')[-1])
              #   back = part.data
               #  all_x.append(x)
                # all_back.append(back)
            #if index_name.startswith('fiona_decay_station_x_strip'):
             #   detector = "DS"
              #  x = 31 - int(index_name.split('_')[-1])
               # back = part.data
                #all_x.append(x)
                #all_back.append(back)
            #elif index_name.startswith('fiona_decay_station_y_strip'):
             #   detector = "DS"
              #  y = index_name.split('_')[-1]
               # front = part.data
                #all_y.append(y)
                #all_front.append(front)
            #if index_name.startswith('chopper'):
             #   detector = "chop"
              #  chopper = part.data
            if index_name == 'rutherford_east':
                detector = "RuthE"
                if part.data != None:
                    ruth = part.data
            
        #except ValueError:
        #    index_name = part.index
        except KeyError:
            index_name = part.index

        temp_event_dict[index_name] = part.data


    if (IndexConstants.clock_low.name in temp_event_dict):
        seconds = (ctypes.c_uint16(temp_event_dict[IndexConstants.clock_low.name]).value + (ctypes.c_uint16(temp_event_dict[IndexConstants.clock_high.name]).value * 2**16) ) / 10000000.0
        global old_seconds,tempsec
        while seconds < old_seconds:
            seconds += 429.4967296
        old_seconds = seconds

        # if detector == "ruthw" and ruthw > 1000:
        #    f.write(f"{file_name[-17:]}\t{detector}\t{seconds}\t{current_event_number}\t{ruthw}\n")
        if detector == "RuthE" and ruth > 800:
            f.write(f"{file_name[-17:]}\t{detector}\t{seconds}\t{current_event_number}\t{ruth}\n")
        

    logger.debug(f"Clearing temp event.")
    temp_event.clear()


"""
Buffers are written back to back in chunks of 16,384 bytes. If it is the first buffer in a file it contains the
file header. All subsequent buffers begin with a buffer header. The buffer header is followed by event headers,
each event is followed by one or more sub events. Sub event headers are followed by data entries.
"""


stat_info = os.stat(file_name)
size = stat_info.st_size
logger.debug(f"File size in bytes: {size}")

number_of_buffers = size / gsi_buffer_size_in_bytes

if number_of_buffers.is_integer():
    number_of_buffers = int(number_of_buffers)
else:
    raise ValueError("Number of buffers is not an integer, file may be corrupt?")

logger.debug(f"Number of buffers: {number_of_buffers}")

logger.debug(f"Size of event header: {sizeof_event}")
logger.debug(f"Size of subevent header: {sizeof_sub_event}")

# we start at -1 because the first buffer will be the file header and so we want that to be number 0
# this way we only count the buffers that give us data, which will be consistent with the C++ code,
# we can change this in the future once the python is verified to give the same results as C++.

buffers_read = -1
last_event_number = 0
current_event_number = None
last_buffer_element_id_number = None

buffers = []

with open(file_name, 'rb', buffering=gsi_buffer_size_in_bytes) as file:
    for buffer_number in range(number_of_buffers):
        buffer = io.BytesIO(file.read(gsi_buffer_size_in_bytes))
        buffers.append(buffer)

logger.debug(len(buffers))

file_header_buffer = buffers[0]

data_buffers = buffers[1:]

number_of_data_elements_left_over = None

temp_buffer = io.BytesIO()
read_into_next_buffer = None
free1 = None

### output file name was here....

file_header_bytes = buffers[0].read(ctypes.sizeof(FileHeader))
file_header = FileHeader.from_buffer_copy(file_header_bytes)
print("=====================")
print("file Header")
print("=====================")
print(f"Header:\n {file_header}")
output_file.write(f"Header = {file_header} \n")
print("Comments:")
for i in range(file_header.number_of_comment_lines):
    print(f"Comment {i}: {file_header.comments[i]}")
    output_file.write(f"Comment{i}: {file_header.comments[i]}")
output_file.write("\n")

for index, buffer in enumerate(data_buffers):
    seconds = 0
    logger.debug("=*" * 30)
    logger.debug("=*" * 30)
    logger.debug("=*" * 30)
    logger.debug(f"Buffer Number: {index + 1} of {len(data_buffers)}")

    #print(f"Position before reading buffer element bytes: {buffer.tell()}")
    buffer_element_bytes = buffer.read(sizeof_buffer_element)
    buffer_element = BufferElement.from_buffer_copy(buffer_element_bytes)
    #print(f"Position after reading buffer element bytes: {buffer.tell()}")

    last_buffer_element_id_number = buffer_element.buffer_id_number

    #print(f"Buffer Element:\n{buffer_element}")
    #print(f"Buffer Id: {buffer_element.buffer_id_number}")
    if buffer_element.fragment_ends_at_beginning_of_buffer:
        logger.debug(f"Fragment ends at beginning of buffer.")
    if buffer_element.fragment_begins_at_end_of_buffer:
        logger.debug(f"Fragment begins at end of buffer.")

    logger.debug(f"Number of fragments: {buffer_element.number_of_fragments}")
    logger.debug(f"Buffer Data length in bytes: {buffer_element.data_length}")
    logger.debug(f"Length of last event in buffer: {buffer_element.free_1}")

    logger.debug(f"Step through each of the {buffer_element.number_of_fragments} events (fragements) in this buffer.")
  
    for fragment_number in range(buffer_element.number_of_fragments):
        logger.debug(f"Fragment number: {fragment_number + 1} of {buffer_element.number_of_fragments}")
		
        if buffer_element.fragment_ends_at_beginning_of_buffer and fragment_number == 0:
            """Handle a fragment which ends at the beginning of a buffer."""
            logger.debug(f"current buffer positon: {buffer.tell()}")
            #raise ValueError("Recover from split fragment here.")
            buffer_element_header_bytes = buffer.read(sizeof_buffer_element_header)
            buffer_element_header = BufferElementHeader.from_buffer_copy(buffer_element_header_bytes)
            buffer_element_header_end = buffer.tell()
            logger.debug(f"Buffer element header: {buffer_element_header}")
            logger.debug(f"buffer element header dlen: {buffer_element_header.dlen} dlen in bytes: {buffer_element_header.dlen * 2}")

            logger.debug(f"Current position: {buffer.tell()}")

            #corrected_read_into = read_into_next_buffer + 8
            corrected_read_into = buffer_element_header.dlen * 2
            logger.debug(f"Expect the split stuff to end at read into bytes?: {corrected_read_into}")
            logger.debug(f"the read into correction that works for everything else up to this point: {read_into_next_buffer + 8}")
            temp_buffer.write(buffer.read(corrected_read_into))
            logger.debug(f"done reading into temp buffer. Non temp buffer position: {buffer.tell()}")

            logger.debug(f"Process temporary buffer now.")

            logger.debug("~" * 30)
            hex_data = temp_buffer.getbuffer().hex()
            n = 8
            split = [hex_data[i:i+n] for i in range(0, len(hex_data), n)]
            k = 0
            for word in split:
                logger.debug(f"{k}: {hex(k+12)}: {word}")
                k += 1
            logger.debug("~" * 30)

            logger.debug(f"temp buffer len: {len(temp_buffer.getvalue())}")
            temp_buffer.seek(0, os.SEEK_END)
            logger.debug(f"temp buffer tell: {temp_buffer.tell()}")
            logger.debug("Seek temp buffer to zero")
            temp_buffer.seek(0)
            logger.debug(f"temp buffer tell: {temp_buffer.tell()}")
            event = process_event(temp_buffer)
            current_event_number = event.count
            logger.debug(f"event: {event}")
            logger.debug(f"event dlen: {event.dlen}")
            logger.debug("setting event dlen to free 1")
            event.dlen = free1
            logger.debug(f"event dlen: {event.dlen}")
            expected_end_from_event = temp_buffer.tell() + event.corrected_data_length_in_bytes
            logger.debug(f"expected end event: {expected_end_from_event}")
            logger.debug(f"Done processing temporary buffer event header.")
            logger.debug(f"temp buffer tell: {temp_buffer.tell()}")
            subevent = process_subevent(temp_buffer)
            logger.debug(f"subevent: {subevent}")
            expected_end_from_subevent = temp_buffer.tell() + subevent.corrected_data_length_in_bytes
            logger.debug(f"expected end subevent: {expected_end_from_subevent}")
            logger.debug(f"Done processing temporary buffer subevent hearder. ")
            logger.debug(f"temp buffer tell: {temp_buffer.tell()}")
            process_data(temp_buffer, subevent, tell_position=True)
            logger.debug(f"Done processing temporary buffer data bits. ")
            logger.debug(f"temp buffer tell: {temp_buffer.tell()}")

            done_with_subevents = False
            while done_with_subevents is False:
                analyze_event(output_file)
                if expected_end_from_subevent == expected_end_from_event:
                    done_with_subevents = True
                    logger.debug("Done with subevents for temp buffer")
                else:
                    logger.debug("---start processing a sub-sub event and data in temp buffer---")
                    logger.debug(
                        f"temp buffer file tell: {temp_buffer.tell()} event: {expected_end_from_event} subevent: {expected_end_from_subevent}")
                    subevent = process_subevent(temp_buffer)
                    expected_end_from_subevent = temp_buffer.tell() + subevent.corrected_data_length_in_bytes
                    process_data(temp_buffer, subevent, tell_position=True)
                    logger.debug("---end processing a sub-sub event and data in temp buffer---")
            logger.debug(f"Done processing temporary buffer data bits for subevents. ")
            logger.debug(f"temp buffer tell: {temp_buffer.tell()}")
            logger.debug("clearing temp buffer")
            logger.debug(f"temp buffer len: {len(temp_buffer.getvalue())}")
            temp_buffer = io.BytesIO()
            logger.debug(f"temp buffer len: {len(temp_buffer.getvalue())}")
            #raise ValueError("fix fix fix")


        elif buffer_element.fragment_begins_at_end_of_buffer and fragment_number + 1 == buffer_element.number_of_fragments:
            """Handle a fragment which begins at the end of a buffer."""
            #raise ValueError("This fragment runs past the end of the buffer")
            before = buffer.tell()
            logger.debug(f"before is: {before}")
            distance_to_end = gsi_buffer_size_in_bytes - before
            logger.debug(f"distance to end in bytes: {distance_to_end}")
            logger.debug(f"length in free 1: {buffer_element.free_1}")
            free1 = buffer_element.free_1
            free1_bytes = buffer_element.free_1 * 2
            logger.debug(f"length in free 1 in bytes?: {free1_bytes}")
            read_into_next_buffer = free1_bytes - distance_to_end
            logger.debug(f"read into next buffer: {read_into_next_buffer}")

            logger.debug(f"@@@SSS>>> buffer tell: {buffer.tell()}")
            event = process_event(buffer)
            current_event_number = event.count
            logger.debug(f"@@@XXX>>> buffer tell: {buffer.tell()}")
            logger.debug(f"event data length in bytes: {event.data_length_in_bytes}")
            logger.debug(f"event data length in corrected bytes: {event.corrected_data_length_in_bytes}")
            expected_end_from_event = buffer.tell() + event.corrected_data_length_in_bytes
            logger.debug(f"expected end event: {expected_end_from_event}")
            logger.debug(f"@@@YYY>>> buffer tell: {buffer.tell()}")
            buffer.seek(before)
            logger.debug(f"@@@ZZZ>>> buffer tell: {buffer.tell()}")
            temp_buffer.write(buffer.read(event.corrected_data_length_in_bytes + sizeof_event))
            logger.debug(f"@@@@@@@>>> buffer tell: {buffer.tell()}")
            if buffer.tell() != gsi_buffer_size_in_bytes:
                #raise ValueError("Did NOT read all of the end of this fragment into the temp buffer!!!")
                logger.debug("Did NOT read all of the end of this fragment into the temp buffer!!!")
            #raise ValueError("fix fix fix")

            break

            # event = process_event(buffer)
            # logger.debug(f"event data length in bytes: {event.data_length_in_bytes}")
            # logger.debug(f"event data length in corrected bytes: {event.corrected_data_length_in_bytes}")
            # expected_end_from_event = buffer.tell() + event.corrected_data_length_in_bytes
            # logger.debug(f"expected end event: {expected_end_from_event}")
            # # logger.debug(f"other: {before + event.data_length_in_bytes}")
            #
            # subevent = process_subevent(buffer)
            # expected_end_from_subevent = buffer.tell() + subevent.corrected_data_length_in_bytes
            # logger.debug(f"expected end from subevent: {expected_end_from_subevent}")
            #
            # logger.debug(f"length in free 1: {buffer_element.free_1}")
            # logger.debug(f"Number of data elements: {subevent.number_of_data_elements}")
            # distance_to_end_of_data_in_bytes = expected_end_from_subevent - expected_end_from_event
            # logger.debug(f"Distance to end in bytes: {distance_to_end_of_data_in_bytes}")
            # number_of_data_elements_left_over = distance_to_end_of_data_in_bytes / ctypes.sizeof(Data())
            # logger.debug(f"Number of data elements left over: {number_of_data_elements_left_over}")
            # range_count = int(subevent.number_of_data_elements - number_of_data_elements_left_over)
            # process_data(buffer, subevent, range_count)
            # if buffer.tell() != gsi_buffer_size_in_bytes:
            #     raise ValueError(
            #         f"There is a subevent before the end? file.tell: {buffer_element.tell()} buffer end: {gsi_buffer_size_in_bytes}")
            # break

        else:
            """The current event is not fragmented."""
            logger.debug("No fragment has occurred.")
            before = buffer.tell()
            event = process_event(buffer)
            current_event_number = event.count
            logger.debug(f"event data length in bytes: {event.data_length_in_bytes}")
            logger.debug(f"event data length in corrected bytes: {event.corrected_data_length_in_bytes}")
            expected_end_from_event = buffer.tell() + event.corrected_data_length_in_bytes
            logger.debug(f"expected end event: {expected_end_from_event}")
            #logger.debug(f"other: {before + event.data_length_in_bytes}")

            subevent = process_subevent(buffer)
            expected_end_from_subevent = buffer.tell() + subevent.corrected_data_length_in_bytes
            logger.debug(f"expected end from subevent: {expected_end_from_subevent}")
            process_data(buffer, subevent)

        done_with_subevents = False

        while done_with_subevents is False:
            analyze_event(output_file)
            if expected_end_from_subevent == expected_end_from_event:
                done_with_subevents = True
            else:
                logger.debug("---start processing a sub-sub event and data---")
                logger.debug(
                    f"file tell: {buffer.tell()} event: {expected_end_from_event} subevent: {expected_end_from_subevent}")
                subevent = process_subevent(buffer)
                expected_end_from_subevent = buffer.tell() + subevent.corrected_data_length_in_bytes
                process_data(buffer, subevent)
                logger.debug("---end processing a sub-sub event and data---")


output_file.close()
end_time = time.time()
total_time = end_time - start_time

print(f"total time: {total_time} / seconds -- {total_time/60} minutes")
