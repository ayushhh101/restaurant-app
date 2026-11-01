BIG DATA ANALYTICS PRACTICAL — PENDRIVE KIT
Prepared from the seven uploaded experiment journals.

CONTENTS
Each Experiment_N folder contains exactly two files:
- ExpN_Instructions.txt — baby-step execution instructions.
- ExpN_Code.<extension> — code/command reference to paste or execute.

IMPORTANT ENVIRONMENT NOTE
The source journals span different software stacks and versions: Hadoop/MapReduce, Sqoop/MySQL, MongoDB, Pig, Python, and R. A single laptop cannot reliably validate all of these without their matching runtimes and services. I executed the Python Experiment 6 program and checked its output. The Java MapReduce code was reviewed for API/type consistency but cannot be compiled here without Hadoop libraries. MongoDB, Sqoop, Pig and R code were checked against the journal's structure and syntax but were not run against live services here. Experiment 1/2 require a correctly configured Linux Hadoop lab environment. Please do not interpret static review as a live integration test.

EXAM-DAY STRATEGY
1. Identify which experiment number is asked.
2. Open that folder's Instructions file first.
3. Follow the numbered steps in order.
4. Open the matching Code file and paste only the required section.
5. Keep input and output paths exactly as the instructions say, unless your lab gives different paths.
6. Hadoop MapReduce output directories must not already exist.
7. Never format HDFS or drop a database/collection just to fix an error. The MongoDB script does not drop existing collections.

SOURCE JOURNAL ALIGNMENT
- Exp 1: pseudo-distributed Hadoop + HDFS commands.
- Exp 2: Sqoop import/export, selected columns/rows, password options, compression.
- Exp 3: Word Count, total word count, matrix multiplication (2x5 × 5x3).
- Exp 4: online bookstore CRUD, search, regex, aggregation and indexes.
- Exp 5: Pig agriculture and Titanic analysis.
- Exp 6: Bloom Filter + DGIM malicious URL/threat stream.
- Exp 7: Iris dataset analysis and plots in R.

Known assumptions are called out inside the corresponding instruction files. In particular, Experiment 5 requires the actual CSV datasets; Experiment 2 requires matching MySQL credentials/schema; Hadoop/Sqoop/Pig require compatible lab installations.
