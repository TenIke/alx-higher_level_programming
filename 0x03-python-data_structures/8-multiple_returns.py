#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != "":
        sen_len = len(sentence)
        tuple1 = (sen_len,)
        tuple2 = tuple1 + (sentence[0],)
        return tuple2
    else:
        return (0, None)
