def main():
    t_s = float(input())
    t_c = float(input())
    t_r = float(input())

    total_time = t_s + t_c + t_r

    if total_time > 4:
        return "Time"

    v_s = 1.5/t_s

    if v_s < 2:
        return "Swimming"

    v_c = 40/t_c

    if v_c < 20:
        return "Cycling"

    v_r = 10/t_r

    if v_r < 8:
        return "Running"

    return total_time


print(main())