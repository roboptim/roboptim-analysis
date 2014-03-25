#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import re
import os
import argparse
import yaml
import fnmatch
from datetime import datetime


def generate_benchmark_yaml(filenames, output_dir):
    """
    Generate a YAML file containing optimization timings.
    """
    benchmark = list()

    # Fill benchmark dictionary
    for name in filenames:
        file = open(name, "r").read()

        # Get solver used
        solver_match = re.search(r'Plugin: ([\w-]+)', file)
        if solver_match:
            solver = solver_match.group(1)
        else:
            raise Exception("Missing \"Plugin\" field in log file.")

        # Get problem name
        problem = name.split(os.sep)[-2]

        # Get problem test suite (if any)
        test_suite = "n/a"
        if name.split(os.sep)[-3] != solver:
            test_suite = name.split(os.sep)[-3]

        # Get time
        time_match = re.search(r'total elapsed time: ([0-9:\.]+)', file)
        if time_match:
            t = time_match.group(1)
            t = 1e-6 * datetime.strptime(t, '%H:%M:%S.%f').microsecond
        else:
            raise Exception("Missing \"total elapsed time\" in log "
                            "file.")
        benchmark.append(
            {
                'solver': solver,
                'testsuite': test_suite,
                'problem': problem,
                'time': t
            }
        )
        print(name)
        print(solver)
        print(problem)
        print(t)
        print(test_suite)

    # Write dictionary to YAML file
    with open(output_dir + '/benchmark.yml', 'w') as outfile:
        outfile.write(yaml.dump(benchmark, default_flow_style=False))


def main(**kwargs):
    log_dir = kwargs['dir_in']
    output_dir = kwargs['dir_out']
    export_benchmark = kwargs['benchmark']

    # Check the existence of the log directory
    if not(os.path.isdir(log_dir)):
        raise Exception("Invalid RobOptim log directory")

    # Find journal.log recursively
    log_name = 'journal.log'
    journal_logs = []
    for root, dirnames, filenames in os.walk(log_dir):
        for filename in fnmatch.filter(filenames, log_name):
            journal_logs.append(os.path.join(root, filename))

    if export_benchmark:
        generate_benchmark_yaml(journal_logs, output_dir)

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description="""
                                     Convert RobOptim logs to YAML files
                                     """)
    parser.add_argument('-i', '--dir-in', type=str, help='root log directory',
                        default='/tmp/roboptim-shared-tests')
    parser.add_argument('-o', '--dir-out', type=str, help='output directory',
                        default='/tmp')
    parser.add_argument('--benchmark', nargs='?', type=bool,
                        const=True, default=True,
                        help='generate a benchmark YAML file')
    args = parser.parse_args()
    main(**vars(args))
