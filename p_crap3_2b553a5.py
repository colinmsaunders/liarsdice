import pprint
from random import randint
import time
from operator import itemgetter

bluff99 = {
    200:46,
    199:46,
    198:45,
    197:45,
    196:45,
    195:45,
    194:44,
    193:44,
    192:44,
    191:44,
    190:44,
    189:44,
    188:44,
    187:43,
    186:43,
    185:43,
    184:42,
    183:42,
    182:42,
    181:42,
    180:42,
    179:41,
    178:41,
    177:41,
    176:41,
    175:41,
    174:41,
    173:40,
    172:40,
    171:40,
    170:40,
    169:39,
    168:39,
    167:39,
    166:39,
    165:39,
    164:38,
    163:38,
    162:38,
    161:38,
    160:38,
    159:37,
    158:37,
    157:37,
    156:37,
    155:37,
    154:37,
    153:36,
    152:36,
    151:36,
    150:36,
    149:36,
    148:35,
    147:35,
    146:35,
    145:35,
    144:34,
    143:34,
    142:34,
    141:34,
    140:34,
    139:33,
    138:33,
    137:33,
    136:33,
    135:33,
    134:32,
    133:32,
    132:32,
    131:32,
    130:32,
    129:31,
    128:31,
    127:31,
    126:31,
    125:30,
    124:30,
    123:30,
    122:30,
    121:30,
    120:30,
    119:30,
    118:29,
    117:29,
    116:29,
    115:29,
    114:28,
    113:28,
    112:28,
    111:28,
    110:28,
    109:27,
    108:27,
    107:27,
    106:27,
    105:27,
    104:26,
    103:26,
    102:26,
    101:25,
    100:26,
    99:25,
    98:25,
    97:25,
    96:25,
    95:24,
    94:24,
    93:24,
    92:24,
    91:24,
    90:24,
    89:23,
    88:23,
    87:23,
    86:23,
    85:22,
    84:22,
    83:22,
    82:22,
    81:21,
    80:21,
    79:21,
    78:21,
    77:21,
    76:20,
    75:20,
    74:20,
    73:20,
    72:20,
    71:19,
    70:19,
    69:19,
    68:19,
    67:19,
    66:18,
    65:18,
    64:18,
    63:18,
    62:17,
    61:17,
    60:17,
    59:17,
    58:17,
    57:16,
    56:16,
    55:16,
    54:16,
    53:15,
    52:15,
    51:15,
    50:15,
    49:15,
    48:14,
    47:14,
    46:14,
    45:14,
    44:13,
    43:13,
    42:13,
    41:13,
    40:12,
    39:12,
    38:12,
    37:12,
    36:11,
    35:11,
    34:11,
    33:11,
    32:10,
    31:10,
    30:10,
    29:10,
    28:10,
    27:9,
    26:9,
    25:9,
    24:9,
    23:8,
    22:8,
    21:8,
    20:7,
    19:7,
    18:7,
    17:7,
    16:6,
    15:6,
    14:6,
    13:6,
    12:5,
    11:5,
    10:5,
    9:4,
    8:4,
    7:4,
    6:3,
    5:3,
    4:3,
    3:2,
    2:2,
    1:1
}

bluff90 = {
    200:40,
    199:40,
    198:39,
    197:39,
    196:39,
    195:39,
    194:39,
    193:39,
    192:39,
    191:38,
    190:38,
    189:38,
    188:38,
    187:38,
    186:37,
    185:37,
    184:37,
    183:37,
    182:37,
    181:36,
    180:36,
    179:36,
    178:36,
    177:36,
    176:36,
    175:35,
    174:35,
    173:35,
    172:35,
    171:35,
    170:34,
    169:34,
    168:34,
    167:34,
    166:34,
    165:34,
    164:33,
    163:33,
    162:33,
    161:33,
    160:33,
    159:32,
    158:32,
    157:32,
    156:32,
    155:32,
    154:31,
    153:31,
    152:31,
    151:31,
    150:31,
    149:31,
    148:30,
    147:30,
    146:30,
    145:30,
    144:30,
    143:29,
    142:29,
    141:29,
    140:29,
    139:29,
    138:28,
    137:28,
    136:28,
    135:28,
    134:28,
    133:28,
    132:27,
    131:27,
    130:27,
    129:27,
    128:27,
    127:26,
    126:26,
    125:26,
    124:26,
    123:26,
    122:25,
    121:25,
    120:25,
    119:25,
    118:25,
    117:25,
    116:24,
    115:24,
    114:24,
    113:24,
    112:24,
    111:23,
    110:23,
    109:23,
    108:23,
    107:23,
    106:23,
    105:22,
    104:22,
    103:22,
    102:22,
    101:21,
    100:21,
    99:21,
    98:21,
    97:21,
    96:21,
    95:20,
    94:20,
    93:20,
    92:20,
    91:20,
    90:20,
    89:19,
    88:19,
    87:19,
    86:19,
    85:19,
    84:18,
    83:18,
    82:18,
    81:18,
    80:18,
    79:17,
    78:17,
    77:17,
    76:17,
    75:17,
    74:16,
    73:16,
    72:16,
    71:16,
    70:16,
    69:15,
    68:15,
    67:15,
    66:15,
    65:15,
    64:14,
    63:14,
    62:14,
    61:14,
    60:14,
    59:13,
    58:13,
    57:13,
    56:13,
    55:13,
    54:13,
    53:12,
    52:12,
    51:12,
    50:12,
    49:12,
    48:11,
    47:11,
    46:11,
    45:11,
    44:10,
    43:10,
    42:10,
    41:10,
    40:10,
    39:9,
    38:9,
    37:9,
    36:9,
    35:9,
    34:9,
    33:8,
    32:8,
    31:8,
    30:8,
    29:7,
    28:7,
    27:7,
    26:7,
    25:7,
    24:6,
    23:6,
    22:6,
    21:6,
    20:5,
    19:5,
    18:5,
    17:5,
    16:5,
    15:4,
    14:4,
    13:4,
    12:4,
    11:3,
    10:3,
    9:3,
    8:3,
    7:2,
    6:2,
    5:2,
    4:2,
    3:1,
    2:1,
    1:1
}

