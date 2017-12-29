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
        self.finish_time_ = []

    def Process(self, request):
        #print(self.finish_time_)
        # write your code here
        if len(self.finish_time_)==0:
            self.finish_time_.append(request.arrival_time+request.process_time)
            #print('1 - Append {0}'.format(request.arrival_time+request.process_time))
            return Response(False, request.arrival_time)
        
        finish_time = self.finish_time_[0]
        while finish_time <= request.arrival_time:
            self.finish_time_.pop(0)
            if len(self.finish_time_) == 0:
                break
            finish_time = self.finish_time_[0]

        #print('after check {0}'.format(self.finish_time_) )
        if len(self.finish_time_)==0: #if all tasks have finished before arrival
            self.finish_time_.append(request.arrival_time+request.process_time)
            #print('2-Append {0}'.format(request.arrival_time+request.process_time))
            return Response(False, request.arrival_time)
        elif len(self.finish_time_) < self.size:
            #if there is still task but the request can fit into buffer
            #have to wait for last task in queue to finish
            finish_time = self.finish_time_[-1]
            self.finish_time_.append(finish_time+request.process_time)
            #print('3-Append {0}'.format(finish_time+request.process_time))
            return Response(False, finish_time)
            
        return Response(True, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
