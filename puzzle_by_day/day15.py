# Lin Wouters
# 14-12-2022

import numpy as np
import regex as re
from tqdm import tqdm
from collections import defaultdict

def do_stuff(filepath, row=10, boundaries = [0,20]):

    all_positions = []
    beacons = []
    no_signal = []
    with open(filepath) as f:
        # print(len(f.split('\n')))
        for line in tqdm(f):
            # Get the positions of the sensor and beacon
            positions = re.findall(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)[0]
            S_x, S_y, B_x, B_y = int(positions[0]), int(positions[1]), int(positions[2]), int(positions[3])
            # Add sensor and beacon to places where there is no signal
            beacons.append((int(positions[0]), int(positions[1])))
            beacons.append((int(positions[2]), int(positions[3])))
            # Calculate distance
            dist = abs(S_x - B_x) + abs(S_y - B_y)

            # Add positions where there is no signal
            for i in range(-dist, dist+1):
                if row >= S_y + (-dist + abs(i)) and row <= S_y + (dist - abs(i)):
                    no_signal.append((S_x + i, row))

    num_no_beacons = sum([1 for pos in set(no_signal)- set(beacons) if pos[1]==row])

    return num_no_beacons


def do_stuff2(filepath, row=10, boundaries = [0,20]):

    all_positions = []
    beacons = []
    no_signal = []
    keep_track = defaultdict(lambda:[])
    beacons_dict = defaultdict(lambda:[])

    with open(filepath) as f:
        # print(len(f.split('\n')))
        for line in tqdm(f):
            # Get the positions of the sensor and beacon
            positions = re.findall(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)[0]
            S_x, S_y, B_x, B_y = int(positions[0]), int(positions[1]), int(positions[2]), int(positions[3])
            # Add sensor and beacon to places where there is no signal
            beacons.append((int(positions[0]), int(positions[1])))
            beacons.append((int(positions[2]), int(positions[3])))

            # beacons_dict[int(positions[1])] += [int(positions[0])]
            # beacons_dict[int(positions[3])] += [int(positions[2])]

            # Calculate distance
            dist = abs(S_x - B_x) + abs(S_y - B_y)

            # Add positions where there is no signal
            for i_y in range(-dist, dist+1):
                keep_track[S_y + i_y].append([S_x + (-dist + abs(i_y)), S_x + (dist - abs(i_y))])

    # Iterate over the rows
    for i_y in tqdm(list(keep_track)):
        # Sort the intervals based on start
        keep_track[i_y].sort()
        # posi = []
        # for track in keep_track[i_y]:
        #     posi += range(track[0], track[1])
        # print(i_y)
        # print(i_y, sorted(set(posi)))

        # prin.t(i, keep_track[i])
        if i_y < boundaries[0] or i_y > boundaries[1]:
            continue

        # Update max interval
        max_interval = boundaries[0]
        for j in range(1, len(keep_track[i_y])):
            max_interval = max(max_interval, keep_track[i_y][j-1][1])
            if max_interval < keep_track[i_y][j][0]-1:
                # return [i_y, keep_track[i_y][j-1][1]+1]
                return (keep_track[i_y][j-1][1]+1)*4000000 + i_y

        if keep_track[i_y][-1][1] < boundaries[1]:
            # return [i_y, keep_track[i_y][j-1][1]+1]
            return (keep_track[i_y][j-1][1]+1)*4000000 + i_y

    print(keep_track[1])

    return True


if __name__ == "__main__":
    filepath="data/test_day15.txt"
    print(f"Number of positions the beacon cant be at row 10: {do_stuff2(filepath, row=10, boundaries=[0,20])}")
    filepath="data/day15.txt"
    print(f"Number of positions the beacon cant be at row 2000000: {do_stuff2(filepath, row=2000000, boundaries=[0,4000000])}")