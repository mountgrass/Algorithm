# python3

class JobThread:
    def __init__(self,id, end):
        self.id = id
        self.end = end
        
class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.threadHeap = []
        for i in range(0,self.num_workers):
            self.threadHeap.append( JobThread(i,0) )
        #print(self.threadHeap)
    
    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def ThreadSiftUp(self,i):
        parent = int(i/2)
        while i > 0 and self.threadHeap[parent].end > self.threadHeap[i].end:
            self.threadHeap[parent],self.threadHeap[i] = self.threadHeap[i], self.threadHeap[parent]
            i = parent
            
    def ThreadSiftDown(self,i):
        maxIndex = i
        l = 2*i+1
        n = self.num_workers
        if l < n:
            lEndEarlier = self.threadHeap[l].end < self.threadHeap[maxIndex].end
            liEndSameTime = self.threadHeap[l].end == self.threadHeap[maxIndex].end
            if lEndEarlier or (liEndSameTime and self.threadHeap[l].id < self.threadHeap[maxIndex].id):
                maxIndex = l
           
        r = 2*i+2
        if r < n:
            #print(self.threadHeap[r].id, self.threadHeap[r].end, self.threadHeap[maxIndex].id, self.threadHeap[maxIndex].end)
            rEndEarlier = self.threadHeap[r].end < self.threadHeap[maxIndex].end
            riEndSameTime = self.threadHeap[r].end == self.threadHeap[maxIndex].end
            if (rEndEarlier or (riEndSameTime and self.threadHeap[r].id < self.threadHeap[maxIndex].id) ):
                maxIndex = r
        #print('maxIndex:{0}'.format(self.threadHeap[maxIndex].id))
        
        if i!=maxIndex:
           self.threadHeap[maxIndex],self.threadHeap[i] = self.threadHeap[i], self.threadHeap[maxIndex]
           self.ThreadSiftDown(maxIndex)

    def ChangePriority(self,i, p):
        oldP = self.threadHeap[i].end
        self.threadHeap[i].end = p
        if p < oldP:
            self.ThreadSiftUp(i)
        else:
            #print("SiftDown {0}".format(self.threadHeap[i].id))
            self.ThreadSiftDown(i)


    def assign_jobs_faster(self):
        n = self.num_workers
        m = len(self.jobs)
        #print(n,m)
        self.assigned_workers = [None] * m
        self.start_times = [None] * m

        jobQueue = []
        for i in range(0, m):
            jobQueue.append(i)

        while len(jobQueue) > 0:

            jobId = jobQueue[0]
            del jobQueue[0]
            job_time = self.jobs[jobId]
            #print(jobId, job_time)
            
            self.assigned_workers[jobId] = self.threadHeap[0].id
            self.start_times[jobId] = self.threadHeap[0].end
            self.ChangePriority(0, self.start_times[jobId] + job_time )           
        
        
    def solve(self):
        self.read_data()
        self.assign_jobs_faster()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