bluff80 = {
    200:38,
    199:37,
    198:37,
    197:37,
    196:37,
    195:37,
    194:37,
    193:36,
    192:36,
    191:36,
    190:36,
    189:36,
    188:35,
    187:35,
    186:35,
    185:35,
    184:35,
    183:35,
    182:34,
    181:34,
    180:34,
    179:34,
    178:34,
    177:33,
    176:33,
    175:33,
    174:33,
    173:33,
    172:33,
    171:32,
    170:32,
    169:32,
    168:32,
    167:32,
    166:32,
    165:31,
    164:31,
    163:31,
    162:31,
    161:30,
    160:30,
    159:30,
    158:30,
    157:30,
    156:30,
    155:30,
    154:29,
    153:29,
    152:29,
    151:29,
    150:29,
    149:29,
    148:28,
    147:28,
    146:28,
    145:28,
    144:28,
    143:28,
    142:27,
    141:27,
    140:27,
    139:27,
    138:26,
    137:26,
    136:26,
    135:26,
    134:26,
    133:25,
    132:25,
    131:25,
    130:25,
    129:25,
    128:25,
    127:25,
    126:24,
    125:24,
    124:24,
    123:24,
    122:24,
    121:23,
    120:23,
    119:23,
    118:23,
    117:23,
    116:23,
    115:22,
    114:22,
    113:22,
    112:22,
    111:22,
    110:21,
    109:21,
    108:21,
    107:21,
    106:21,
    105:21,
    104:20,
    103:20,
    102:20,
    101:20,
    100:20,
    99:20,
    98:19,
    97:19,
    96:19,
    95:19,
    94:19,
    93:18,
    92:18,
    91:18,
    90:18,
    89:18,
    88:18,
    87:17,
    86:17,
    85:17,
    84:17,
    83:17,
    82:16,
    81:16,
    80:16,
    79:16,
    78:16,
    77:15,
    76:15,
    75:15,
    74:15,
    73:15,
    72:15,
    71:14,
    70:14,
    69:14,
    68:14,
    67:14,
    66:13,
    65:13,
    64:13,
    63:13,
    62:13,
    61:12,
    60:12,
    59:12,
    58:12,
    57:12,
    56:12,
    55:11,
    54:11,
    53:11,
    52:11,
    51:11,
    50:10,
    49:10,
    48:10,
    47:10,
    46:10,
    45:10,
    44:9,
    43:9,
    42:9,
    41:9,
    40:9,
    39:8,
    38:8,
    37:8,
    36:8,
    35:8,
    34:7,
    33:7,
    32:7,
    31:7,
    30:7,
    29:6,
    28:6,
    27:6,
    26:6,
    25:6,
    24:5,
    23:5,
    22:5,
    21:5,
    20:5,
    19:4,
    18:4,
    17:4,
    16:4,
    15:4,
    14:3,
    13:3,
    12:3,
    11:3,
    10:3,
    9:2,
    8:2,
    7:2,
    6:2,
    5:1,
    4:1,
    3:1,
    2:1,
    1:0
}

