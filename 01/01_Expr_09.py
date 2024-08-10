def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]), int(t[1]), int(t[2])

def hms2str(h, m, s):
    return ('0'+str(h))[-2:]+':'+('0'+str(m))[-2:]+':'+('0'+str(s))[-2:]

def to_sec(h, m, s):
    return s+m*60+h*3600

def to_hms(s):
    hours = s//3600
    minutes = (s-hours*3600)//60
    seconds = s-hours*3600-minutes*60
    return hours, minutes, seconds

def diff(h1, m1, s1, h2, m2, s2):
    second_1 = to_sec(h1, m1, s1)
    second_2 = to_sec(h2, m2, s2)
    d = second_2-second_1
    return to_hms(d)

def main():
    hms_start = list(str2hms(input()))
    hms_end = list(str2hms(input()))
    diffs = diff(hms_start[0], hms_start[1], hms_start[2], hms_end[0], hms_end[1], hms_end[2])
    print(hms2str(diffs[0], diffs[1], diffs[2]))

exec(input())