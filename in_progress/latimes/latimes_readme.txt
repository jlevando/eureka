
This readme was last updated by Lisa McAulay on 2021-02-13.

The LA Times Collection is being migrated by Lisa McAulay with assistance from Geno Sanchez. The first major ingest of this collection was performed in December 2019 and March-April 2020. The collection is being re-ingested into Californica-Stage and Ursus-Stage in February-March 2021 to correct the collection name and to correct erroneous values in the date.normalized field. 

* Ingest Challenges *
This collection contains ~17,000 items and when one record is updated, a substantial amount of re-indexing takes place. Ursus stage goes down whenever one of the latimes csv files is ingested. The Apps team decided on a solution on 2/10/21, and they will begin implementing in the near future. Lisa McAulay will wait to re-ingest the collection on production until the new solution is implemented. As of 3/8/21, the solution has not yet been implemented. 

* Problems To Resolve *
latimes2_failed.csv includes 11 items for which we cannot find the original TIFF images. 

* Collection Status *

The collection is continuing to be described in the metadata section of the Resource Acquisition and Metadata Services department (RAMS). 

The collection is divided into several CSVs because it is so large and the processes related to (1) Bucketeer, (2) Fester, and (3) Californica cannot handle more than 3,000 items at a time. I can't remember the details. 

In February 2021, we are trying to re-ingest the collection because we have an error in the collection name. It is showing us that there are some errors in the metadata that are now incompatible with Californica. 

The main error is non-conformance to ISO8601 in the date.normalized field, which the Californica Solr now uses for date sorting.  