bluff70 = {
    200:36,
    199:36,
    198:36,
    197:35,
    196:35,
    195:35,
    194:35,
    193:35,
    192:35,
    191:34,
    190:34,
    189:34,
    188:34,
    187:34,
    186:33,
    185:33,
    184:33,
    183:33,
    182:33,
    181:33,
    180:32,
    179:32,
    178:32,
    177:32,
    176:32,
    175:31,
    174:31,
    173:31,
    172:31,
    171:31,
    170:31,
    169:30,
    168:30,
    167:30,
    166:30,
    165:30,
    164:30,
    163:29,
    162:29,
    161:29,
    160:29,
    159:29,
    158:29,
    157:28,
    156:28,
    155:28,
    154:28,
    153:28,
    152:28,
    151:27,
    150:27,
    149:27,
    148:27,
    147:27,
    146:26,
    145:26,
    144:26,
    143:26,
    142:26,
    141:26,
    140:25,
    139:25,
    138:25,
    137:25,
    136:25,
    135:25,
    134:24,
    133:24,
    132:24,
    131:24,
    130:24,
    129:23,
    128:23,
    127:23,
    126:23,
    125:23,
    124:23,
    123:23,
    122:22,
    121:22,
    120:22,
    119:22,
    118:22,
    117:21,
    116:21,
    115:21,
    114:21,
    113:21,
    112:21,
    111:20,
    110:20,
    109:20,
    108:20,
    107:20,
    106:20,
    105:19,
    104:19,
    103:19,
    102:19,
    101:19,
    100:18,
    99:18,
    98:18,
    97:18,
    96:18,
    95:18,
    94:17,
    93:17,
    92:17,
    91:17,
    90:17,
    89:16,
    88:16,
    87:16,
    86:16,
    85:16,
    84:16,
    83:15,
    82:15,
    81:15,
    80:15,
    79:15,
    78:15,
    77:14,
    76:14,
    75:14,
    74:14,
    73:14,
    72:13,
    71:13,
    70:13,
    69:13,
    68:13,
    67:13,
    66:12,
    65:12,
    64:12,
    63:12,
    62:12,
    61:11,
    60:11,
    59:11,
    58:11,
    57:11,
    56:11,
    55:10,
    54:10,
    53:10,
    52:10,
    51:10,
    50:10,
    49:9,
    48:9,
    47:9,
    46:9,
    45:9,
    44:8,
    43:8,
    42:8,
    41:8,
    40:8,
    39:8,
    38:7,
    37:7,
    36:7,
    35:7,
    34:7,
    33:6,
    32:6,
    31:6,
    30:6,
    29:6,
    28:6,
    27:5,
    26:5,
    25:5,
    24:5,
    23:5,
    22:4,
    21:4,
    20:4,
    19:4,
    18:4,
    17:3,
    16:3,
    15:3,
    14:3,
    13:3,
    12:3,
    11:2,
    10:2,
    9:2,
    8:2,
    7:2,
    6:1,
    5:1,
    4:1,
    3:1,
    2:0,
    1:0
}

bluff60 = {
    200:34,
    199:34,
    198:34,
    197:34,
    196:34,
    195:34,
    194:33,
    193:33,
    192:33,
    191:33,
    190:33,
    189:33,
    188:32,
    187:32,
    186:32,
    185:32,
    184:32,
    183:32,
    182:31,
    181:31,
    180:31,
    179:31,
    178:31,
    177:31,
    176:30,
    175:30,
    174:30,
    173:30,
    172:30,
    171:30,
    170:29,
    169:29,
    168:29,
    167:29,
    166:29,
    165:29,
    164:28,
    163:28,
    162:28,
    161:28,
    160:28,
    159:28,
    158:27,
    157:27,
    156:27,
    155:27,
    154:27,
    153:27,
    152:26,
    151:26,
    150:26,
    149:26,
    148:26,
    147:25,
    146:25,
    145:25,
    144:25,
    143:25,
    142:25,
    141:24,
    140:24,
    139:24,
    138:24,
    137:24,
    136:24,
    135:23,
    134:23,
    133:23,
    132:23,
    131:23,
    130:23,
    129:22,
    128:22,
    127:22,
    126:22,
    125:22,
    124:21,
    123:21,
    122:21,
    121:21,
    120:21,
    119:21,
    118:21,
    117:20,
    116:20,
    115:20,
    114:20,
    113:20,
    112:20,
    111:19,
    110:19,
    109:19,
    108:19,
    107:19,
    106:18,
    105:18,
    104:18,
    103:18,
    102:18,
    101:18,
    100:17,
    99:17,
    98:17,
    97:17,
    96:17,
    95:17,
    94:16,
    93:16,
    92:16,
    91:16,
    90:16,
    89:16,
    88:15,
    87:15,
    86:15,
    85:15,
    84:15,
    83:15,
    82:14,
    81:14,
    80:14,
    79:14,
    78:14,
    77:13,
    76:13,
    75:13,
    74:13,
    73:13,
    72:13,
    71:12,
    70:12,
    69:12,
    68:12,
    67:12,
    66:12,
    65:11,
    64:11,
    63:11,
    62:11,
    61:11,
    60:11,
    59:10,
    58:10,
    57:10,
    56:10,
    55:10,
    54:9,
    53:9,
    52:9,
    51:9,
    50:9,
    49:9,
    48:8,
    47:8,
    46:8,
    45:8,
    44:8,
    43:8,
    42:8,
    41:7,
    40:7,
    39:7,
    38:7,
    37:7,
    36:6,
    35:6,
    34:6,
    33:6,
    32:6,
    31:6,
    30:5,
    29:5,
    28:5,
    27:5,
    26:5,
    25:5,
    24:4,
    23:4,
    22:4,
    21:4,
    20:4,
    19:3,
    18:3,
    17:3,
    16:3,
    15:3,
    14:3,
    13:2,
    12:2,
    11:2,
    10:2,
    9:2,
    8:1,
    7:1,
    6:1,
    5:1,
    4:1,
    3:1,
    3:0,
    2:0,
    1:0
}

