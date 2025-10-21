

import math

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
    pass