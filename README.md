# Popularity Prediction Algorithm (PPA) for Aptstore : Dynamic Storage Management for Hadoop
PPA is used to predict the popularity of the files in the cluster. Decision Engine in Aptstore uses this information to decide which files are to be moved from primary to secondary storage and vice versa. It also decides on which files are to be replicated more. The most popular files can be replicated more and kept in primary storage for better i/o throughput. Likewise replication can be avoided for unpopular files and these files can be moved to the secondary storage. This will improve the storage efficiency in the hadoop. The concept of PPA is proposed in the paper mentioned in the reference. 

<p align="center">
    <img src="images/aptstore_architecture.jpg" alt="aptstore architecture overview" />
</p>


I have implemented the Popularity Prediction algorithm (PPA) in python. I have uploaded the source code in plain python file and in a Jupyter notebook which has all the simulated data and the results. Finally, I have displayed the results in bar graph for better visualization. I have also uploaded the ppt containing detailed information and usuage of the algorithm.

## Simulation and Output

### Sample simulation 
I have randomly generated the initial popularity and number of blocks for random files and then predicted the popularity based on accessed and deleted files
<p align="center">
    <img src="images/input_ouput_sc.png" alt="sample input output" />
</p>

### Visualization of Results

<p align="center">
    <img src="images/popularity_sc.png" alt="initial popularity" width=45%  />
    <img src="images/block_sc.png" alt="number of blocks" width=45% /><br>
    <span>Randomly generated initial popularity and number of blocks</span>
</p>
<p align="center">
    <img src="images/predicted_sc.png" alt="Predicted Popularity" width=75% /><br>
     <span>Predicted popularity of files</span>
</p>




If any issue is found in my implementation, please let me know. Thanks for reading.

## Reference
K. R. Krish, A. Khasymski, A. R. Butt, S. Tiwari and M. Bhandarkar, "AptStore: Dynamic storage management for hadoop," 2013 IEEE International Conference on Cluster Computing (CLUSTER), 2013, pp. 1-5, doi: 10.1109/CLUSTER.2013.6702657.