bluff55 = {
    200:34,
    199:34,
    198:33,
    197:33,
    196:33,
    195:33,
    194:33,
    193:33,
    192:32,
    191:32,
    190:32,
    189:32,
    188:32,
    187:32,
    186:31,
    185:31,
    184:31,
    183:31,
    182:31,
    181:31,
    180:30,
    179:30,
    178:30,
    177:30,
    176:30,
    175:30,
    174:29,
    173:29,
    172:29,
    171:29,
    170:29,
    169:29,
    168:28,
    167:28,
    166:28,
    165:28,
    164:28,
    163:28,
    162:27,
    161:27,
    160:27,
    159:27,
    158:27,
    157:26,
    156:26,
    155:26,
    154:26,
    153:26,
    152:26,
    151:26,
    150:25,
    149:25,
    148:25,
    147:25,
    146:25,
    145:25,
    144:24,
    143:24,
    142:24,
    141:24,
    140:24,
    139:24,
    138:23,
    137:23,
    136:23,
    135:23,
    134:23,
    133:23,
    132:22,
    131:22,
    130:22,
    129:22,
    128:22,
    127:22,
    126:21,
    125:21,
    124:21,
    123:21,
    122:21,
    121:20,
    120:20,
    119:20,
    118:20,
    117:20,
    116:20,
    115:19,
    114:19,
    113:19,
    112:19,
    111:19,
    110:19,
    109:18,
    108:18,
    107:18,
    106:18,
    105:18,
    104:18,
    103:17,
    102:17,
    101:17,
    100:17,
    99:17,
    98:17,
    97:16,
    96:16,
    95:16,
    94:16,
    93:16,
    92:16,
    91:15,
    90:15,
    89:15,
    88:15,
    87:15,
    86:15,
    85:14,
    84:14,
    83:14,
    82:14,
    81:14,
    80:14,
    79:13,
    78:13,
    77:13,
    76:13,
    75:13,
    74:13,
    73:12,
    72:12,
    71:12,
    70:12,
    69:12,
    68:12,
    67:11,
    66:11,
    65:11,
    64:11,
    63:11,
    62:10,
    61:10,
    60:10,
    59:10,
    58:10,
    57:10,
    56:9,
    55:9,
    54:9,
    53:9,
    52:9,
    51:9,
    50:8,
    49:8,
    48:8,
    47:8,
    46:8,
    45:8,
    44:7,
    43:7,
    42:7,
    41:7,
    40:7,
    39:7,
    38:6,
    37:6,
    36:6,
    35:6,
    34:6,
    33:6,
    32:5,
    31:5,
    30:5,
    29:5,
    28:5,
    27:5,
    26:4,
    25:4,
    24:4,
    23:4,
    22:4,
    21:4,
    20:3,
    19:3,
    18:3,
    17:3,
    16:3,
    15:3,
    14:2,
    13:2,
    12:2,
    11:2,
    10:2,
    9:1,
    8:1,
    7:1,
    6:1,
    5:1,
    4:1,
    3:0,
    2:0,
    1:0
}

bluff50 = {
    200:33,
    199:33,
    198:33,
    197:33,
    196:33,
    195:32,
    194:32,
    193:32,
    192:32,
    191:31,
    190:31,
    189:31,
    188:31,
    187:31,
    186:31,
    185:31,
    184:30,
    183:30,
    182:30,
    181:30,
    180:30,
    179:30,
    178:29,
    177:29,
    176:29,
    175:29,
    174:29,
    173:29,
    172:28,
    171:28,
    170:28,
    169:28,
    168:28,
    167:28,
    166:28,
    165:27,
    164:27,
    163:27,
    162:27,
    161:27,
    160:26,
    159:26,
    158:26,
    157:26,
    156:26,
    155:26,
    154:25,
    153:25,
    152:25,
    151:25,
    150:25,
    149:25,
    148:24,
    147:24,
    146:24,
    145:24,
    144:24,
    143:24,
    142:23,
    141:23,
    140:23,
    139:23,
    138:23,
    137:23,
    136:22,
    135:22,
    134:22,
    133:22,
    132:22,
    131:22,
    130:21,
    129:21,
    128:21,
    127:21,
    126:21,
    125:21,
    124:20,
    123:20,
    122:20,
    121:20,
    120:20,
    119:20,
    118:19,
    117:19,
    116:19,
    115:19,
    114:19,
    113:19,
    112:19,
    111:18,
    110:18,
    109:18,
    108:18,
    107:18,
    106:17,
    105:17,
    104:17,
    103:17,
    102:17,
    101:17,
    100:16,
    99:16,
    98:16,
    97:16,
    96:16,
    95:16,
    94:15,
    93:15,
    92:15,
    91:15,
    90:15,
    89:15,
    88:14,
    87:14,
    86:14,
    85:14,
    84:14,
    83:14,
    82:13,
    81:13,
    80:13,
    79:13,
    78:13,
    77:13,
    76:12,
    75:12,
    74:12,
    73:12,
    72:12,
    71:12,
    70:12,
    69:11,
    68:11,
    67:11,
    66:11,
    65:11,
    64:10,
    63:10,
    62:10,
    61:10,
    60:10,
    59:10,
    58:9,
    57:9,
    56:9,
    55:9,
    54:9,
    53:9,
    52:8,
    51:8,
    50:8,
    49:8,
    48:8,
    47:8,
    46:8,
    45:7,
    44:7,
    43:7,
    42:7,
    41:7,
    40:6,
    39:6,
    38:6,
    37:6,
    36:6,
    35:6,
    34:6,
    33:5,
    32:5,
    31:5,
    30:5,
    29:5,
    28:5,
    27:4,
    26:4,
    25:4,
    24:4,
    23:4,
    22:4,
    21:3,
    20:3,
    19:3,
    18:3,
    17:3,
    16:3,
    15:2,
    14:2,
    13:2,
    12:2,
    11:2,
    10:2,
    9:1,
    8:1,
    7:1,
    6:1,
    5:1,
    4:1,
    3:0,
    2:0,
    1:0
}

