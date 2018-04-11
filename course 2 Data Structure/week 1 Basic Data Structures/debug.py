# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 00:54:07 2018

@author: CX
"""

# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        '''
        Check if the requests in the buffer are finished when new request arrive
        If so, pop them
        '''
        finish_num = 0
        for finish in self.finish_time:
            if finish<=request.arrival_time:
                finish_num += 1
            else:
                break
        for i in range(finish_num):
            self.finish_time.pop(0)
        '''
        Check if 3 conditions: buffer is empty;buffer is full;buffer is not full
        '''
        if len(self.finish_time)==self.size:
            return Response(True, -1)
        elif self.finish_time == []:
            start_time = request.arrival_time
            self.finish_time.append(start_time + request.process_time)
            return Response(False, start_time)
        else:
            start_time = self.finish_time[-1]
            self.finish_time.append(start_time + request.process_time)
            return Response(False, start_time)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)



size, count = (2,3)
request1 = Request(0,2)
request2 = Request(1,4)
request3 = Request(5,3)

requests = [request1,request2,request3]

buffer = Buffer(size)
responses = ProcessRequests(requests, buffer)

PrintResponses(responses)
