import random

def read_from_text(file_name, operation):
    with open(file_name, operation) as fr:
        data = fr.read().splitlines()

        n, target = map(int, data[0].split())

        data = data[1:]

        name, avg_run = [], []

        for i in data:
            name.append(i.split()[0])
            avg_run.append(i.split()[1])

        avg_run = [ int(avg_run[i]) for i in range(len(avg_run)) ]

        return n, target, name, avg_run

def create_dictionary(total_batsman, avg_runs):
    my_dict = {}
    for i in range(total_batsman):
        my_dict[i] = avg_runs[i]

    return my_dict

def generate_population(population_number, total_batsman):
    all_population = []
    for _ in range(population_number):
        all_population.append([random.randint(0,1) for _ in range(total_batsman)])

    return all_population

def fitness_function(generated_array, run_dict, target):
    sum = 0
    for i, j in enumerate(generated_array):
        if  j == 1:
            sum += run_dict[i]

    return sum

def rank_population(all_population, run_dict, target):
    temp = {}
    for i in all_population:
        score = fitness_function(i, run_dict, target)
        temp[score] = i

    ranked_population_list = []
    ranked_population = {k: v for k,v in sorted(temp.items())}

    for i, j in ranked_population.items():
        ranked_population_list.append(j)

    return ranked_population_list

def cross_over(first, second):
    point = random.randint(1, len(first)-1)
    child1 = first[0:point] + second[point:]
    child2 = second[0:point] + first[point:]

    return child1, child2, point

def mutate(child1, child2):
    point = random.randint(0, len(child1)-1)

    if child1[point] == 0:
        child1[point] = 1
    else:
        child1[point] = 0
    
    if child2[point] == 0:
        child2[point] = 1
    else:
        child2[point] = 0

    return child1, child2, point

total_batsman, target, name, avg_run = read_from_text('input1.txt','r')
run_dict = create_dictionary(total_batsman, avg_run)
population = generate_population(10, total_batsman)
ranked_list = rank_population(population, run_dict, target)

# new_list = []
# p1, p2 = random.sample(ranked_list, 2)
# print(p1, p2)
# c1, c2, cp = cross_over(p1, p2)
# print(c1,c2,cp)
# nc1, nc2, cp2 = mutate(c1, c2)
# new_list.append(nc1, nc2)

gen_count = 1
found = False
while not found:

    print("====================================================")
    print(f"Generation # {gen_count}")
    print(f"Target: {target}")
    print("====================================================")
    i = 0
    for j in ranked_list:
        print(f"Chromosome #{i}: {j} | Difference: {fitness_function(j, run_dict, target)}")
        i += 1
    print("====================================================")

    for i in ranked_list:
        ff_r = fitness_function(i, run_dict, target)

        if ff_r == target:
            found = True
            print(f"{name}\n{i}")
            break

    new_gen = []

    for i in range(5):
        p1, p2 = random.sample(ranked_list[:5],2)
        # print(f"Selected Parent: {p1} and {p2}")
        c1, c2, cp = cross_over(p1, p2)
        # print(f"Child Produced: {c1} and {c2} and cross-over at {cp}")
        nc1, nc2, mp = mutate(c1, c2)
        # print(f"Mutation: {nc1} and {nc2}")
        new_gen.append(nc1)
        new_gen.append(nc2)

    ranked_list = rank_population(new_gen, run_dict, target)

    gen_count += 1
    
    if gen_count == 10000:
        print(f"{name}\n-1")
        break