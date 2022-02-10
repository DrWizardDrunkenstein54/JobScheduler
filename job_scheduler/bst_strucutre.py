from datetime import *


class Node:  # Node object is a job with a start time, length of the job, and name of the job

    def __init__(self, job_info):

        start_time, duration, name = job_info.split(",")
        self.right_child = None
        self.left_child = None
        self.ui_starting_time = start_time
        self.ui_duration = duration
        self.name = name
        self.starting_time = datetime.strptime(self.ui_starting_time, '%H:%M:%S')
        self.duration = datetime.strptime(self.ui_duration, "%H:%M:%S")  # REAL DURATION OF JOB --> COMPARABLE
        raw_end_time = self.starting_time + timedelta(hours=self.duration.hour,
                                                      minutes=self.duration.minute,
                                                      seconds=self.duration.second)
        raw_end_time = str(raw_end_time)
        self.end_time = raw_end_time[11:]  # REAL END TIME OF JOB --> COMPARABLE


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_job(self, new_node):  # Jobs are nodes
        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        if self.root is None:
            self.root = new_node

        else:
            self._insert_job(self.root, new_node)

    def _insert_job(self, current_node, new_node):  # Current node, What to insert
        # NOTE: JOB DURATION HAS TO BE LESS THAN 24 HOURS
        current_node_starting_time = current_node.ui_starting_time[0:2]
        current_node_end_time = current_node.end_time[0:2]
        new_node_starting_time = new_node.ui_starting_time[0:2]
        new_node_end_time = new_node.end_time[0:2]

        if new_node_starting_time[:2] == "0" + new_node_starting_time[1]:
            new_node_starting_time = new_node_starting_time[1]

        if new_node_end_time[:2] == "0" + new_node_end_time[1]:
            new_node_end_time = new_node_end_time[1]

        if current_node_starting_time[:2] == "0" + current_node_starting_time[1]:
            current_node_starting_time = current_node_starting_time[1]

        if current_node_end_time[:2] == "0" + current_node_end_time[1]:
            current_node_end_time = current_node_end_time[1]



        if int(new_node_starting_time) > int(current_node_end_time):
            if current_node.right_child is None:
                current_node.right_child = new_node
            else:
                self._insert_job(current_node.right_child, new_node)

        elif int(new_node_end_time) < int(current_node_starting_time) and int(new_node_end_time) < int(current_node_end_time):

            if current_node.left_child is None:
                current_node.left_child = new_node
            else:
                self._insert_job(current_node.left_child, new_node)

        elif int(new_node_starting_time) == int(current_node_end_time):  # If hour is the same, we need to check the minutes
            if int(new_node.ui_starting_time[3:5]) > int(current_node.end_time[3:5]):  # Grabbing indices
                if current_node.right_child is None:
                    current_node.right_child = new_node
                else:
                    self._insert_job(current_node.right_child, new_node)
            elif int(new_node.end_time[3:5]) < int(current_node.ui_starting_time[3:5]):
                if current_node.left_child is None:
                    current_node.left_child = new_node
                else:
                    self._insert_job(current_node.left_child, new_node)
        else:
            print("Your job cannot be inserted because there's a time conflict with another job that you specified previously")


    def job_order(self):
        self._job_order(self.root)

    def _job_order(self, current_job_node):
        if current_job_node:
            self._job_order(current_job_node.left_child)
            print(f"|Job Name: {current_job_node.name} | Starting Time: {current_job_node.ui_starting_time} | Duration: {current_job_node.ui_duration} |", end=" " + "\n")
            self._job_order(current_job_node.right_child)

    def min_right_subtree(self, curr):
        if curr.left_child is None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_job(self, active_node):
        self._delete_job(self.root, None, None, active_node)

    def _delete_job(self, current_node, prev_node, is_left, delete_node):
        if current_node:
            if delete_node == current_node.name:
                if current_node.left_child and current_node.right_child:
                    min_child = self.min_right_subtree(current_node.right_child)
                    current_node.name = min_child.data
                    self._delete_job(current_node.right_child, current_node, False, min_child.data)
                elif current_node.left_child is None and current_node.right_child is None:
                    if prev_node:
                        if is_left:
                            prev_node.left_child = None
                        else:
                            prev_node.right_child = None
                    else:
                        self.root = None
                elif current_node.left_child is None:
                    if prev_node:
                        if is_left:
                            prev_node.left_child = current_node.right_child
                        else:
                            prev_node.right_child = current_node.right_child
                    else:
                        self.root = current_node.right_child
                else:
                    if prev_node:
                        if is_left:
                            prev_node.left_child = current_node.left_child
                        else:
                            prev_node.right_child = current_node.left_child
                    else:
                        self.root = current_node.left_child
            elif delete_node < current_node.name:
                self._delete_job(current_node.left_child, current_node, True, delete_node)
            elif delete_node > current_node.name:
                self._delete_job(current_node.right_child, current_node, False, delete_node)
        else:
            print(f"{delete_node} not found in tree")


# a = Node("05:30:00,00:30:00,job1")
# b = BinarySearchTree()
# b.insert_job(a)
#
#
# print(b.root.ui_starting_time)
