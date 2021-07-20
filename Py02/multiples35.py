def sum_multiples(n):
    multiples_of_five = n // 5
    multiples_of_three = n // 3
    multiples_of_both = n // 15
    
    sum_mof = multiples_of_five*(multiples_of_five+1)*5//2
    sum_mot = multiples_of_three*(multiples_of_three+1)*3//2
    sum_mob = multiples_of_both*(multiples_of_both+1)*15//2
    
    return sum_mof + sum_mot - sum_mob