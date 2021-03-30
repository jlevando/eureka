
This readme was last updated by Lisa McAulay on 2021-03-29.

The LA Times Collection is being migrated by Lisa McAulay with assistance from Geno Sanchez. The first major ingest of this collection was performed between December 2019 and April 2020. In February 2021, we began the process of re-ingesting the collection into Californica-Stage and Ursus-Stage to correct the collection name and to correct erroneous values in the date.normalized field. As of March 2021, that process is still ongoing. 

* Action Log *
3/16/21 - on Californica-Stage, added a value to column description.note in the latimes_collection.csv, and then re-festerized the csv (not sure if that was necessary or not) Began new ingest circa 8:30am.

3/29/21 - testing on STAGE a new setup from John that should allow ingest into Californica without bringing ursus down

* Ingest Challenges *
This collection contains ~17,000 items and when one record is updated, a substantial amount of re-indexing takes place. Ursus stage goes down whenever one of the latimes csv files is ingested. The Apps team decided on a solution on 2/10/21, and they will begin implementing in the near future. Lisa McAulay will wait to re-ingest the collection on production until the new solution is implemented. As of 3/22/21, the solution has not yet been implemented. 


* Collection Status : In Progress *

The collection is continuing to be described in the metadata section of the Resource Acquisition and Metadata Services department (RAMS). 

Rows in the CSV marked with a value in the item_status other than "Completed" are loaded into Californica, but marked as "Private" and not released to Ursus. 

The collection is divided into several CSVs because it is so large and the processes related to (1) Bucketeer, (2) Fester, and (3) Californica cannot handle more than 3,000 items at a time. 

In February 2021, we are trying to re-ingest the collection because we have an error in the collection name. It is showing us that there are some errors in the metadata that are now incompatible with Californica. 

The main error is non-conformance to ISO8601 in the date.normalized field, which the Californica Solr now uses for date sorting.  

Image Problems

11 items related to Paul Conrad and winning the Pulitzer prize in 1984 are lost. Those items have been marked "Needs QA" in DLCS and moved to latimes_cannot_migrate.txt file. The negatives will need to be rescanned if we want to put them online through the Samvera interface.  


