# Write a function that takes in a ist of numbers and returns a dictionary containing the following statistics about the numbers: the mean,
# median, mode, sample variance, sample standard deviation, and 95% confidence interval for the mean.
# Note that
# You can assume that the given list contains a large-enough number of samples from a population to use a z-score of 1.96.
# Ifthere's more than one mode, your function can return any of them.
# You shouldn't use any libraries.
# Your output values will automatically be rounded to the fourth decimal.
# Sample Input
# input_list = [2, 1, 3, 4, 4, 5, 6, 71
# Sample Output
# {
# "mean" : 4.0,
# median" : 4.0,
# "mode": 4.0,
# "sample_variance": 4.0,
# "sample_standard _deviation": 2.0,
# "mean_confidence_ interval" : [2.6141, 5.3859],
# }

def get_statistics(input_list):
    sorted_input = sorted(input_list)
    input_length = len(input_list)

    mean = sum(sorted_input) / input_length

    middle_idx = (len(sorted_input) -1) // 2 # -1 to match index 
    median = sorted_input[middle_idx]

    if input_length % 2 == 0:
        middle_number_1 = sorted_input[middle_idx]
        middle_number_2 = sorted_input[middle_idx + 1]
        median = (middle_number_1 + middle_number_2) / 2

    number_counts = {x: sorted_input.count(x) for x in set(sorted_input)} # we have used set so we only have unique key and value
    mode = max(number_counts.keys(), key=lambda unique_number: number_counts[unique_number]) 
    # here key variable work as a filter to give max number of counts amoung all key 
    # takes number_counts.keys() and put it in lambda like: MAX(number_counts[x] = total_countsof_x) 

    sample_variance = sum([(number - mean) ** 2 / (input_length - 1) for number in sorted_input])

    sample_standard_deviation = sample_variance ** 0.5

    mean_standard_error = sample_standard_deviation / input_length ** 0.5
    z_score_standard_error = 1.96 * mean_standard_error # z-score for 95% is 1.96 from z-score table
    mean_confidence_interval = [mean - z_score_standard_error, mean + z_score_standard_error]
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }


