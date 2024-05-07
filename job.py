import heapq

class JobScheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, job, priority):
        heapq.heappush(self.jobs, (priority, job))

    def get_next_job(self):
        if self.jobs:
            priority, job = heapq.heappop(self.jobs)
            return job
        else:
            return None

if __name__ == "__main__":
    scheduler = JobScheduler()
    
    # Adding jobs with their priorities
    scheduler.add_job("Job 1", 3)
    scheduler.add_job("Job 2", 1)
    scheduler.add_job("Job 3", 2)
    
    # Getting the next job to be executed
    next_job = scheduler.get_next_job()
    while next_job:
        print("Executing:", next_job)
        next_job = scheduler.get_next_job()