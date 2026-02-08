import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.maxheap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.maxheap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.tasks[taskId]
        self.tasks[taskId] = (userId, newPriority)
        heapq.heappush(self.maxheap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.maxheap:
            neg_p, neg_t = heapq.heappop(self.maxheap)
            priority, taskId = -neg_p, -neg_t
            cur = self.tasks.get(taskId)
            if cur is None:
                continue
            userId, cur_priority = cur
            if cur_priority != priority:
                continue
            del self.tasks[taskId]
            return userId
        return -1