bluff40 = {
    200:32,
    199:32,
    198:31,
    197:31,
    196:31,
    195:31,
    194:31,
    193:31,
    192:30,
    191:30,
    190:30,
    189:30,
    188:30,
    187:30,
    186:30,
    185:29,
    184:29,
    183:29,
    182:29,
    181:29,
    180:29,
    179:28,
    178:28,
    177:28,
    176:28,
    175:28,
    174:27,
    173:27,
    172:27,
    171:27,
    170:27,
    169:27,
    168:27,
    167:26,
    166:26,
    165:26,
    164:26,
    163:26,
    162:25,
    161:25,
    160:25,
    159:25,
    158:25,
    157:25,
    156:24,
    155:24,
    154:24,
    153:24,
    152:24,
    151:24,
    150:24,
    149:23,
    148:23,
    147:23,
    146:23,
    145:23,
    144:23,
    143:22,
    142:22,
    141:22,
    140:22,
    139:22,
    138:22,
    137:22,
    136:21,
    135:21,
    134:21,
    133:21,
    132:21,
    131:21,
    130:20,
    129:20,
    128:20,
    127:20,
    126:20,
    125:20,
    124:19,
    123:19,
    122:19,
    121:19,
    120:19,
    119:19,
    118:18,
    117:18,
    116:18,
    115:18,
    114:18,
    113:18,
    112:18,
    111:17,
    110:17,
    109:17,
    108:17,
    107:17,
    106:16,
    105:16,
    104:16,
    103:16,
    102:16,
    101:16,
    100:16,
    99:15,
    98:15,
    97:15,
    96:15,
    95:15,
    94:15,
    93:14,
    92:14,
    91:14,
    90:14,
    89:14,
    88:14,
    87:13,
    86:13,
    85:13,
    84:13,
    83:13,
    82:13,
    81:12,
    80:12,
    79:12,
    78:12,
    77:12,
    76:12,
    75:11,
    74:11,
    73:11,
    72:11,
    71:11,
    70:11,
    69:11,
    68:10,
    67:10,
    66:10,
    65:10,
    64:10,
    63:10,
    62:9,
    61:9,
    60:9,
    59:9,
    58:9,
    57:9,
    56:8,
    55:8,
    54:8,
    53:8,
    52:8,
    51:8,
    50:7,
    49:7,
    48:7,
    47:7,
    46:7,
    45:7,
    44:7,
    43:6,
    42:6,
    41:6,
    40:6,
    39:6,
    38:6,
    37:5,
    36:5,
    35:5,
    34:5,
    33:5,
    32:5,
    31:4,
    30:4,
    29:4,
    28:4,
    27:4,
    26:4,
    25:4,
    24:3,
    23:3,
    22:3,
    21:3,
    20:3,
    19:3,
    18:2,
    17:2,
    16:2,
    15:2,
    14:2,
    13:2,
    12:2,
    11:1,
    10:1,
    9:1,
    8:1,
    7:1,
    6:1,
    5:0,
    4:0,
    3:0,
    2:0,
    1:0
}

bluff30 = {
    200:30,
    199:30,
    198:30,
    197:30,
    196:30,
    195:30,
    194:29,
    193:29,
    192:29,
    191:29,
    190:29,
    189:29,
    188:28,
    187:28,
    186:28,
    185:28,
    184:28,
    183:28,
    182:27,
    181:27,
    180:27,
    179:27,
    178:27,
    177:27,
    176:27,
    175:26,
    174:26,
    173:26,
    172:26,
    171:26,
    170:26,
    169:25,
    168:25,
    167:25,
    166:25,
    165:25,
    164:25,
    163:24,
    162:24,
    161:24,
    160:24,
    159:24,
    158:24,
    157:23,
    156:23,
    155:23,
    154:23,
    153:23,
    152:23,
    151:22,
    150:22,
    149:22,
    148:22,
    147:22,
    146:22,
    145:22,
    144:21,
    143:21,
    142:21,
    141:21,
    140:21,
    139:21,
    138:21,
    137:20,
    136:20,
    135:20,
    134:20,
    133:20,
    132:19,
    131:19,
    130:19,
    129:19,
    128:19,
    127:19,
    126:19,
    125:18,
    124:18,
    123:18,
    122:18,
    121:18,
    120:18,
    119:18,
    118:17,
    117:17,
    116:17,
    115:17,
    114:17,
    113:17,
    112:17,
    111:16,
    110:16,
    109:16,
    108:16,
    107:16,
    106:15,
    105:15,
    104:15,
    103:15,
    102:15,
    101:15,
    100:15,
    99:14,
    98:14,
    97:14,
    96:14,
    95:14,
    94:14,
    93:13,
    92:13,
    91:13,
    90:13,
    89:13,
    88:13,
    87:13,
    86:12,
    85:12,
    84:12,
    83:12,
    82:12,
    81:12,
    80:11,
    79:11,
    78:11,
    77:11,
    76:11,
    75:11,
    74:10,
    73:10,
    72:10,
    71:10,
    70:10,
    69:10,
    68:10,
    67:9,
    66:9,
    65:9,
    64:9,
    63:9,
    62:9,
    61:8,
    60:8,
    59:8,
    58:8,
    57:8,
    56:8,
    55:8,
    54:7,
    53:7,
    52:7,
    51:7,
    50:7,
    49:7,
    48:7,
    47:6,
    46:6,
    45:6,
    44:6,
    43:6,
    42:6,
    41:5,
    40:5,
    39:5,
    38:5,
    37:5,
    36:5,
    35:5,
    34:4,
    33:4,
    32:4,
    31:4,
    30:4,
    29:4,
    28:3,
    27:3,
    26:3,
    25:3,
    24:3,
    23:3,
    22:3,
    21:2,
    20:2,
    19:2,
    18:2,
    17:2,
    16:2,
    15:2,
    14:1,
    13:1,
    12:1,
    11:1,
    10:1,
    9:1,
    8:1,
    7:1,
    6:0,
    5:0,
    4:0,
    3:0,
    2:0,
    1:0
}

