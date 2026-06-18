g = ("arithmetic progression")
print(g)
nth_term = lambda a, d, n: a + (n - 1) * d
sum_of_terms = lambda a, d, n: (n/2) * (2 * a + (n - 1) * d)

# Ab input ki baari hai
a = int(input("Enter (a)"))
d = int(input("Enter (d)"))
n = int(input("Enter (n)"))

print("\n Aapki Series")

for i in range(1, n + 1):
    term = nth_term(a, d, i) 
    print(term, end="  ")

print("\n\n------- Here are the results------")
print(f"{n}th term is: {nth_term(a, d, n)}") 
print(f"Total sum is: {sum_of_terms(a, d, n)}") 

