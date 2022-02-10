# JOB SCHEDULER PROJECT

from job_scheduler.bst_strucutre import *

run_status = True

my_company = BinarySearchTree()


def welcome():
    print("Welcome to your job scheduler app!")
    print("To get started, here is your key:")
    print("\t1: Check current job schedule")
    print("\t2: Add a job to the schedule")
    print("\t3: Delete a job from the schedule")
    print("\t4: Quit job scheduler and review jobs")


def job_schedule():
    my_company.job_order()


def add_job():
    job_title = input("Enter the name of the job: ")
    job_start_time = input("Enter the start time of the job in the following format (hh:mm:ss): ")
    job_duration = input("Enter the duration of the job: ")
    job_information = f"{job_start_time},{job_duration},{job_title}"

    my_company.insert_job(f"{job_information}")


def delete_job():
    job_to_delete = input("Enter the name of the job: ")
    my_company.delete_job(job_to_delete)


def exit_app():
    global run_status
    run_status = False
    print("\nThanks for using our app, hope to see you soon!")
    my_company.job_order()


def get_input():
    user_decision = input("Enter a number between 1 and 4: ")
    if int(user_decision) == 1:
        job_schedule()
    elif int(user_decision) == 2:
        add_job()
    elif int(user_decision) == 3:
        delete_job()
    elif int(user_decision) == 4:
        exit_app()
    else:
        print("Oops! Something was wrong with your input! Please Try Again!")
        get_input()


if __name__ == "__main__":
    welcome()
    while run_status:
        get_input()
