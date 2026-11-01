# EXPERIMENT 2 — SQOOP COMMAND REFERENCE
# Run commands individually in Linux terminal; first create the MySQL schema as in instructions.
# Check tools:
java -version
hadoop version
sqoop version
mysql --version

# Import full table:
sqoop import --connect jdbc:mysql://localhost:3306/college --username root -P --table faculty --target-dir /user/$USER/faculty_import --delete-target-dir --num-mappers 1

# Import subset:
sqoop import --connect jdbc:mysql://localhost:3306/college --username root -P --table faculty --columns id,name,salary --where "department='Computer'" --target-dir /user/$USER/faculty_subset --delete-target-dir --num-mappers 1

# Password-file import (create mysql.pass securely first):
sqoop import --connect jdbc:mysql://localhost:3306/college --username root --password-file file://$PWD/mysql.pass --table faculty --target-dir /user/$USER/faculty_filepass --delete-target-dir --num-mappers 1

# Compressed import:
sqoop import --connect jdbc:mysql://localhost:3306/college --username root -P --table faculty --target-dir /user/$USER/faculty_gzip --delete-target-dir --compress --compression-codec org.apache.hadoop.io.compress.GzipCodec --num-mappers 1

# Export:
sqoop export --connect jdbc:mysql://localhost:3306/college --username root -P --table faculty_export --export-dir /user/$USER/faculty_export_input --input-fields-terminated-by '\t' --num-mappers 1
