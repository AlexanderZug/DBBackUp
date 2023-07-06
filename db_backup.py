import datetime
import multiprocessing
import subprocess


def process_database(database):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dump_file = f"{database}_{current_time}.sql"
    command = f"pg_dump -U postgres -d {database} > {dump_file}"
    subprocess.run(command, shell=True)


def parallel_process(databases, parallelism):
    pool = multiprocessing.Pool(processes=parallelism)
    pool.map(process_database, databases)
    pool.close()
    pool.join()
