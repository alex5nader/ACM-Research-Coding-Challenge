# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

# Explanation

I started by looking up what a cluster and clustering algorithm are. I found a
python library called `scikit-learn` which integrates with numpy and matplotlib
and provides implementations of and explanations for several clustering algorithms,
as well as a simple explanation of clustering itself.

After reading through the Wikipedia page for
[Cluster Analysis](https://en.wikipedia.org/wiki/Cluster_analysis) and the
`scikit-learn` page for
[Clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering),
I decided to use the DBSCAN algorithm since its comparison images looked the most
accurate to how I would categorize them and because it did not require me to
pre-determine the number of clusters.

I had never used numpy or matplotlib before, so I used the
[DBSCAN example](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py)
to introduce me to basic usage of them. Several ideas in this
example were new to me:
- operations on arrays (`class_member_mask & core_samples_mask`)
  - applies the operation between corresponding members of each array
- indexing an array with another array (`xy = data[class_member_mask & core_samples_mask]`)
  - `a[b]` returns all the elements in `a` for which the corresponding value in `b` is `True`
- comparing an array to a scalar (`class_member_mask = (labels == k)`)
  - returns an array containing the result of the comparison against each element
- slice indexing a matrix (`xy[:, 0]`)
  - works the same as slice indexing for lists, but across all dimensions of the array

After reading through the numpy
[Absolute Beginners Tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html),
I was able to make sense of all these operations.

Finally, I went through the example code and made sure I fully understood the
purpose everything. After my research into numpy, matplotlib, scikit-learn,
and DBSCAN, I was able to make sense of the example.

The exact listing of libraries I used can be found in [requirements.txt](requirements.txt).
