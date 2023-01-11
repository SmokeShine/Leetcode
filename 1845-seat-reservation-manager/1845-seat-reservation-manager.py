class SeatManager:

    def __init__(self, n: int):
        seats_=[x for x in range(1,n+1)]
        heapq.heapify(seats_)
        self.seats_=seats_
        

    def reserve(self) -> int:
        if self.seats_:
            return heapq.heappop(self.seats_)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats_,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)