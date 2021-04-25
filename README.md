# datascience_nodes

See this directory:

```
/Users/jhalverson/rc/cluster_stats/datascience_partition/<date>
```


To obtain data:

```
$ ssh della
$ sacct -S 02/19 -P -a --partition=datascience -o jobid%20,user,account,state%12,start,elapsed,elapsedraw,timelimit%15,timelimitraw,cputimeraw,ncpus,nnodes,reqmem%10,partition%15,alloctres%50,qos,maxrss%15 > feb19_mar19_2021_datascience.csv
```