bluff20 = {
    200:29,
    199:28,
    198:28,
    197:28,
    196:28,
    195:28,
    194:28,
    193:28,
    192:28,
    191:27,
    190:27,
    189:27,
    188:27,
    187:27,
    186:27,
    185:26,
    184:26,
    183:26,
    182:26,
    181:26,
    180:26,
    179:25,
    178:25,
    177:25,
    176:25,
    175:25,
    174:25,
    173:24,
    172:24,
    171:24,
    170:24,
    169:24,
    168:24,
    167:24,
    166:23,
    165:23,
    164:23,
    163:23,
    162:23,
    161:23,
    160:23,
    159:22,
    158:22,
    157:22,
    156:22,
    155:22,
    154:22,
    153:21,
    152:21,
    151:21,
    150:21,
    149:21,
    148:21,
    147:20,
    146:20,
    145:20,
    144:20,
    143:20,
    142:20,
    141:20,
    140:19,
    139:19,
    138:19,
    137:19,
    136:19,
    135:19,
    134:18,
    133:18,
    132:18,
    131:18,
    130:18,
    129:18,
    128:18,
    127:17,
    126:17,
    125:17,
    124:17,
    123:17,
    122:17,
    121:17,
    120:16,
    119:16,
    118:16,
    117:16,
    116:16,
    115:16,
    114:16,
    113:15,
    112:15,
    111:15,
    110:15,
    109:15,
    108:15,
    107:15,
    106:14,
    105:14,
    104:14,
    103:14,
    102:14,
    101:14,
    100:13,
    99:13,
    98:13,
    97:13,
    96:13,
    95:12,
    94:12,
    93:12,
    92:12,
    91:12,
    90:12,
    89:12,
    88:12,
    87:11,
    86:11,
    85:11,
    84:11,
    83:11,
    82:11,
    81:11,
    80:10,
    79:10,
    78:10,
    77:10,
    76:10,
    75:10,
    74:10,
    73:9,
    72:9,
    71:9,
    70:9,
    69:9,
    68:9,
    67:9,
    66:8,
    65:8,
    64:8,
    63:8,
    62:8,
    61:8,
    60:7,
    59:7,
    58:7,
    57:7,
    56:7,
    55:7,
    54:7,
    53:6,
    52:6,
    51:6,
    50:6,
    49:6,
    48:6,
    47:6,
    46:5,
    45:5,
    44:5,
    43:5,
    42:5,
    41:5,
    40:5,
    39:4,
    38:4,
    37:4,
    36:4,
    35:4,
    34:4,
    33:4,
    32:3,
    31:3,
    30:3,
    29:3,
    28:3,
    27:3,
    26:3,
    25:3,
    24:2,
    23:2,
    22:2,
    21:2,
    20:2,
    19:2,
    18:2,
    17:1,
    16:1,
    15:1,
    14:1,
    13:1,
    12:1,
    11:1,
    10:1,
    9:1,
    8:0,
    7:0,
    6:0,
    5:0,
    4:0,
    3:0,
    2:0,
    1:0
}

