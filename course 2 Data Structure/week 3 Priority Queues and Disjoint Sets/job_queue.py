# python3

class HeapThread(object):
    def __init__(self,n):
        self.n = n
        self.free_time = [0]*n
        self.corr_index = list(range(n))
        
    def add_to_free_time(self,process_time):
        self.free_time[0] += process_time
        self.shift_down(0)
    
    def shift_down(self,i):
        min_index = i
        
        left_child_i = 2*i+1
        if left_child_i<self.n:
            if self.free_time[left_child_i]<self.free_time[min_index]:
                min_index = left_child_i
            elif self.free_time[left_child_i]==self.free_time[min_index] and self.corr_index[left_child_i]<self.corr_index[min_index]:
                min_index = left_child_i
                
        right_child_i = 2*i+2
        if right_child_i<self.n:
            if self.free_time[right_child_i]<self.free_time[min_index]:
                min_index = right_child_i
            elif self.free_time[right_child_i]==self.free_time[min_index] and self.corr_index[right_child_i]<self.corr_index[min_index]:
                min_index = right_child_i

        if i != min_index:
            self.free_time[i],self.free_time[min_index] = self.free_time[min_index],self.free_time[i]
            self.corr_index[i],self.corr_index[min_index] = self.corr_index[min_index],self.corr_index[i]
            self.shift_down_free_time(min_index)

class JobQueue(object):
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        assign_heap = HeapThread(self.num_workers)
        
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = assign_heap.corr_index[0]
            self.start_times[i] = assign_heap.free_time[0]
            assign_heap.add_to_free_time(self.jobs[i])

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

