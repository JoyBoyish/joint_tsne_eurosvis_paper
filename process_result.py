# encoding = utf-8
import os
import numpy as np


def save_cluster(cluster_path, texts):
    with open(cluster_path, 'w', encoding='utf-8') as f:
        for line in texts:
            f.write(line + "\n")

    print("save {} successfully. ".format(cluster_path))


def split_result(result_path):
    label_set = {}
    with open(result_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            items = line.split()
            label = items[-1]

            if label not in label_set:
                # create an empty array
                label_set[label] = []

            label_set[label].append(line)

    return label_set


if __name__ == "__main__":
    data_name = "dynamic_tsne_final"
    result_dir = os.path.join(
        "/Users/joe/Codes/PythonProjects/joint_tsne_experiments/results",
        data_name)

    for method_name in os.listdir(result_dir):
        method_dir = os.path.join(result_dir, method_name)
        for result_name in os.listdir(method_dir):
            result_path = os.path.join(method_dir, result_name)
            cluster_set = split_result(result_path)

            for cluster_name, cluster_texts in cluster_set.items():
                cluster_dir = os.path.join(method_dir, cluster_name)
                if not os.path.exists(cluster_dir):
                    os.mkdir(cluster_dir)
                cluster_path = os.path.join(cluster_dir, result_name)
                save_cluster(cluster_path, cluster_texts)
