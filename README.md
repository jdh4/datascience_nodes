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

Number of users in last month for all of Della (could probably just include user than subtract 1):

```
$ sacct -a -S 04/08 -P -n -o jobid,user,state | grep -v -E '[0-9_]{4}\.(ex|ba|in)|[0-9_]{4}\.[0-9]{1,}' | awk -F'|' '{print $2}' | sort | uniq | wc -l
305
```
