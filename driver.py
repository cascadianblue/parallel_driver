import subprocess
import csv


PROBLEM_SIZES = (102400000, 204800000, 409600000)
NUM_THREADS = (2, 4, 8, 16)


output_file = open('output.csv', 'w')
output = csv.writer(output_file)
output.writerow(['']+[str(i) for i in PROBLEM_SIZES])


for num_threads in NUM_THREADS:
    row = [str(num_threads)]
    for problem_size in PROBLEM_SIZES:
        result = subprocess.run(['mpirun', '-np', str(num_threads), '--map-by', 'node', 'mergeSortMPI', str(problem_size)], stdout=subprocess.PIPE)
        print("Finished problem size: %s threads: %s" % (problem_size, num_threads))
        row += [result.stdout.decode('utf-8').strip()]
    output.writerow(row)

output_file.close()
