# qstest
Python codes for the (q,s)--test 

Please cite  
  Kojaku, S. and Masuda, N. "A generalised significance test for individual communities in networks". Preprint arXiv:???? (2017).


## Files
Directory qstest/ contains python codes.  
  * qstest/__init__.py is for initialing this package
  * qstest/qstest.py is the main codes of the (q,s)-test 
  * qstest/quality_functions.py contains the codes of the quality functions of individual communities
  * qstest/size_functions.py contains the codes of the size of individual communities.


### INSTALL:

  To install from source, type
        
   python setup.py install 
       
  To install with pip command, type 
        
   pip install qstest 
    	
 
### USAGE:

  To use as a python library:
   
   import qstest
  
 
**[input-file]**  
 * The file should contain a list of edges (space-separated).  
 * The first and second columns represent the IDs of the two nodes forming an edge.    
 * The node's ID is assumed to start from 1.  
  
**[output_file]**  
 * The first column represents the node's ID.
 * The second column represents the index of the core-periphery pair to which each node belongs.
 * The third column indicates whether each node is a core node (= 1) or a peripheral node (= 0).
 * The fourth column indicates whether each node belongs to a significant core-periphery pair (= 1) or not (= 0).
  
  
**[options]**  
* -r R  
 Run the KM-config algorithm R times. (Default: 10)  
* -a ALPHA  
  Set the significance level before the Šidák correction to ALPHA. (Default: 1). If this option is not set, the statistical test is not carried out.
* -l N  
Set the number of randomised networks to N. (Default: 500)
* -d "D"  
Change the delimiter for [input-file] and [output-file] to D. (Default: space)  


 ### EXAMPLES:
    
  To find core-periphery pairs, type
    
    ./km_config example_edge_list.txt result.txt
    
  To find significant core-periphery pairs at a significance level of 0.05, type
 
    ./km_config example_edge_list.txt result.txt -a 0.05 


## MATLAB  
      
### COMPILE:

  Go to the matlab/ directory. Then, type
        
    make
    
  or type
       
    mex CXXFLAGS='$CXXFLAGS -fopenmp' LDFLAGS='$LDFLAGS -fopenmp' CXXOPTIMFLAGS='-O3 -DNDEBUG' LDOPTIMFLAGS='-O3' km_config_mex.cpp 
    
  This will produce a mex file "km_config_mex.mexa64" in the matlab/ directory. 
  Copy "matlab/km_config_mex.mexa64" and "matlab/km_config.m" to your working directory.
 
 
 ### USAGE:

    [c, x, Q, q, p_vals] = km_config(A, num_of_runs, alpha, num_of_rand_nets);
 
 
  **INPUT:** 
 
  * A - N times N adjacency matrix, where N is the number of nodes. A(i, j) = 1 if nodes and j are adjacent. Otherwise A(i, j) = 0. Matrix A should be symmetric, i.e., A(i, j) = A(j, i).
      
  * (optional) num_of_runs - Number of runs. (Default: 10) 
      
  * (optional) alpha - Statistical significance level before the Šidák correction. (Default: 1) If alpha is not set, the statistical test is not carried out. 
      
  * (optional) num_of_rand_nets - Number of randomised networks. (Default: 500) 


  **OUTPUT:**

  * c - N-dimensional column vector. c(i) is the index of the core-periphery pair to which node i belongs.
          If node i belongs to an insignificant core-periphery pair, then c(i) = NaN.
      
  * x - N-dimensional column vector. If node i is a core node, x(i) = 1. If node i is a periphery node, x(i) = 0.
          If node i belongs to an insignificant core-periphery pair, then x(i) = NaN.
      
  * Q - The quality value of the detected core-periphery pair.
      
  * q - C-dimensional column vector. q(i) is the contribution of the i-th core-periphery pair to Q.
          C is the number of core-periphery pairs.
      
  * p_vals - C-dimensional column vector. p_vals(i) is the statistical significance of the i-th core-periphery pair. 

  
### EXAMPLES:
    
To find core-periphery pairs, type 
 
    [c, x, Q, q] = km_config(A);

To find significant core-periphery pairs at a significance level of 0.05, type	
    
    [c, x, Q, q, p_vals] = km_config(A, 10, 0.05);


### REQUIREMENT: 
      
  MATLAB 2012 or later.

---
Last updated: 17 October 2017


