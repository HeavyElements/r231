from ctypes import BigEndianStructure, c_char, c_int16, c_int32
import ctypes

class CVString(BigEndianStructure):
    _fields_ = [("string_length", c_int16),
                ("string", (c_char * 78)),
                ]

    def __str__(self):
        return f"{self.string.decode('ascii')}\n"


class FileHeader(BigEndianStructure):
    _fields_ = [("tlen", c_int16),
                ("dlen", c_int16),
                ("subtype", c_int16),
                ("type", c_int16),
                ("frag", c_int16),
                ("used", c_int16),
                ("buf", c_int32),
                ("evt", c_int32),
                ("current_i", c_int32),
                ("stime", (c_int32 * 2)),
                ("free", (c_int32 * 4)),
                ("label_length", c_int16),
                ("label", (c_char * 30)),
                ("file_name_length", c_int16),
                ("filename", (c_char * 86)),
                ("user_name_length", c_int16),
                ("user_name", (c_char * 30)),
                ("time", (c_char * 24)),
                ("run_id_length", c_int16),
                ("run_id", (c_char * 66)),
                ("explanation_length", c_int16),
                ("explanation", (c_char * 66)),
                ("number_of_comment_lines", c_int32),
                ("comments", (CVString * 30)),
                ]

    def __str__(self):
        return f"tlen: {self.tlen}\n" \
               f"dlen: {self.dlen}\n" \
               f"subtype: {self.subtype}\n" \
               f"type: {self.type}\n" \
               f"frag: {self.frag}\n" \
               f"used: {self.used}\n" \
               f"buf: {self.buf}\n" \
               f"evt: {self.evt}\n" \
               f"current_i: {self.current_i}\n" \
               f"stime: {list(self.stime)}\n" \
               f"free: {list(self.free)}\n" \
               f"label: {self.label.decode('ascii')}\n" \
               f"filename: {self.filename.decode('ascii')}\n" \
               f"user name: {self.user_name.decode('ascii')}\n" \
               f"time: {self.time.decode('ascii')}\n" \
               f"run id: {self.run_id.decode('ascii')}\n" \
               f"explanation: {self.explanation.decode('ascii')}\n" \
               f"number of comment lines: {self.number_of_comment_lines}\n"


class BufferElementHeader(BigEndianStructure):
    _fields_ = [
        ("dlen", c_int32),
        ("subtype", c_int16),
        ("type", c_int16),
    ]

    def __str__(self):
        return f"dlen: {self.dlen}\n" \
               f"subtype: {self.subtype}\n" \
               f"type: {self.type}\n"


class BufferElement(BigEndianStructure):
    _fields_ = [
        ("dlen", c_int32),  # Length of data field in words (2 bytes per word)
        ("subtype", c_int16),
        ("type", c_int16),
        ("begin", c_char),  # Fragment begin at end of buffer
        ("end", c_char),    # Fragment end at begin of buffer
        ("used", c_int16),  # Used length of data field in words
        ("buf", c_int32),   # Current buffer number
        ("evt", c_int32),   # Number of fragments
        ("current_i", c_int32),     # Index, temporarily used
        ("time", (c_int32 * 2)),    # Time stamp
        ("free", (c_int32 * 4)),    # Free 1: Length of last event in buffer
    ]

    @property
    def data_length(self):
        """
        Returns the length of the data field in number of bytes.

        :return:
        """
        return self.dlen * 2

    @property
    def fragment_begins_at_end_of_buffer(self):
        return bool(int.from_bytes(self.begin, byteorder="big"))

    @property
    def fragment_ends_at_beginning_of_buffer(self):
        return bool(int.from_bytes(self.end, byteorder="big"))

    @property
    def buffer_id_number(self):
        return self.buf

    @property
    def number_of_fragments(self):
        return self.evt

    @property
    def free_1(self):
        return list(self.free)[1]

    def __str__(self):
        return f"dlen: {self.dlen}\n" \
               f"subtype: {self.subtype}\n" \
               f"type: {self.type}\n" \
               f"begin: {self.begin}\n" \
               f"end: {self.end}\n" \
               f"used: {self.used}\n" \
               f"buf: {self.buf}\n" \
               f"evt: {self.evt}\n" \
               f"current i: {self.current_i}\n" \
               f"time: {list(self.time)}\n" \
               f"free: {list(self.free)}\n"


class Event(BigEndianStructure):
    _fields_ = [
        ("dlen", c_int32), #  Data length + 4 in words
        ("subtype", c_int16),
        ("type", c_int16),
        ("trigger", c_int16),
        ("dummy", c_int16),
        ("count", c_int32)
    ]

    @property
    def data_length_in_bytes(self):
        return self.dlen * 2 # Data length + 4 in words

    @property
    def corrected_data_length_in_bytes(self):
        return (self.dlen - 4) * 2

    def __str__(self):
        return f"dlen: {self.dlen}\n" \
               f"subtype: {self.subtype}\n" \
               f"type: {self.type}\n" \
               f"trigger: {self.trigger}\n" \
               f"dummy: {self.dummy}\n" \
               f"count: {self.count}\n"


class SubEvent(BigEndianStructure):
    _fields_ = [
        ("dlen", c_int32), # Data length +2 in words
        ("subtype", c_int16),
        ("type", c_int16),
        ("control", c_char),
        ("subcrate", c_char),
        ("procid", c_int16),
    ]

    @property
    def data_length_in_bytes(self):
        # dlen is data len + 2 in words, there are 2 bytes per word
        return self.dlen * 2

    @property
    def corrected_data_length_in_bytes(self):
        return (self.dlen - 2) * 2

    @property
    def number_of_data_elements(self):
        # there are 2 bytes per data element
        return int(self.corrected_data_length_in_bytes / ctypes.sizeof(Data()))

    def __str__(self):
        return f"dlen: {self.dlen}\n" \
               f"subtype: {self.subtype}\n" \
               f"type: {self.type}\n" \
               f"control: {self.control}\n" \
               f"subcrate: {self.subcrate}\n" \
               f"procid: {self.procid}\n"


class Data(BigEndianStructure):
    _fields_ = [
        ("data", c_int16),
        ("index", c_int16),
    ]

    def __str__(self):
        return f"data: {self.data}\n" \
               f"index: {self.index}\n"
