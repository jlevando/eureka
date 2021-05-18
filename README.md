# eureka

A repository for metadata CSV files for ingest into Californica (UCLA instance of Hyrax, part of the Samvera family). These CSVs are usually created through exported from DLCS (UCLA Library's homegrown Digital Library Collection System) or may be newly created for new collections based on the Californica metadata template.

Naming convention: short_collection_name.csv. E.g., bennett.csv
Please use camel case for longer names. 

There are four directories in the Eureka repository, which reflect a workflow:
* done 
* in_progress
* checked_out
* metadata_reload

CSV files that are not in `done` should not be edited without communicating with the staff member responsible for shepherding the related collection through ingest. 

CSV files that are not yet ready for production ingest should be kept in the `_test` directory.
