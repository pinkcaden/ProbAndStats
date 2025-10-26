import math

def get_q1(sample):
    return sorted(sample)[math.floor(len(sample)/4)]

def get_q3(sample):
    return sorted(sample)[math.floor(3 * (len(sample) / 4))]

def get_iqr(sample):
    return get_q3(sample) - get_q1(sample)

def get_l_outlier(sample):
    return get_q1(sample) - (1.5 * get_iqr(sample))

def get_r_outlier(sample):
    return get_q3(sample) + (1.5 * get_iqr(sample))

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

def problem_seventeen():
    smokers = [69.3, 56.0, 22.1, 47.6,
               53.2, 48.1, 52.7, 34.4,
               60.2, 43.8, 23.2, 13.8]
    non_smokers = [28.6, 25.1, 26.4, 34.9,
                   29.8, 28.4, 38.5, 30.2,
                   30.6, 31.8, 41.6, 21.1,
                   36.0, 37.9, 13.9]
    print(sorted(smokers))
    print(sorted(non_smokers))
    print(f"Smoker Mean: {get_mean(smokers):.3f}")
    print(f"Non-smoker Mean: {get_mean(non_smokers):.3f}")

    print(f"Smoker Standard Deviation: {get_standard_deviation(smokers):.3f}")
    print(f"Non-smoker Standard Deviation: {get_standard_deviation(non_smokers):.3f}")

def problem_eighteen():
    grades = [23, 60, 79, 32, 57, 74, 52, 70, 82,
              36, 80, 77, 81, 95, 41, 65, 92, 85,
              55, 76, 52, 10, 64, 75, 78, 25, 80,
              98, 81, 67, 41, 71, 83, 54, 64, 72,
              88, 62, 74, 43, 60, 78, 89, 76, 84,
              48, 84, 90, 15, 79, 34, 67, 17, 82,
              69, 74, 63, 80, 85, 61]
    print(f"Grades Mean: {get_mean(grades):.3f}")
    print(f"Grades Median: {get_median(grades):.3f}")
    print(f"Grades Standard Deviation: {get_standard_deviation(grades):.3f}")

def problem_twentyfour():
    salaries = [3.79, 2.99, 2.77, 2.91, 3.10, 1.84, 2.52, 3.22,
                2.45, 2.14, 2.67, 2.52, 2.71, 2.75, 3.57, 3.85,
                3.36, 2.05, 2.89, 2.83, 3.13, 2.44, 2.10, 3.71,
                3.14, 3.54, 2.37, 2.68, 3.51, 3.37]
    print(f"Salary Mean: {get_mean(salaries):.3f}")
    print(f"Salary Standard Deviation: {get_standard_deviation(salaries):.3f}")

def problem_twentyeight():
    low_injection = [72.68, 72.62, 72.58, 72.48, 73.07,
                     72.55, 72.42, 72.84, 72.58, 72.92]
    high_injection = [71.62, 71.68, 71.74, 71.48, 71.55,
                      71.52, 71.71, 71.56, 71.70, 71.5]
    print(f"Low Injection Mean: {get_mean(low_injection):.3f}")
    print(f"High Injection Mean: {get_mean(high_injection):.3f}")

def problem_twentynine():
    grades = [23, 60, 79, 32, 57, 74, 52, 70, 82,
              36, 80, 77, 81, 95, 41, 65, 92, 85,
              55, 76, 52, 10, 64, 75, 78, 25, 80,
              98, 81, 67, 41, 71, 83, 54, 64, 72,
              88, 62, 74, 43, 60, 78, 89, 76, 84,
              48, 84, 90, 15, 79, 34, 67, 17, 82,
              69, 74, 63, 80, 85, 61]

    print(f"Q1: {get_q1(grades)}")
    print(f"Median: {get_median(grades):.3f}")
    print(f"Q3: {get_q3(grades)}")

    print(f"IQR: {get_iqr(grades)}")
    print(f"L Outlier: {get_l_outlier(grades)}")
    print(f"R Outlier: {get_r_outlier(grades)}")

def problem_thirtyone():
    low_velocity = [76.2, 76.09, 75.98, 76.15, 76.17,
                    75.94, 76.12, 76.18,76.25, 75.82]
    high_velocity = [93.25, 93.19, 92.87, 93.29, 93.37,
                     92.98, 93.47, 93.75, 93.89, 91.62]