# Basic-ETL

This is an example final project of a local ETL process. As an intro & undergrad
class this does not include network operations that would typically be expected and this version does not include NoSQL systems. It starts with building Tests (TDD) and then progresses through:
- Checking a directory for files
- Processing the files in the directory based on their extension
  - This example includes a parallel processing option (this was not required)
  - Standard Parsing (remove empty lines and performs basic validation)
    - Text Files include very basic NLP operation (nGram & regex matching)
- Loads data to an included SQLite database
  - This was used to explain the limitations of ACID for analysis
  - Seperate version with MongoDB is included in its own Repository
- Performs standard SQL analysis (using aggregated functions and group by)
- Performs Rule Based Analysis (Affinity Analysis and Proability of event)

This was used to show iterative software development (Agile & TDD) with
Python and in a data engineering application. The project used to build the
data (both the JSON & XML) is included in [JSG-Research-Methods](#addme).

## License

The content of any data used within projects 
themselves is licensed under the 
[Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/) and has been entered by random answering of questions (its fake data).
While the source code of any script or program 
is licensed under the [MIT license](license.md).

<small> 

*All code was authored and written by Professor Greenwell (self) based on 
problems proposed in workbook.*

</small>
