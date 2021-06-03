# Popularity Prediction Algorithm (PPA) for AptStore : Dynamic Storage Management for Hadoop

## Introduction
- Typical Hadoop setups employ Direct Attached Storage (**DAS**) with compute nodes and uniform replication of data to sustain high I/O throughput and fault tolerance. However, not all data is accessed at the same time or rate. Thus, if a large replication factor is used to support higher throughput for popular data, it wastes storage by unnecessarily replicating unpopular data as well. Conversely, if less replication is used to conserve storage for the unpopular data, it means fewer replicas for even popular data and thus lower I/O throughput.
- How can we achieve to improve the overall I/O throughput while reducing the storage cost?

<p align="center">
    <img src="images/aptstore_architecture.jpg" alt="aptstore architecture overview" />
</p>

### AptStore : Dynamic Storage Management for Hadoop
AptStore is a dynamic data management system for Hadoop, which aims to improve overall I/O throughput while reducing storage cost. It is a tiered storage system that uses the standard Direct Attached Storage (DAS) (primary storage) for popular data to sustain high I/O throughput, and network attached storage (NAS) (secondary storage) for cost-effective, fault-tolerant, but lower-throughput storage for unpopular data. 

To determine how popular a file is, an algorithm is needed that can analyze the file system audit logs and predict the popularity of file. This is done by using a file **popularity prediction algorithm (PPA)**. At every RT (Reference time), the PPA analyzes the access pattern for each file and predicts a expected popularity value for it for the next RT.

## Problem Statement

In AptStore, a decision engine (DE) uses an algorithm to predict the expected popularity of files for the next reference time (RT) in the Hadoop cluster. This algorithm is called a **popularity prediction algorithm (PPA)**. Based on the predicted popularity score of the files, DE can suggest USS (Unified Storage System) on which files are to be kept in the primary storage and which ones to be kept in the secondary storage. It also gives insight to decide which files are to be replicated more and for which files replication is to be avoided. This decision helps in improving the i/o throughput as well as reducing the storage cost. **_Implement PPA which will predict the expected popularity of files using their initial popularity, access intervals, number of blocks and load in the cluster_**.

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

