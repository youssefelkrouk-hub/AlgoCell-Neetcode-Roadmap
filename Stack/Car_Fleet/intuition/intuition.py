class Solution(object):
    def carFleet(self, target, position, speed):
        # Pair each car's position with its speed, sorted by position
        # so we process cars from closest to target to farthest.
        cars = sorted(zip(position, speed), reverse=True)

        fleets = []  # stack of arrival times, one per fleet
        for pos, spd in cars:
            time_to_target = (target - pos) / spd

            # If this car reaches the target no later than the fleet
            # ahead of it, it merges into that fleet (doesn't add a new one).
            if not fleets or time_to_target > fleets[-1]:
                fleets.append(time_to_target)

        return len(fleets)

