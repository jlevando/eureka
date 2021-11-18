This readme was last updated by Lisa McAulay on 2021-11-18.

The LA Times Collection is being migrated by Lisa McAulay with assistance from Geno Sanchez. All csvs now contain the correct values for collection and repository names and have the right CC license. All CSVs are festerized with the correct values and have been loaded to both stage and prod. Now the task comes of creating a new batch load of newly described content to publish under the "OpenUCLA" collection. First step is to create a new CSV containing LA Times items with status = pending. 

Process:
- festerize on local computer
- ingest newly festerized csv to cal-stage
- run jenkins solr synch on stage 
- check an item for accuracy (QC) (ursus-stage)
- ingest to cal-prod
- run jenkins solr synch on prod (digital)
- check an item for accuracy



* Concerns *

- Accurately completing an update to the LA Times collection


* CSV Statuses *

latimes_collection.csv     NEEDS re-festerizing after all other csvs have been festerized; added value for license; repository name is correct (1 row)
latimes1.csv               ingested into californica prod 5/21/21; stage 6/10/21 -- license value and repository name are correct  (2996 rows)
latimes_failed.csv         ingested into californica prod 5/21/21 -- festerized, has license value; repository name is correct) (1 row) 

*latimes2.csv*               may be outmoded? - ingested to californica prod on 5/22/21 -- NEEDS re-festerizing, broke original csv into 10 separate CSVs since tetsting on 10/22/21 revealed that fester would no longer handle the larger csv,  (10/25/21); previously had  added value for License to CSV; and checked that repository name is correct  (2986 rows)

