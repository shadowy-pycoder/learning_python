#!/usr/bin/env python3
# 2149583361 -> "128.32.10.1"
# 32         -> "0.0.0.32"
# 0          -> "0.0.0.0"

def int32_to_ip(int32: int) -> str:
    '''Converts 32-bit integers to human-readable IPv4-address'''
    try:
        int32 = abs(int(int32))
    except ValueError:
        raise SystemExit('Invalid integer')
    if len(f'{int32:b}') > 32:
        raise SystemExit('Invalid integer')
    int8 = f'{int32:0>8x}'
    ip_addr = '.'.join(str(int(int8[i:i+2], 16))
                       for i in range(0, len(int8), 2))
    return ip_addr


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip('1') == "0.0.0.1"
assert int32_to_ip(-1) == "0.0.0.1"
assert int32_to_ip('-1') == "0.0.0.1"
