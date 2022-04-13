import itertools

def fcfs(processes, bursts, arrivals=None) :

    burst_time = []
    wait_time = []
    turn_time = []

    burst_time = bursts # 실행시간 입력

    end_time = [0 for i in range(len(processes))] # 각 프로세스가 끝나는 시간 계산
    

    end_time = list(itertools.accumulate(bursts))
    print(end_time)

    # 대기시간 Wait_time = (i-1) end_time - arrivals
    wait_time = [0 for i in range(len(processes))]
    for i in range(1, len(processes)):
        wait_time[i] = end_time[i-1] - arrivals[i]

    #변환시간 turn_time = end_time - arrivals
    turn_time = [0 for i in range(len(processes))]
    for i in range(0, len(processes)):
        turn_time[i]  = end_time[i] - arrivals[i]

    return burst_time, wait_time, turn_time

# process id
processes = [1, 2, 3, 4, 5, 6]
# Burst time of all processes
burst_time = [5, 9, 6, 15, 6, 3]
# Arrival time of all processes
arrival_time = [0, 3, 6, 7, 8, 10]

p = processes.copy()
n = len(processes)

b, w, t = fcfs(processes, burst_time, arrival_time)
print("process ID                 :", p)
print("Burst_time                 :", b)
print("Waiting_time               :", w)
print("Turn_Around_time           :", t)
print("평균 waiting 시간           :", sum(w)/n)
print("평균 turn around 시간       :", sum(t)/n)
