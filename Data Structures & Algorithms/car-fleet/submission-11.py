class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            zip(position, speed), reverse=True
        )  # Sorts by position descending

        fleets = 0
        current_max_time = 0.0

        # 2. Iterate through cars from closest to furthest
        for pos, spd in cars:
            time_to_target = (target - pos) / spd

            # If a car takes MORE time than the fleet leader ahead of it,
            # it cannot catch up. It becomes the leader of a new fleet.
            if time_to_target > current_max_time:
                fleets += 1
                current_max_time = time_to_target  # Update the bottleneck time

        return fleets