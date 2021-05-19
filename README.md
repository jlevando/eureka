# eureka

A repository for metadata CSV files for ingest into Californica (UCLA instance of Hyrax, part of the Samvera family). 

A metadata CSV can be created through an export from DLCS (UCLA Library's homegrown Digital Library Collection System) or using a metadata template CSV for new collections. This process is managed by members of the Digital Library Program.

Naming convention: short_collection_name.csv. E.g., bennett.csv
Please use underscore (\_) for clarity, if desired. E.g., hood_mantle.csv

There are four major directories in the Eureka repository, which reflect a workflow:
* done 
* in_progress
* checked_out
* metadata_reload

Within each directory there are additional directories for larger collections or paginated materials collections which are comprised of multiple CSVs (pages and works). Additionally, in the `in_progress` directory staff members have named directories in which they put their work. We are transitioning to this new file management practice in May 2021.

`done` is for CSVs for which all the metadata contained in the CSV and all the content files have been fully ingested into Californica. These files are the metadata and file inventory of record for the digital collections they represent.

`in_progress` contains files that are currently being managed actively through the ingest process. 

`checked_out` contains files that have been ported to Google Sheets for a non-DLP staff member to review, edit, add to. This process prevents a file coordination problem when working with collaborators who are not actively using github as part of their regular workflow. 

`metadata_reload` is a waiting location for CSVs that have metadata fields that did not map to the available ingest fields for Californica. There is a metadata review process that we do in batches to prepare these files for ingest or to develop a list of new fields needed in Californica. Files will remain in `metadata_reload` until all metadata is addressed.

Some additional directories for testing have been added and those are:
* _test
* fester_samples

CSV files that are not in `done` should not be edited without communicating with the staff member responsible for shepherding the related collection through ingest. 

CSV files that are not yet ready for production ingest should be kept in the `_test` directory.
