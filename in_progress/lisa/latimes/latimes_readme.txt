This readme was last updated by Lisa McAulay on 2021-05-19.

The LA Times Collection is being migrated by Lisa McAulay with assistance from Geno Sanchez. The first major ingest of this collection was performed between December 2019 and April 2020. In February 2021, we began the process of re-ingesting the collection into Californica-Stage and Ursus-Stage to correct the collection name and to correct erroneous values in the date.normalized field. We later discovered 3 additional corrections to make: repository name, license, and festerizing. As of May 2021, that process is still ongoing. After the re-ingest is completed, we need to ingest new metadata for the materials described under "OpenUCLA"

* Blockers *

2021-05-21 - still waiting on APPS-835 ticket (delete child items on californica stage for pages ingested pre-fester workflow). cannot ingest on stage until after that work is completed. Dawn is testing the work done by Andy on APPS-835 with a new ingest of Armenian manuscripts on californica-stage.


* Action Log *

5/21/21 - Feeling frustrated at having had to wait over 6 months to fix this problem, decided to attempt moving past validating my work on stage (since stage is caught up in the Armenian manuscripts process) and skipping on to doing the work on production. Started an import of latimes1.csv at 7:42am today

5/19/21 - Reviewing latimes1.csv for all the required revisions. Repository name is consistent and correct, Manifest URLs are the final column (has been festerized), added CC 4.0 license URI.

5/15/21 - experimented with adding License column and value using latimes2_failed on californica-stage. It seemed to work. Must use the exact same URI as used in LA Daily News (because it must already be enabled in a way that the other creative commons URIs are not (because I tried a different one and it did not work)). 

4/30/21 - Anthony changed the limits on filesize for nginx which unblocked me related to feseterizing latimes1 and latimes 2.csv 

4/20/21 - correcting values for repository name, services contact, and rights holder in latimes7.csv and latimes8.csv

4/19/21 - discovered that some of the LA Times csvs have not been festerized. Including, latimes1, latimes2

4/13/21 - cleaned up values in name.repository column of latimes3.csv to use when re-ingesting into californica-stage

3/29/21 - testing on STAGE a new setup from John that should allow ingest into Californica without bringing ursus down

3/16/21 - on Californica-Stage, added a value to column description.note in the latimes_collection.csv, and then re-festerized the csv (not sure if that was necessary or not) Began new ingest circa 8:30am. 

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


