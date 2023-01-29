def negative_positive(numbers):
    positive = [n for n in numbers if n >= 0]
    negative = [n for n in numbers if n < 0]
    print(sum(negative))
    print(sum(positive))
    if sum(positive) > abs(sum(negative)):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


my_numbers = [int(x) for x in input().split()]
print(negative_positive(my_numbers))