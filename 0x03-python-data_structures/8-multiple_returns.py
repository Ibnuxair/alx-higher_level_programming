#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence_len == 0:
        return
    else:
        return (sentence_len, sentence[0])
