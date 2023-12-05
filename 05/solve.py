from typing import Dict, List

from rich import print


def read_txt_file(filename: str) -> List[str]:
    with open(f"./{filename}.txt", "r") as f:
        lines = f.readlines()

    return lines


def create_traversal_structure(data: List[str]) -> List[Dict[str, int]]:
    map_ = []

    for dsr in data:
        dest_range_start, source_range_start, range_length = dsr.split()
        map_.append(
            {
                "source": int(source_range_start),
                "destination": int(dest_range_start),
                "range": int(range_length),
            }
        )

    return map_


def get_seeds_stage_1():
    seeds_raw = read_txt_file("seeds")[0]
    return [int(s) for s in seeds_raw.split(":")[1].split()]


def get_seeds_stage_2():
    seeds_raw = read_txt_file("seeds")[0]
    seeds_ = [int(s) for s in seeds_raw.split(":")[1].split()]

    all_ranges_sum = 0
    for seed_start_ix in range(0, len(seeds_), 2):
        all_ranges_sum += seeds_[seed_start_ix + 1]

    for seed_start_ix in range(0, len(seeds_), 2):
        print("SEED IX: ", seed_start_ix)
        seed_st = seeds_[seed_start_ix]
        seed_rng = seeds_[seed_start_ix + 1]
        for r in range(seed_rng):
            prg = r / seed_rng
            ttl_prg = r / all_ranges_sum
            s = seed_st + r
            print(
                f"SEED PROGRESS: {prg * 100:6f} TOTAL PROGRESS: {ttl_prg * 100:6f}% @ SEED: {s}",
                end="\r",
            )
            yield s


def get_seed_to_soil():
    return create_traversal_structure(read_txt_file("seed_to_soil")[1:])


def get_soil_to_fertilizer():
    return create_traversal_structure(read_txt_file("soil_to_fertilizer")[1:])


def get_fertilizer_to_water():
    return create_traversal_structure(read_txt_file("fertilizer_to_water")[1:])


def get_water_to_light():
    return create_traversal_structure(read_txt_file("water_to_light")[1:])


def get_light_to_temp():
    return create_traversal_structure(read_txt_file("light_to_temp")[1:])


def get_temp_to_humidity():
    return create_traversal_structure(read_txt_file("temp_to_humidity")[1:])


def get_humidity_to_location():
    return create_traversal_structure(read_txt_file("humidity_to_location")[1:])


def find_(item: int, map_: List[Dict[str, int]]) -> int:
    sorted_map = map_

    for m_ in sorted_map:
        if item >= m_["source"]:
            if item < (m_["source"] + m_["range"]):
                return m_["destination"] + (item - m_["source"])
            else:
                return item

    raise ValueError("Could not find mapped destination value.")


def main() -> None:
    # seeds = get_seeds_stage_1()
    seeds = get_seeds_stage_2()

    seed_to_soil = get_seed_to_soil()
    soil_to_fertilizer = get_soil_to_fertilizer()
    fertilizer_to_water = get_fertilizer_to_water()
    water_to_light = get_water_to_light()
    light_to_temp = get_light_to_temp()
    temp_to_humidity = get_temp_to_humidity()
    humidity_to_location = get_humidity_to_location()

    sorted_seed_to_soil = sorted(seed_to_soil, key=lambda x: x["source"], reverse=True)
    sorted_soil_to_fertilizer = sorted(
        soil_to_fertilizer, key=lambda x: x["source"], reverse=True
    )
    sorted_fertilizer_to_water = sorted(
        fertilizer_to_water, key=lambda x: x["source"], reverse=True
    )
    sorted_water_to_light = sorted(
        water_to_light, key=lambda x: x["source"], reverse=True
    )
    sorted_light_to_temp = sorted(
        light_to_temp, key=lambda x: x["source"], reverse=True
    )
    sorted_temp_to_humidity = sorted(
        temp_to_humidity, key=lambda x: x["source"], reverse=True
    )
    sorted_humidity_to_location = sorted(
        humidity_to_location, key=lambda x: x["source"], reverse=True
    )

    min_location = float("inf")

    for seed in seeds:
        soil = find_(seed, sorted_seed_to_soil)
        fertilizer = find_(soil, sorted_soil_to_fertilizer)
        water = find_(fertilizer, sorted_fertilizer_to_water)
        light = find_(water, sorted_water_to_light)
        temp = find_(light, sorted_light_to_temp)
        humidity = find_(temp, sorted_temp_to_humidity)
        location = find_(humidity, sorted_humidity_to_location)

        if location < min_location:
            min_location = location

    print("STAGE 1: ", min_location)


if __name__ == "__main__":
    main()