latimes2-1.csv             ingested to californica prod on 10/25/21 -- re-festerized; License and repository name are correct  (300 rows) 
latimes2-2.csv             ingested to californica prod on 10/26/21 -- re-festerized; License and repository name are correct  (300 rows) 
latimes2-3.csv             ingested to californica stage + prod 10/27/21 -- re-festerized; License and repository name are correct  (300 rows) 
latimes2-4.csv             ingested to californica stage + prod 10/27/21 -- re-festerized; License and repository name are correct  (300 rows) 
latimes2-5.csv             ingested to californica stage + prod 10/28/21 -- re-festerized; License and repository name are correct  (300 rows) 
latimes2-6.csv             ingested to californica stage + prod 10/29/21 -- re-festerized on 10/26/21; License and repository name are correct  (300 rows) 
latimes2-7.csv             ingested to californica stage + prod 10/29/21 -- re-festerized on 10/26/21; License and repository name are correct  (300 rows) 
latimes2-8.csv             ingested to californica stage + prod 10/30/21 -- re-festerized on 10/30/21; License and repository name are correct  (300 rows) 
latimes2-9.csv             ingested to californica stage + prod 11/02/21 -- re-festerized on 11/02/21; License and repository name are correct  (## rows) 
latimes2-10.csv            ingested to californica stage + prod 11/03/21 -- re-festerized on 11/02/21; License and repository name are correct  (287 rows) 
latimes2_supplement.csv    ingested to californica stage on 11/12/21; ingested to prod 11/13/21 -- re-festerized on 11/12/21; License and repository name is correct  (1 row) (renamed from latimes2_failed.csv since the name was really distracting when trying to troubleshoot problems since the file seemed to be self-describing as a failure)
latimes3.csv               ingested to californica prod on 5/22/21; NEED to ingest to stage -- festerized 5/22/21; License and repository name are correct  (3001 rows)
latimes4.csv               ingested to californica prod on 5/23/21; ingested to stage 11/13/21 -- festerized; License and repository name are correct  (2994 rows)
latimes5.csv               ingested to californica prod on 5/23/21; ingested to stage 11/15/21 -- festerized 5/23/21; License and repository name are correct (2996 rows)
latimes6.csv               ingested to californica prod on 5/24/21; ingested to stage 11/16/21 -- festerized 5/24/21; License and repository name are correct (3000 rows)
latimes7.csv               ingested to californica prod on 5/24/21; ingested to stage 11/17/21 -- re-festerized on 5/24/21, License and repository value are correct (2794 rows)
latimes7_failed_new.csv    ingested to californica prod on 5/25/21; ingested to stage 11/17/21 -- re-festerized 5/25/21; License and repository name are correct (192 rows)
latimes8.csv               ingested to californica prod on 5/25/21; ingested to ingest to stage 11/17/21 -- re-festerized on 5/25/21; License and respository name are correct (60 rows)


* Action Log *

Reviewing all latimes csvs for item status is not equal to 'completed.' 
latimes1.csv was all 'completed'
same with latimes2-1.csv through latimes2-7.csv
latimes2-8 had multiple item statuses so i am separating them into different files. 
latimes2-8_dupes.csv now has all the items that are marked as duplicating other items that are already published. These items will not be published.
latimes2-8_in_progress.csv contains the items with the status "in progress" and I looked in DLCS and the sample of 3 items that I looked at were all still "in_progress".
latimes2-8.csv now only contains the files that are "completed". 
latimes2-9_dupes.csv now has all the items that are marked as duplicating other items that are already published. These items will not be published. latimes2-9_in_progress.csv contains 2 items with the status "in progress" and I looked in DLCS both still "in_progress"
latimes2-9_needs_review.csv has items with the status "needs review" in DLCS. I reviewed all of these in DLCS and they look like files that won't be published. but i'll need to check in with Martha and Claudia when I've got the other things cleaned up. 
latimes2-9.csv now only contains the files that are "completed". 
latimes2-10_newly_completed.csv - contains 1 item that looks like it was changed status 
latimes2-10_needs_review.csv has items with the status "needs review" in DLCS. I reviewed all of these in DLCS and 3 of 4 look like files that won't be published; the 4th, I'm unsure. I'll need to check in with Martha and Claudia when I've got the other things cleaned up. 
latimes2-10.csv now only contains the files that are "completed".
latimes3_imported.csv - contains items with status "imported" (as of the time this csv was initially created)
latimes3_pending.csv - contains items with status "pending"
latimes3.csv now only contains the files that are "completed".
latimes4.csv now only contains the files that are "completed". created 4 new files: latimes4_pending.csv, latimes4_needs_review.csv, latimes4_in_progress.csv, latimes4_imported.csv
now reviewing latimes5.csv

Moving on to look at other csvs for item status to get them all sorted into groups before moving forward. 
"in_progress" CSVs items might need to be reviewed in more detail. 

11/18/21 - running jenkins for latimes8.csv

11/17/21 - ran jenkins to sync californica-stage and ursus-stage for latimes7.csv; verified results of latimes7.csv load; ingested latimes7_failed_new.csv to stage, used jenkins, verified results; ingested latimes8.csv to stage

11/16/21 - ran jenkins to synch californica-stage and ursus-stage; verified results of latimes5.csv load; ingested latimes6.csv into stage, used jenkins, ingested latimes7.csv to stage

11/15/21 - ingested latimes5.csv into stage 

11/13/21 - moved on to ingest latimes4.csv into stage - completed; solr reindexed for ursus-stage on 11/15/21

October - November 2021 - Lisa working on understanding difficulties with festerize workflow. Lisa had to update her festerize and that required some cleanup of old Python and Festerize files (did this cleanup synchronously with Mark); Library computing infrastructure had a massive outage on 10/21/21. Additionally, when working together, Mark and Lisa determined that  the CSVs with ~3000 rows are too large for current festerize workflow (but the underlying problem we think is a timeout for the ingest fester service). We tried with 100 rows and it worked; so maybe try with 500 rows, and if that works, try splitting the csvs into smaller portions. 

10/25/21 - Began trying to pick up where I left off in May 2021; needed help with festerize and had to change number of rows per CSV since Fester is now timing out when trying to run the 3000 row CSVs. Broke latimes2.csv into 10 batches.

10/22/21 - Paired with Mark Matney for a lengthy troubleshooting process related to updating the festerize script on my local computer and then determining that the CSVs I had used in the past were now too large to go through the Fester workflow without timeout.

5/25/21 - (Lisa) Completed loading latimes csvs into californica prod. 

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

* Detailed Notes about Different Phases of Work * 

*October - November 2021*
First main activity when coming back to this collection was to finish ingesting the most recent CSVs to californica-stage since Lisa was unable to do that in May 2021 due to competing work taking place at the same time of stage for another collection. 

Accomplishing this "behind the scenes" work served the purpose of catching the LA Times collection back up to our standard workflow, which is ingest CSVs into stage and when verified that that process has worked correctly, ingest into production. With this process, we also have the same data on stage and prod, which makes troubleshooting or reviewing things easier.  Since May 2021, stage has lagged behind production. The first major ingest of this collection was performed between December 2019 and April 2020. In February 2021, we began the process of re-ingesting the collection into Californica-Stage and Ursus-Stage to correct the collection name and to correct erroneous values in the date.normalized field. We later discovered 3 additional corrections to make: repository name, license, and festerizing. As of May 2021, that process is still ongoing. In late May 2021, Lisa stopped working on LA Times re-ingest because she was waiting for californica-stage to be available for large jobs (it had been slowed down / unusable due to work to delete page images for Armenian manuscripts from the repo). She picked up re-ingest again in October 2021.

After many months away from the LA Times migration work, Lisa is re-orienting herself to where she left off in May 2021 and trying to finish up all the remaining work. This has included upating her local copies of festerize script and extensive troubleshooting to resolve problems with installing an updated script and dealing with a small file that was returning 0K "successful" file instead of a CSV with data. 

Also had to research why I had left an uncommitted change in latimes3.csv on my laptop from July 2021. Looks like I had found an item that had been erroneously marked as "completed" in my CSV, but was not an image that should ever be published. It was just a scratch image (can't remember if it was just a notes page or a bad image or something like that). There was a ticket asking the Apps team to help me with deleting it. 


11/12/21 - (Lisa) Updated my local version of festerize to Festerize v0.4.2, but that did not fix the problem with latimes2_supplement.csv. Instead I used the Web form to re-festerize it. I am now ingesting it into californica-stage, and I'm surprised to see it's going very very very slowly. 

2021-10-22 - was trying to get back into working on this collection, and I started by looking at my notes about csv statuses. I saw that latimes2.csv was marked as "needing refesterizing" so I started there. Had trouble running festerize and am troubleshooting with Mark. 


* Problems Solved *

October - November 2021 - Udated version of festerize; debugging "small csv file results in 0k output from festerize" - a few weeks of troubleshooting with Mark and Kevin. 

October - November 2021 - Fester no longer can handle the same CSV files that worked in the past (3,000 rows of LA Times made the process timeout.) In order to work on the collection I had to break the CSVs into much smaller files. 

May 2021 - APPS-835 (work to delete page image files in Californica stage for Armenian manuscripts) was perceived as a process that meant we could not do any ingesting into stage. Geno and Lisa eventually went back to loading CSVs into stage, but Lisa by that time had stepped away from LA Times and it took a long time to get back to the interrupted work. 

2021-10-22 - not sure if APPS-835 is still a blocker to working on stage; i think not. APPS-835 is actually still in progress (fwiw). 

2021-05-21 - still waiting on APPS-835 ticket (delete child items on californica stage for pages ingested pre-fester workflow). cannot ingest on stage until after that work is completed. Dawn is testing the work done by Andy on APPS-835 with a new ingest of Armenian manuscripts on californica-stage.