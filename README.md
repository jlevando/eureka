# eureka

A repository for metadata CSV files for ingest into Californica (UCLA instance of Hyrax, part of the Samvera family). 

A metadata CSV can be created through an export from DLCS (UCLA Library's homegrown Digital Library Collection System) or using a metadata template CSV for new collections. This process is managed by members of the Digital Library Program (DLP).

For collections that are being prepared for Californica, we intend the Eureka repository to be the repository of record for metadata and digital file inventories. The DLP is reviewing this intention and our current workflows to test the validity and stability of this designation. We do not think Eureka will be our ideal repository of record, but in the current time during our migration and infrastructure development, Eureka is the de facto repository of record. 

Naming convention: 
short_collection_name.csv. E.g., bennett.csv
Please use underscore (\_) for clarity, if desired. E.g., hood_mantle.csv

There are four major directories in the Eureka repository, which reflect a workflow:
* done 
* in_progress
* checked_out
* metadata_reload

Within each directory there are additional directories for larger collections or paginated materials collections which are comprised of multiple CSVs (pages and works).

`done` is for CSVs for which all the metadata contained in the CSV and all the content files have been fully ingested into Californica. These files are the metadata and file inventory of record for the digital collections they represent.

`in_progress` contains files that are currently being managed actively through the ingest process. In the `in_progress` directory we use directories for each staff member to contain the CSVs for collections they are actively working on. This sequestering of CSVs into staff member's designated directories makes clear who is working on which collections. We are transitioning to this new file management practice in May 2021.

`checked_out` contains files that have been ported to Google Sheets for non-DLP staff member to review, edit, and add to. Examples of people to whom a CSV may be checked out to include, designated staff in Library Special Collections or metadata staff in Resource Acquisition and Metadata Services. This process of moving a CSV into `checked_out` helps highlight files that are in process outside of the repository. We use this process to assist in file coordination and team communication when working with collaborators who are not actively using github as part of their regular workflow. 

`metadata_reload` is a holding location for CSVs that have metadata fields that did not map to the available ingest fields for Californica. There is a metadata review process that we do in batches to identify solutions for several collections and implement new fields in Californica if needed. Files will remain in `metadata_reload` until all metadata is addressed.

Some additional directories for testing have been added and those are:
* _test
* fester_samples

CSV files that are not in `done` should not be edited without communicating with the staff member responsible for shepherding the related collection through ingest. 

CSV files that are not yet ready for production ingest should be kept in the `_test` directory.
