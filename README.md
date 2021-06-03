# Popularity Prediction Algorithm (PPA) for Aptstore : Dynamic Storage Management for Hadoop
PPA is used to predict the popularity of the files in the cluster. Decision Engine in Aptstore uses this information to decide which files are to be moved from primary to secondary storage and vice versa. It also decides on which files are to be replicated more. The most popular files can be replicated more and kept in primary storage for better i/o throughput. Likewise replication can be avoided for unpopular files and these files can be moved to the secondary storage. This will improve the storage efficiency in the hadoop. The concept of PPA is proposed in the paper mentioned in the reference. 

<p align="center">
    <img src="images/aptstore_architecture.jpg" alt="aptstore architecture overview" />
</p>


I have implemented the Popularity Prediction algorithm (PPA) in python. I have uploaded the source code in plain python file and in a Jupyter notebook which has all the simulated data and the results. Finally, I have displayed the results in bar graph for better visualization. I have also uploaded the ppt containing detailed information and usuage of the algorithm.

## Simulation and Result

### Sample Input Data simulation 
- Files are generated randomly and added to accessed_files list. 
- Some files were chosen randomly from the accessed_files and added to the deleted_files list
<p align="center">
    <img src="images/accessed_deleted_files.png" alt="accessed/deleted files" />
</p>


- Now, for each unique file in accessed_file list, random values for initial popularity and number of blocks are generated
<p align="center">
    <img src="images/input.png" alt="sample input" />
</p>

### Result: Running PPA on Simulated Data
- Simulated data are fed into the PPA algorithm and expected popularity is obtained in the *Predicted_Popularity* column. **NaN** in *Predicted_Popularity* means the corresponding file has been deleted.
<p align="center">
    <img src="images/accessed_deleted_files.png" alt="accessed/deleted files" />
</p>
<p align="center">
    <img src="images/output.png" alt="output" />
</p>

**Result Analysis:** File 4 has the highest value for the predicted_popularity as it has comparatively the least number of blocks and it has been accessed comparatively a greater number of times. Conversely, File 3 has the lowest value for the predicted_popularity as it has comparatively a greater number of blocks and it has been accessed only once. Also, its initial popularity is less.

### Visualization of Results

<p align="center">
    <img src="images/output_graph.png" alt="Output graph" />    
</p>




If any issue is found in my implementation, please let me know. Thanks for reading.

## Reference
K. R. Krish, A. Khasymski, A. R. Butt, S. Tiwari and M. Bhandarkar, "AptStore: Dynamic storage management for hadoop," 2013 IEEE International Conference on Cluster Computing (CLUSTER), 2013, pp. 1-5, doi: 10.1109/CLUSTER.2013.6702657.

