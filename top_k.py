import heapq
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)

    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [item[1] for item in heap]