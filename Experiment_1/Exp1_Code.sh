# Experiment 1 is command-line based; paste/run commands from Exp1_Instructions.txt.
# This shell file is a compact reference. Run each command individually in a Linux terminal.
java -version
hadoop version
echo "$HADOOP_HOME"
start-dfs.sh
start-yarn.sh
jps
hdfs dfs -mkdir -p /user/$USER/bda
hdfs dfs -ls /
printf "Hello Hadoop\nBig Data Analytics\n" > sample.txt
hdfs dfs -put -f sample.txt /user/$USER/bda/
hdfs dfs -cat /user/$USER/bda/sample.txt
hdfs dfs -get -f /user/$USER/bda/sample.txt downloaded_sample.txt
printf "Moved file example\n" > moved.txt
hdfs dfs -moveFromLocal moved.txt /user/$USER/bda/
hdfs dfs -cp /user/$USER/bda/sample.txt /user/$USER/bda/sample_copy.txt
hdfs dfs -mv /user/$USER/bda/sample_copy.txt /user/$USER/bda/renamed.txt
hdfs dfs -ls /user/$USER/bda
hdfs dfs -cat /user/$USER/bda/renamed.txt
