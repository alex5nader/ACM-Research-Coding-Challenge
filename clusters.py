import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN


def main() -> None:
    data = np.genfromtxt('ClusterPlot.csv', skip_header=1, delimiter=',', usecols=(1, 2))

    db = DBSCAN(eps=0.25, min_samples=10).fit(data)

    # array containing whether or not each point is a core point
    # a core point is one that has >= min_samples points nearby
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True

    # array containing id of cluster (or -1 for noise) for each point (label is the id of a cluster)
    labels = db.labels_

    # number of clusters (not including any noise)
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Cluster count:', n_clusters_)
    print('Noise point count:', n_noise_)

    unique_labels = set(labels)
    # colors evenly spaced along spectral colormap for each cluster
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

    plt.title('Clusters')

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]

        # array containing whether or not each point is in the current cluster
        class_member_mask = (labels == k)

        # get all core points in this cluster
        # xy is of the form
        # [[x1, y1],
        #  [x2, y2],
        #  [x3, y3],
        #  etc...  ]
        xy = data[class_member_mask & core_samples_mask]
        # draw them big
        # xy[a:b, 0] returns a list of xN for all a <= N < b
        # a and b default to 0 and len(xy)
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

        # get all non-core points in this cluster
        xy = data[class_member_mask & ~core_samples_mask]
        # draw them small
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)

    plt.show()


if __name__ == '__main__':
    main()
