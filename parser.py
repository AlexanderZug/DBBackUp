import multiprocessing
import argparse

from db_backup import parallel_process, process_database


def get_cli_options() -> argparse.Namespace:
    """
    Return CLI argument object
    """
    parser = argparse.ArgumentParser(
        description="Dump databases and cleanup the dump files"
    )
    parser.add_argument(
        "-d",
        "--database",
        type=str,
        help="Database(s) to dump",
    )
    parser.add_argument(
        "-p",
        "--parallel",
        action="store_true",
        help="Run the script in parallel mode",
    )
    return parser.parse_args()


def main():
    options = get_cli_options()
    databases = options.database.split(",")
    num_cores = multiprocessing.cpu_count()
    parallelism = num_cores

    if options.parallel:
        parallel_process(databases, parallelism)
    else:
        for db in databases:
            process_database(db)


if __name__ == "__main__":
    main()