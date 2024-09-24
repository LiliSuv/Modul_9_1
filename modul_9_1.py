def apply_all_func(funct, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function (funct)
    return results

print (apply_all_func ([6, 20, 15, 9], max, min))
print (apply_all_func ([6, 20, 15, 9], len, sum, sorted))
