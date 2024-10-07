## What are python memory issues?

### First step - unzip data.zip file
### Second step - work on converting the unzipped file "data.json" to a csv file (inside the converter.py >> convert function)
* use - https://docs.python.org/3/library/csv.html
* create a table with the following headers: Row Number, State, Measure, Value
* then iterate over the "data.json" file and add the data to the table according to the headers

* Data structure of the file:
  * Dictionary with two keys - "meta" and "data"
  * "data" is a list of lists, in each list the data is structured in the following order -
    * [':sid', ':id', ':position', ':created_at', ':created_meta', ':updated_at', ':updated_meta', ':meta', 'port_name', 'state', 'port_code', 'border', 'date', 'measure', 'value', 'latitude', 'longitude', 'point', ':@computed_region_wbq9_i9bc', ':@computed_region_nw2e_u85y', ':@computed_region_erx2_rfp6']
    * this means that if I access data["data"][0][9] - I will get the first row's State

* Data taken from - https://catalog.data.gov/dataset/border-crossing-entry-data-683ae

### Third step - create another file that only has the top 5 states by their value for a specific measure of your choice :) implement in highscore.py >> highscore
### Run your script using ```docker compose up```
### check the output