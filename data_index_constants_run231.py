from enum import IntEnum, unique

@unique
class IndexConstants(IntEnum):
    # from the CAEN V830 scaler
    clock_low = 2
    clock_high = 3
    requested_triggers_low = 4
    requested_triggers_high = 5
    accepted_triggers_low = 6
    accepted_triggers_high = 7
    trap_dumps_low = 8
    trap_dumps_high = 9
    target_rotations_low = 10
    target_rotations_high = 11

    # from the V560 scaler
    time_since_wheel_laser_flash_low = 16
    time_since_wheel_laser_flash_high = 17

    # from the V262 i / o module
    # bit=  bit1=   bit2=   bit3=inhibit triggers
    ##I262 = 27

    # the error words
    error_location_low = 28
    error_location_high = 29

    error_type_low = 30
    error_type_high = 31

    # DSSD at BGS exit. for this detector, the front side strips give Y positions, back side strips give X positions
    # detector is rotated such that the connectors are on the WEST side
    # define iC1Y  32    // BGS focal plane detector, front side -    Y positions
    # define iC1X  64    // BGS focal plane detector, back side -    X positions
    cave_1_x_strip_0 = 32
    cave_1_x_strip_1 = 33
    cave_1_x_strip_2 = 34
    cave_1_x_strip_3 = 35
    cave_1_x_strip_4 = 36
    cave_1_x_strip_5 = 37
    cave_1_x_strip_6 = 38
    cave_1_x_strip_7 = 39
    cave_1_x_strip_8 = 40
    cave_1_x_strip_9 = 41
    cave_1_x_strip_10 = 42
    cave_1_x_strip_11 = 43
    cave_1_x_strip_12 = 44
    cave_1_x_strip_13 = 45
    cave_1_x_strip_14 = 46
    cave_1_x_strip_15 = 47
    cave_1_x_strip_16 = 48
    cave_1_x_strip_17 = 49
    cave_1_x_strip_18 = 50
    cave_1_x_strip_19 = 51
    cave_1_x_strip_20 = 52
    cave_1_x_strip_21 = 53
    cave_1_x_strip_22 = 54
    cave_1_x_strip_23 = 55
    cave_1_x_strip_24 = 56
    cave_1_x_strip_25 = 57
    cave_1_x_strip_26 = 58
    cave_1_x_strip_27 = 59
    cave_1_x_strip_28 = 60
    cave_1_x_strip_29 = 61
    cave_1_x_strip_30 = 62
    cave_1_x_strip_31 = 63

    cave_1_y_strip_0 = 160
    cave_1_y_strip_1 = 161
    cave_1_y_strip_2 = 162
    cave_1_y_strip_3 = 163
    cave_1_y_strip_4 = 164
    cave_1_y_strip_5 = 165
    cave_1_y_strip_6 = 166
    cave_1_y_strip_7 = 167
    cave_1_y_strip_8 = 168
    cave_1_y_strip_9 = 169
    cave_1_y_strip_10 = 170
    cave_1_y_strip_11 = 171
    cave_1_y_strip_12 = 172
    cave_1_y_strip_13 = 173
    cave_1_y_strip_14 = 174
    cave_1_y_strip_15 = 175
    cave_1_y_strip_16 = 176
    cave_1_y_strip_17 = 177
    cave_1_y_strip_18 = 178
    cave_1_y_strip_19 = 179
    cave_1_y_strip_20 = 180
    cave_1_y_strip_21 = 181
    cave_1_y_strip_22 = 182
    cave_1_y_strip_23 = 183
    cave_1_y_strip_24 = 184
    cave_1_y_strip_25 = 185
    cave_1_y_strip_26 = 186
    cave_1_y_strip_27 = 187
    cave_1_y_strip_28 = 188
    cave_1_y_strip_29 = 189
    cave_1_y_strip_30 = 190
    cave_1_y_strip_31 = 191

    # define invC1X 0    // non-zero inverts strip numbers in analysis so they go from  west to east
    # define invC1Y 0    // non-zero inverts strip numbers in analysis so they go from  west to east

    # // DSSD at cave 2 entrance. for this detector, the front side strips give Y positions, back side strips give X positions
    # // detector is rotated such that the connectors are on the EAST side
    # define iC2F 96        // Cave2 wall lo-E front
    # define iC2B 128    // Cave2 wall hi-E front
    cave_2_front_strip_0 = 96
    cave_2_front_strip_1 = 97
    cave_2_front_strip_2 = 98
    cave_2_front_strip_3 = 99
    cave_2_front_strip_4 = 100
    cave_2_front_strip_5 = 101
    cave_2_front_strip_6 = 102
    cave_2_front_strip_7 = 103
    cave_2_front_strip_8 = 104
    cave_2_front_strip_9 = 105
    cave_2_front_strip_10 = 106
    cave_2_front_strip_11 = 107
    cave_2_front_strip_12 = 108
    cave_2_front_strip_13 = 109
    cave_2_front_strip_14 = 110
    cave_2_front_strip_15 = 111
    cave_2_front_strip_16 = 112
    cave_2_front_strip_17 = 113
    cave_2_front_strip_18 = 114
    cave_2_front_strip_19 = 115
    cave_2_front_strip_20 = 116
    cave_2_front_strip_21 = 117
    cave_2_front_strip_22 = 118
    cave_2_front_strip_23 = 119
    cave_2_front_strip_24 = 120
    cave_2_front_strip_25 = 121
    cave_2_front_strip_26 = 122
    cave_2_front_strip_27 = 123
    cave_2_front_strip_28 = 124
    cave_2_front_strip_29 = 125
    cave_2_front_strip_30 = 126
    cave_2_front_strip_31 = 127

    cave_2_back_strip_0 = 128
    cave_2_back_strip_1 = 129
    cave_2_back_strip_2 = 130
    cave_2_back_strip_3 = 131
    cave_2_back_strip_4 = 132
    cave_2_back_strip_5 = 133
    cave_2_back_strip_6 = 134
    cave_2_back_strip_7 = 135
    cave_2_back_strip_8 = 136
    cave_2_back_strip_9 = 137
    cave_2_back_strip_10 = 138
    cave_2_back_strip_11 = 139
    cave_2_back_strip_12 = 140
    cave_2_back_strip_13 = 141
    cave_2_back_strip_14 = 142
    cave_2_back_strip_15 = 143
    cave_2_back_strip_16 = 144
    cave_2_back_strip_17 = 145
    cave_2_back_strip_18 = 146
    cave_2_back_strip_19 = 147
    cave_2_back_strip_20 = 148
    cave_2_back_strip_21 = 149
    cave_2_back_strip_22 = 150
    cave_2_back_strip_23 = 151
    cave_2_back_strip_24 = 152
    cave_2_back_strip_25 = 153
    cave_2_back_strip_26 = 154
    cave_2_back_strip_27 = 155
    cave_2_back_strip_28 = 156
    cave_2_back_strip_29 = 157
    cave_2_back_strip_30 = 158
    cave_2_back_strip_31 = 159

    # define invC2X 1    // non-zero inverts strip numbers in analysis so they go from  west to east
    # define invC2Y 1    // non-zero inverts strip numbers in analysis so they go from bottom to top

    # define iFPE 160    // FIONA FP Hi-E east end
    # define iFPW 176    // FIONA FP hi-E west end
    # this is the back of the cube detector
    #######fiona_focal_plane_east = 160
    ########fiona_focal_plane_west = 176
    # define invFPE 0    // non-zero inverts strip numbers in analysis so they go from  bottom to top
    # define invFPW 1    // non-zero inverts strip numbers in analysis so they go from  bottom to top

    # define iDSX 192    // FIONA FP, front side - X positions
    # define iDSY 224    // FIONA FP, back side - Y positions
    # regular DSSD at back of fiona
    fiona_decay_station_x_strip_0 = 192
    fiona_decay_station_x_strip_1 = 193
    fiona_decay_station_x_strip_2 = 194
    fiona_decay_station_x_strip_3 = 195
    fiona_decay_station_x_strip_4 = 196
    fiona_decay_station_x_strip_5 = 197
    fiona_decay_station_x_strip_6 = 198
    fiona_decay_station_x_strip_7 = 199
    fiona_decay_station_x_strip_8 = 200
    fiona_decay_station_x_strip_9 = 201
    fiona_decay_station_x_strip_10 = 202
    fiona_decay_station_x_strip_11 = 203
    fiona_decay_station_x_strip_12 = 204
    fiona_decay_station_x_strip_13 = 205
    fiona_decay_station_x_strip_14 = 206
    fiona_decay_station_x_strip_15 = 207
    fiona_decay_station_x_strip_16 = 208
    fiona_decay_station_x_strip_17 = 209
    fiona_decay_station_x_strip_18 = 210
    fiona_decay_station_x_strip_19 = 211
    fiona_decay_station_x_strip_20 = 212
    fiona_decay_station_x_strip_21 = 213
    fiona_decay_station_x_strip_22 = 214
    fiona_decay_station_x_strip_23 = 215
    fiona_decay_station_x_strip_24 = 216
    fiona_decay_station_x_strip_25 = 217
    fiona_decay_station_x_strip_26 = 218
    fiona_decay_station_x_strip_27 = 219
    fiona_decay_station_x_strip_28 = 220
    fiona_decay_station_x_strip_29 = 221
    fiona_decay_station_x_strip_30 = 222
    fiona_decay_station_x_strip_31 = 223

    fiona_decay_station_y_strip_0 = 224
    fiona_decay_station_y_strip_1 = 225
    fiona_decay_station_y_strip_2 = 226
    fiona_decay_station_y_strip_3 = 227
    fiona_decay_station_y_strip_4 = 228
    fiona_decay_station_y_strip_5 = 229
    fiona_decay_station_y_strip_6 = 230
    fiona_decay_station_y_strip_7 = 231
    fiona_decay_station_y_strip_8 = 232
    fiona_decay_station_y_strip_9 = 233
    fiona_decay_station_y_strip_10 = 234
    fiona_decay_station_y_strip_11 = 235
    fiona_decay_station_y_strip_12 = 236
    fiona_decay_station_y_strip_13 = 237
    fiona_decay_station_y_strip_14 = 238
    fiona_decay_station_y_strip_15 = 239
    fiona_decay_station_y_strip_16 = 240
    fiona_decay_station_y_strip_17 = 241
    fiona_decay_station_y_strip_18 = 242
    fiona_decay_station_y_strip_19 = 243
    fiona_decay_station_y_strip_20 = 244
    fiona_decay_station_y_strip_21 = 245
    fiona_decay_station_y_strip_22 = 246
    fiona_decay_station_y_strip_23 = 247
    fiona_decay_station_y_strip_24 = 248
    fiona_decay_station_y_strip_25 = 249
    fiona_decay_station_y_strip_26 = 250
    fiona_decay_station_y_strip_27 = 251
    fiona_decay_station_y_strip_28 = 252
    fiona_decay_station_y_strip_29 = 253
    fiona_decay_station_y_strip_30 = 254
    fiona_decay_station_y_strip_31 = 255
    # define invDSX 1    // non-zero inverts strip numbers in analysis so they go from  west to east
    # define invDSY 0    // non-zero inverts strip numbers in analysis so they go from bottom to top

    GeE = 256  # Clover detecftor energy signals
    chopper = 27
    TGT = 271
    rutherford_east = 286
    rutherford_west = 287

    # MADC slot 17 is unused

    # TDC slot 18 has the MESYTEC MTDC
    SIT = 288
    GET = 320
