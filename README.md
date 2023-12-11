# MADS-699-Capstone-fa23-team26

#### Master of Applied Data Science, University of Michigan

#### SIADS699: Capstone Project (2023, Fall)

#### Authors

* Wenyuan Du (wenyuand@umich.edu)
* Yesen Zhou (zyesen@umich.edu)
* Xi Lu (lucylu@umich.edu)
## Lists

## Book Recommendation Model

With more and more people searching and buying books online, book recommender systems are becoming increasingly important. The book recommender system, which e-commerce, libraries, and bookstores widely use nowadays, can help readers find books they like efficiently and improve book sales revenue significantly. 
Our project is to build a book recommender system website to recommend books for users based on the information they entered, such as the users' age, users' location, etc. We used supervised and unsupervised machine learning methods to build the book recommender system models, evaluated the performance of models, and built our book recommender system website with the best-performed model.


## Data Source

The data used for this project comes from this Kaggle dataset: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data

To run the code in this repository, download the data from Kaggle and place them in the same directory of the .ipynb file.

## Environment Setup
In order to train the models effeciently, we recommend using a HPC cluster, such as the Great Lake HPC cluster that provides multiple CPUs. We used Jupyter Lab with 40 CPUs on the Great Lake HPC cluster.

The Python libraries are managed by pip. To install all the libraries, run `pip install -r requirements.txt`

## Referrence
* Applied Recommender Systems with Python https://link-springer-com.proxy.lib.umich.edu/book/10.1007/978-1-4842-8954-9