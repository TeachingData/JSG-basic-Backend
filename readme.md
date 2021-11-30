# Basic-Backend

Before students could be introduced to the actual ETL (Extract-Transfer-Load) process, it was nesscary to introduce backend engineering work. This contains both an overview of scripting techniques and some specific tools for processing *"standard"* files and an example project of standard serialization using json. As an intro & undergrad
class this does not include network operations that would typically be expected nor NoSQL systems (these are covered in a seperate section). It starts with building Tests (TDD), full mock systems are found in a different course, and then progresses through:
- Checking a directory for files
- Processing the files in the directory based on their extension
  - This example includes a parallel processing option (this was not required)
  - Standard Parsing (remove empty lines and performs basic validation)
- Loads data to an included SQLite database
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
