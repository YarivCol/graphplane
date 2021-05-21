import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    domain_file.write("Propositions: \n")
    for i,d in enumerate(disks):
        domain_file.write("u_" + d + " ")
        for p in pegs:
            domain_file.write(d + "_" + p + " ")
        i += 1
        while i < n_:
            domain_file.write(d + "_" + disks[i] + " ")
            i += 1
    for p in pegs:
        domain_file.write("u_" + p + " ")
    domain_file.write("\nActions: \n")
    for i,d in enumerate(disks):
        for p in pegs:
            domain_file.write("Name: M" + d + "_" + p + "\n"
                              "pre: " + "u_" + p + " " + "u_" + d + "\n"
                              "add: " + d + "_" + p + "\n"
                              "delete: " + "u_" + p + "\n") 
        i += 1
        while i < n_:
            domain_file.write("Name: M" + d + "_" + disks[i] + "\n"
                              "pre: " + "u_" + d + " " + "u_" + disks[i] + "\n"
                              "add: " + d + "_" + disks[i] + "\n"
                              "delete: " + "u_" + disks[i] + "\n")
            i += 1
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    problem_file.write("Initial state: u_" + disks[0] + " ")
    for i in range(len(disks) -1 ):
        problem_file.write(disks[i] + "_" + disks[i + 1] + " ")
    problem_file.write(disks[n_ -1] + "_" + pegs[0] + "\n")
    problem_file.write("Goal state: u_" + disks[0] + " ")
    for i in range(len(disks) -1 ):
        problem_file.write(disks[i] + "_" + disks[i + 1] + " ")
    problem_file.write(disks[n_ -1] + "_" + pegs[m_ -1] + "\n")
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