bluff10 = {
    200:26,
    199:26,
    198:26,
    197:26,
    196:26,
    195:26,
    194:26,
    193:25,
    192:25,
    191:25,
    190:25,
    189:25,
    188:25,
    187:25,
    186:25,
    185:24,
    184:24,
    183:24,
    182:24,
    181:24,
    180:24,
    179:23,
    178:23,
    177:23,
    176:23,
    175:23,
    174:23,
    173:22,
    172:22,
    171:22,
    170:22,
    169:22,
    168:22,
    167:22,
    166:22,
    165:21,
    164:21,
    163:21,
    162:21,
    161:21,
    160:20,
    159:20,
    158:20,
    157:20,
    156:20,
    155:20,
    154:20,
    153:20,
    152:19,
    151:19,
    150:19,
    149:19,
    148:19,
    147:19,
    146:18,
    145:18,
    144:18,
    143:18,
    142:18,
    141:18,
    140:18,
    139:17,
    138:17,
    137:17,
    136:17,
    135:17,
    134:17,
    133:17,
    132:17,
    131:16,
    130:16,
    129:16,
    128:16,
    127:16,
    126:16,
    125:15,
    124:15,
    123:15,
    122:15,
    121:15,
    120:15,
    119:15,
    118:14,
    117:14,
    116:14,
    115:14,
    114:14,
    113:14,
    112:14,
    111:13,
    110:13,
    109:13,
    108:13,
    107:13,
    106:13,
    105:13,
    104:13,
    103:12,
    102:12,
    101:12,
    100:12,
    99:12,
    98:12,
    97:11,
    96:11,
    95:11,
    94:11,
    93:11,
    92:11,
    91:11,
    90:10,
    89:10,
    88:10,
    87:10,
    86:10,
    85:10,
    84:10,
    83:9,
    82:9,
    81:9,
    80:9,
    79:9,
    78:9,
    77:9,
    76:9,
    75:8,
    74:8,
    73:8,
    72:8,
    71:8,
    70:8,
    69:8,
    68:7,
    67:7,
    66:7,
    65:7,
    64:7,
    63:7,
    62:7,
    61:6,
    60:6,
    59:6,
    58:6,
    57:6,
    56:6,
    55:6,
    54:5,
    53:5,
    52:5,
    51:5,
    50:5,
    49:5,
    48:5,
    47:5,
    46:4,
    45:4,
    44:4,
    43:4,
    42:4,
    41:4,
    40:4,
    39:4,
    38:3,
    37:3,
    36:3,
    35:3,
    34:3,
    33:3,
    32:3,
    31:3,
    30:2,
    29:2,
    28:2,
    27:2,
    26:2,
    25:2,
    24:2,
    23:2,
    22:1,
    21:1,
    20:1,
    19:1,
    18:1,
    17:1,
    16:1,
    15:1,
    14:1,
    13:1,
    12:0,
    11:0,
    10:0,
    9:0,
    8:0,
    7:0,
    6:0,
    5:0,
    4:0,
    3:0,
    2:0,
    1:0
}


# These equations are too simplistic
compute_bluff = {1.0:lambda dice: bluff99[dice],
                 0.01:lambda dice: 0,
                 0.1:lambda dice: bluff10[dice],
                 0.2:lambda dice: bluff20[dice],
                 0.3:lambda dice: bluff30[dice],
                 0.4:lambda dice: bluff40[dice],
                 0.5:lambda dice: bluff50[dice],
                 0.55:lambda dice: bluff55[dice],
                 0.6:lambda dice: bluff60[dice],
                 0.7:lambda dice: bluff70[dice],
                 0.8:lambda dice: bluff80[dice],
                 0.9:lambda dice: bluff90[dice],
                 0.99:lambda dice: bluff99[dice]
                }
HIST_LEN=100

stats = {}

BUCKET_KEYS = sorted(compute_bluff.keys())

stattime = 0.0
totaltime = 0.0

def init_stats(hands):
    global stats
    for player in hands:
        stats[player] = {}
        stats[player]['calls'] = []
        stats[player]['called'] = []
        stats[player]['call_chances'] = 0

def update_stats(me, hands, plays):
    global stats

    if not stats:
        init_stats(hands)

    if len(plays) < 2:
        return

    caller = plays[-1]['player']
    callee = plays[-2]['player']
    called_num, called_face = plays[-2]['num'], plays[-2]['face']

    num_dice = sum([sum(hands[player].values()) for player in hands])

    curr_caller_dice = sum(hands[caller].values())
    curr_callee_dice = sum(hands[callee].values())

    actual_number_of_called_face = \
        sum([hands[player].get(called_face,0) for player in hands])
    if actual_number_of_called_face >= called_num:
        winner = callee
    else:
        winner = caller

    state = (num_dice, curr_caller_dice, curr_callee_dice, 
             called_num, called_face, caller, callee, winner, len(plays))
    stats[caller]['calls'].append(state)
    stats[callee]['called'].append(state)

    # Track number of call opportunities for each player
    for index in range(len(plays)-1, 0, -1):
        stats[plays[index]['player']]['call_chances'] += 1

    #print 'careful10 stats'
    #pprint.pprint(stats)

def bucketize(percent):
    for key in BUCKET_KEYS:
        if percent <= key:
            return key
    return key

def get_num_dice(hands):
    num = 0
    for player in hands.split(','):
        num += len(player.split(':')[1])
    return num

def get_prev_plays(history):
    prev_plays = []
    if not history:
        return prev_plays

    for prev_play in history.split(','):
        player, play = prev_play.split(':')
        play = int(play)
        num = play / 10
        face = play % 10
        play_dict = dict(player=player, num=num, face=face)
        prev_plays.append(play_dict)
    return prev_plays

def get_hands(in_hands):
    hands = {}
    for player_hand in in_hands.split(','):
        player, hand = player_hand.split(':')
        hands[player] = {}
        for die in hand:
            if die != 'x':
                die = int(die)
            if die in hands[player]:
                hands[player][die] += 1
            else:
                hands[player][die] = 1
    return hands

