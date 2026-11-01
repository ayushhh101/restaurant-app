import hashlib
import math


class BloomFilter:
    def __init__(self, expected_elements: int, false_positive_rate: float):
        if expected_elements <= 0:
            raise ValueError("expected_elements must be positive")
        if not 0 < false_positive_rate < 1:
            raise ValueError("false_positive_rate must be between 0 and 1")
        self.n = expected_elements
        self.p = false_positive_rate
        self.m = math.ceil(-(self.n * math.log(self.p)) / (math.log(2) ** 2))
        self.k = max(1, round((self.m / self.n) * math.log(2)))
        self.bit_array = [0] * self.m

    def _hashes(self, item: str):
        for i in range(self.k):
            digest = hashlib.sha256(f"{i}:{item}".encode("utf-8")).digest()
            yield int.from_bytes(digest, "big") % self.m

    def add(self, item: str):
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def contains(self, item: str) -> bool:
        return all(self.bit_array[index] == 1 for index in self._hashes(item))


class Bucket:
    def __init__(self, size: int, timestamp: int):
        self.size = size
        self.timestamp = timestamp

    def __repr__(self):
        return f"Bucket(size={self.size}, ts={self.timestamp})"


class DGIM:
    def __init__(self, window_size: int):
        if window_size <= 0:
            raise ValueError("window_size must be positive")
        self.N = window_size
        self.timestamp = 0
        self.buckets = []  # newest first

    def update(self, bit: int):
        if bit not in (0, 1):
            raise ValueError("Stream values must be 0 or 1")
        self.timestamp += 1

        # Remove buckets whose newest represented timestamp is outside window N.
        self.buckets = [
            bucket for bucket in self.buckets
            if self.timestamp - bucket.timestamp < self.N
        ]

        if bit == 1:
            self.buckets.insert(0, Bucket(1, self.timestamp))
            self._merge_buckets()

    def _merge_buckets(self):
        # Buckets are newest first. If 3 of a size exist, merge the two oldest.
        i = 0
        while i < len(self.buckets):
            same_size = [j for j in range(i, len(self.buckets))
                         if self.buckets[j].size == self.buckets[i].size]
            if len(same_size) > 2:
                second_oldest = same_size[-2]
                oldest = same_size[-1]
                merged = Bucket(
                    self.buckets[second_oldest].size * 2,
                    self.buckets[second_oldest].timestamp
                )
                self.buckets[second_oldest] = merged
                self.buckets.pop(oldest)
                i = 0  # merging may cause a higher-size merge
            else:
                i += 1

    def count_ones(self, k: int) -> int:
        if k <= 0:
            return 0
        k = min(k, self.N, self.timestamp)
        if k == 0:
            return 0

        boundary = self.timestamp - k
        # Keep buckets whose newest timestamp lies in the query window.
        included = [b for b in self.buckets if b.timestamp > boundary]
        if not included:
            return 0
        # Standard DGIM estimate: count all newer buckets fully and half
        # of the oldest bucket that intersects the query boundary.
        return sum(b.size for b in included[:-1]) + included[-1].size // 2


if __name__ == "__main__":
    print("\nPART 1: BLOOM FILTER — MALICIOUS URL DETECTOR")
    bloom = BloomFilter(expected_elements=100, false_positive_rate=0.01)
    print(f"Optimal bit array size (m): {bloom.m} bits")
    print(f"Number of hash functions (k): {bloom.k}")

    blacklist_urls = [
        "http://malware-site.com",
        "http://phishing-login.org",
        "http://bad-actor.net",
        "http://crypto-scam.io",
    ]
    for url in blacklist_urls:
        bloom.add(url)
    print(f"Added {len(blacklist_urls)} malicious URLs.")

    test_urls = [
        "http://malware-site.com",
        "http://google.com",
        "http://phishing-login.org",
        "http://wikipedia.org",
    ]
    for url in test_urls:
        status = "POSSIBLY MALICIOUS" if bloom.contains(url) else "DEFINITELY NOT IN FILTER"
        print(f"{url:<32} -> {status}")

    print("\nPART 2: DGIM — THREAT STREAM MONITOR")
    window_size = 20
    stream = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1,
              1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
    dgim = DGIM(window_size)
    for bit in stream:
        dgim.update(bit)

    print("Input stream:", stream)
    print("Active buckets (newest to oldest):")
    for bucket in dgim.buckets:
        print(" ", bucket)

    actual = sum(stream[-window_size:])
    estimated = dgim.count_ones(window_size)
    print("Actual number of 1s in last 20 bits:", actual)
    print("DGIM estimated number of 1s:", estimated)
    print("Absolute estimation error:", abs(actual - estimated))
