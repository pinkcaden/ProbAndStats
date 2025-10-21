

import math

def get_range(sample):
    sorted_sample = sorted(sample)
    return sorted_sample[len(sample) - 1] - sorted_sample[0]

def get_median(sample):
    sorted_sample = sorted(sample)
    sample_size = len(sample)
    if sample_size % 2 == 0:
        return (sorted_sample[int((sample_size / 2) - 1)] + sorted_sample[int((sample_size / 2))]) / 2
    return sorted_sample[int((sample_size / 2) - 1)]


def get_mean(sample):
    run_total = 0
    for num in sample:
        run_total += num
    return run_total/len(sample)

def get_sample_variance(sample):
    mean = get_mean(sample)
    run_total = 0
    for num in sample:
        run_total += (num - mean) ** 2
    return run_total/(len(sample) - 1)

def get_standard_deviation(sample):
    return math.sqrt(get_sample_variance(sample))

def problem_eight():
    sample = [18.71, 21.41, 20.72, 21.81, 19.29,
              22.43, 20.17, 23.71, 19.44, 20.50,
              18.92, 20.33, 23.00, 22.85, 19.25,
              21.77, 22.11, 19.77, 18.04, 21.12]

    print(f"Sample Variance: {get_sample_variance(sample):.3f}")
    print(f"Standard Deviation: {get_standard_deviation(sample):.3f}")

def problem_nine():
    no_aging = [227, 222, 218, 217, 225, 218, 216, 229, 228, 221]
    aging = [219, 214, 215, 211, 209, 218, 203, 204, 201, 205]

    print(f"No aging sample variance: {get_sample_variance(no_aging):.3f}")
    print(f"No aging standard deviation: {get_standard_deviation(no_aging):.3f}")
    print(f"Aging sample variance: {get_sample_variance(aging):.3f}")
    print(f"Aging standard deviation: {get_standard_deviation(aging):.3f}")


def problem_fourteen():
    sample = [572, 572, 573, 568, 569, 575, 565, 570]

    print(get_median(sample))
    print(get_mean(sample))
    print(get_range(sample))
    print(f"Sample Variance: {get_sample_variance(sample):.3f}")
    print(f"Standard Deviation: {get_standard_deviation(sample):.3f}")

problem_nine()
problem_fourteen()