def get_play(me,hands,history) :
    global stattime
    global totaltime

    start = time.time()
    num_dice = get_num_dice(hands)
    player_hands = get_hands(hands)
    plays = get_prev_plays(history)
    if plays and plays[-1]['num'] == 0:
        # last play was a call
        update_stats(me, player_hands, plays)
        return 0

    prev_faces = {}
    for play in plays:
        if play['player'] != me:
            if play['face'] not in prev_faces:
                prev_faces[play['face']] = 1
            else:
                prev_faces[play['face']] += 1

    next_player = get_next_player(me, player_hands)
    call_likelihood = get_call_likelihood(next_player)

    my_dice = player_hands[me]
    num_other_dice = num_dice - sum(my_dice.values())
    num_active_players = len([player for player in player_hands if player_hands[player]]) - 1

    player_count_risk_level = num_active_players ** 0.8

    #bluff_qty = compute_bluff[0.3](num_other_dice)
    #bluff_qty = compute_bluff[bucketize(0.39 -call_likelihood)](num_other_dice)
    tmp_likelihood = call_likelihood ** 0.6
    bluff_qty = compute_bluff[bucketize(0.6/tmp_likelihood/player_count_risk_level)](num_other_dice)
    #bluff_qty = compute_bluff[0.6](num_other_dice)

    if num_active_players == 2 and bluff_qty >= num_other_dice:
        bluff_qty -= 1

    if my_dice:
        my_max_num = max(my_dice.values())
    else:
        my_max_num = 0

    if len(plays) == 0:
        last_play=dict(num=1,face=0)
    else:
        last_play = plays[-1]

    # Play the biggest hand we could reasonably play
    last_face = last_play['face']
    last_num = last_play['num']
    for possible_num in range(my_max_num+bluff_qty,0,-1):
        for possible_face in range(6,0,-1):
            if (my_dice.get(possible_face, 0) + bluff_qty) >= possible_num and \
                (possible_num > last_num or (possible_num == last_num and 
                                             possible_face > last_face)):
                return possible_num*10 + possible_face

    # Do we really want to call?  How conservative is the callee?
    prev_player = plays[-1]['player']
    conserv_rating = get_conserv_rating(prev_player)

    #call_likelihood = call_likelihood ** 0.6
    call_likelihood = call_likelihood ** 0.6
    player_count_risk_level = num_active_players ** 0.2
    max_worthwhile = compute_bluff[bucketize(conserv_rating/call_likelihood/player_count_risk_level)](num_other_dice)
    #max_worthwhile = compute_bluff[bucketize(conserv_rating/call_likelihood)](num_other_dice)
    #lowest_qty = my_max_num + bluff_qty + 1
    lowest_qty = bluff_qty + 1

    if num_active_players == 2 and max_worthwhile >= num_other_dice:
        max_worthwhile -= 1

    # Look at faces in order of how many I have.
    for num in range(1,7):
        if num not in my_dice:
            my_dice[num] = 0

    sorted_dice = sorted(my_dice.iteritems(), key=itemgetter(1), reverse=True)
    sorted_faces = [face for (face, num) in sorted_dice]
    for possible_num in range(lowest_qty, max_worthwhile + 1):
        for possible_face in sorted_faces:
            estimated_num = my_dice.get(possible_face, 0) + possible_num
            if estimated_num > last_num or (estimated_num == last_num and 
                                             possible_face > last_face):
                return estimated_num*10 + possible_face

    # Ok, try going one higher for just those faces we've seen before
    sorted_prev_dice = sorted(prev_faces.iteritems(), key=itemgetter(1), reverse=True)
    sorted_faces = [face for (face, num) in sorted_prev_dice if num>1]
    #sorted_faces = [face for (face, num) in sorted_prev_dice][-2:]
    possible_num = max_worthwhile + 1
    for possible_face in sorted_faces:
        estimated_num = my_dice.get(possible_face, 0) + possible_num
        if estimated_num > last_num or (estimated_num == last_num and 
                                         possible_face > last_face):
            return estimated_num*10 + possible_face

    totaltime += time.time() - start
    return 0

def get_next_player(me, player_hands):
    next = None
    curr = me
    while next == None:
        possible_next = chr(ord(curr) + 1)
        if possible_next not in player_hands:
            possible_next = 'A'
        if sum(player_hands[possible_next].values()) > 0:
            next = possible_next
        else:
            curr = possible_next

    return next



def get_call_likelihood(player):
    global stats

    if player not in stats:
        diff = 1.0
        return diff

    # How often did this player call?
    #print stats[player]
    num_player_calls = len(stats[player]['calls'])
    num_call_chances = stats[player]['call_chances']
    if num_call_chances:
        percent_calls = 1.0*num_player_calls/num_call_chances
    else:
        return 1.0

    # What percent would an average player make?
    average_percent_calls = 0.5

    likelihood = max(percent_calls/average_percent_calls, 0.25)

    return likelihood

def get_conserv_rating(player):
    global stats

    if player not in stats:
        return 0.5

    hist_len = min(HIST_LEN, len(stats[player]['called']))
    if hist_len == 0:
        return 0.75

    callee_history = stats[player]['called'][-hist_len:]
    rating = 1.0*len([play for play in callee_history if play[7] == player])/hist_len
    # Modify rating by tuned value.
    rating = rating**0.3
    rating = min(1.0, rating)
    return rating

