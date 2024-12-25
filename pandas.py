def taxi_numbers(n):
    taxi_nums = []
    cubes = [i**3 for i in range(1, 100)]
    for i in range(len(cubes)):
        for j in range(i+1, len(cubes)):
            for k in range(j+1, len(cubes)):
                for l in range(k+1, len(cubes)):
                    if cubes[i] + cubes[j] == cubes[k] + cubes[l]:
                        taxi_nums.append(cubes[i] + cubes[j])
    taxi_nums.sort()
    return taxi_nums[:n]
print(taxi_numbers(5))
