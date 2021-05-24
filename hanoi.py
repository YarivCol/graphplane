import sys
import itertools


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    domain_file.write("Propositions: \n")
    for idx_disk, disk in enumerate(disks):
        domain_file.write("u_" + disk + " ")
        for peg in pegs:
            domain_file.write(disk + "_" + peg + " ")
        idx_disk += 1
        while idx_disk < n_:
            domain_file.write(disk + "_" + disks[idx_disk] + " ")
            idx_disk += 1
    for peg in pegs:
        domain_file.write("u_" + peg + " ")
    domain_file.write("\nActions: \n")
    for idx_disk,disk in enumerate(disks):
        idx_disk += 1
        for idx_peg, peg in enumerate(pegs):
            for j in range(len(disks) - idx_disk):
                domain_file.write("Name: M" + disk + "_" + disks[idx_disk + j] + "_" + peg + "\n"
                                "pre: " + "u_" + peg + " " + "u_" + disk +" " + disk + "_" + disks[idx_disk + j] + "\n"
                                "add: " + disk + "_" + peg + " u_" + disks[idx_disk + j] + "\n"
                                "delete: " + "u_" + peg + " " + disk + "_" + disks[idx_disk + j] + "\n")
                domain_file.write("Name: M" + disk + "_" + peg + "_" + disks[idx_disk + j] + "\n"
                                "pre: " + "u_" + disks[idx_disk + j] + " " + "u_" + disk + " " + disk + "_" + peg + "\n"
                                "add: " + disk + "_" + disks[idx_disk + j] + " u_" + peg + "\n"
                                "delete: " + "u_" + disks[idx_disk + j] + " " + disk + "_" + peg + "\n")
            for j in range(len(pegs)):
                if idx_peg != j:
                    domain_file.write("Name: M" + disk + "_" + peg + "_" + pegs[j] + "\n"
                                    "pre: " + "u_" + disk + " " + "u_" + pegs[j] + " " + disk + "_" + peg + "\n"
                                    "add: " + disk + "_" + pegs[j] + " u_" + peg + "\n"
                                    "delete: " + "u_" + pegs[j] + " " + disk + "_" + peg + "\n")
            for disk1, disk2 in list(itertools.combinations(range(idx_disk, n_),2)):
                    domain_file.write("Name: M" + disk + "_" + disks[disk1] + "_" + disks[disk2] + "\n"
                                    "pre: " + "u_" + disk + " " + "u_" + disks[disk2] + " " + disk + "_" + disks[disk1] + "\n"
                                    "add: " + disk + "_" + disks[disk2] + " " + "u_" + disks[disk1] + "\n"
                                    "delete: " + "u_" + disks[disk2] + " " + disk + "_" + disks[disk1] + "\n")
                    domain_file.write("Name: M" + disk + "_" + disks[disk2] + "_" + disks[disk1] + "\n"
                                    "pre: " + "u_" + disk + " " + "u_" + disks[disk1] + " " + disk + "_" + disks[disk2] + "\n"
                                    "add: " + disk + "_" + disks[disk1] + " " + "u_" + disks[disk2] + "\n"
                                    "delete: " + "u_" + disks[disk1] + " " + disk + "_" + disks[disk2] + "\n")
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    problem_file.write("Initial state: u_" + disks[0] + " ")
    for i in range(len(disks) -1 ):
        problem_file.write(disks[i] + "_" + disks[i + 1] + " ")
    for i in range(len(pegs) -1 ):
        problem_file.write("u_" + pegs[i + 1] + " ")
    problem_file.write(disks[n_ -1] + "_" + pegs[0] + "\n")
    problem_file.write("Goal state: u_" + disks[0] + " ")
    for i in range(len(disks) -1 ):
        problem_file.write(disks[i] + "_" + disks[i + 1] + " ")
    for i in range(len(pegs) -1 ):
        problem_file.write("u_" + pegs[i] + " ")
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



# while idx_disk < n_:
#             for j in range(len(disks) - idx_disk):
#                 if idx_disk != j:
#                     domain_file.write("Name: M" + disk + "_" + disks[idx_disk + j] + "_" + disks[idx_disk] + "\n"
#                                     "pre: " + "u_" + disk + " " + "u_" + disks[idx_disk] + " " + disk + "_" + disks[idx_disk + j] + "\n"
#                                     "add: " + disk + "_" + disks[idx_disk] + " " + "u_" + disks[idx_disk + j] + "\n"
#                                     "delete: " + "u_" + disks[idx_disk] + " " + disk + "_" + disks[idx_disk + j] + "\n")
#             idx_disk += 1