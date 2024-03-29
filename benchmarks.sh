python hash_tables.py --input_file non_rand_words.txt --hash_function ascii --hash_table linear --table_size 15000 | python3 scatter.py table_ascii_linear_nonrand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file non_rand_words.txt --hash_function rolling --hash_table linear --table_size 15000 | python3 scatter.py table_rolling_linear_nonrand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file non_rand_words.txt --hash_function ascii --hash_table chained --table_size 10000 | python3 scatter.py table_ascii_chained_nonrand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file non_rand_words.txt --hash_function rolling --hash_table chained --table_size 10000 | python3 scatter.py table_rolling_chained_nonrand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file rand_words.txt --hash_function ascii --hash_table linear --table_size 15000 | python3 scatter.py table_ascii_linear_rand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file rand_words.txt --hash_function rolling --hash_table linear --table_size 15000 | python3 scatter.py table_rolling_linear_rand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file rand_words.txt --hash_function ascii --hash_table chained --table_size 10000 | python3 scatter.py table_ascii_chained_rand.png "Load Factor" "Insertion Time"
python hash_tables.py --input_file rand_words.txt --hash_function rolling --hash_table chained --table_size 10000 | python3 scatter.py table_rolling_chained_rand.png "Load Factor" "Insertion Time"

python hash_functions.py --input_file non_rand_words.txt --hash_function ascii --table_size 10000 | python3 scatter.py function_ascii_nonrand.png "Hashed Word" "Hashed Value"
python hash_functions.py --input_file non_rand_words.txt --hash_function rolling --table_size 10000 | python3 scatter.py function_rolling_nonrand.png "Hashed Word" "Hashed Value"
python hash_functions.py --input_file rand_words.txt --hash_function ascii --table_size 10000 | python3 scatter.py function_ascii_rand.png "Hashed Word" "Hashed Value"
python hash_functions.py --input_file rand_words.txt --hash_function rolling --table_size 10000 | python3 scatter.py function_rolling_rand.png "Hashed Word" "Hashed Value"
