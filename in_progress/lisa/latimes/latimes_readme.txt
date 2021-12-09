This readme was last updated by Lisa McAulay on 2021-12-09.

The LA Times Collection is being migrated by Lisa McAulay with assistance from Geno Sanchez. At present, Lisa has ingested standardized metadata CSVs and images for all items that were completed as of November 2019 (Specific date not certain yet - can't find precise evidence; see below). The number of items this comprises is between 16,892 and 16,899. The current phase of work (November 2021 - December 2021) is ingesting all the items that have been edited since 11/01/19 and have a status of either "completed" or "pending" as of 12/02/21. This group of materials will be re-ingested and have their visibility updated to "public" and will be co-members of the LA Times collection and the OpenUCLA collection.

History of This Migration
November 2019 - April 2020 - The first major ingest of this collection was performed.

February 2021 - November 2021 - A major data cleanup of those items. Lisa re-festerized and re-ingesting the full collection in order to correct the following values: 
- collection name
- non compliant date.normalized values
- repository name
- license
- festerizing

November 2021 - December 2021 - Lisa is working on updating the collection to release "newly" completed items (Items that had their metadata edited and completed since the original export). 

Current Actions:
Dedupe latimes_openucla_update_2021_12_02.csv that exist in latimes_pending_batch[1-6].csv. (done)
Related - have Geno and Dawn reload all items that belong to OpenUCLA collections.

latimes_openucla_update_2021_12_02.csv (currently 4,707 rows (+ 1 header row)



Date of Original Export - I think it was possibly 11/01/19 or sometime slightly earlier. 
Evidences:

The first time LA Times was loaded to eureka was 11/14/19. 
Additionally, Jira ticket to migrate LA Times was created on 11/15/19. 
There are some items that were edited on 11/07/19 and are listed as 'Completed' in the original export. (Possibly an edit was made after they were marked as 'Completed'?)
Many items that were last edited on 11/08/19 are listed as 'Pending' in the original export, but show listed as 'Completed' in DLCS now. 
I found several items with current DLCS status = "Completed" that were last edited on 11/01/19 and that are in my group of items that had a status of "pending" in the original export (examples: ark:/21198/zz002dcn47, also ark:/21198/zz002dcn68, ark:/21198/zz002dcn7s, ark:/21198/zz002df48z).
Records that were edited between 10/14/19 and 10/31/19 all have the status "Completed" in the original export. While this isn't complete proof, it indicates that if I were to use Ashton's export of all items that were edited since 11/1/2019 and have status = completed and say those items all should get assigned to be part of OpenUCLA and need to be updated and published openly through Samvera, that would be an accurate portrayal of items that were worked on in the OpenUCLA era and that have changed in some way since the original CSVs were imported. So it is accurate to assign them to OpenUCLA and it is also appropriate to update them in Samvera. The next step is cleaning up all the CSVs so that each record only appears once. 

I did find a record that was listed as having been edited on 11/13/19 that was marked as 'Completed' in the original export (is part of latimes6.csv) - not sure what edit was made. Item is ark:/21198/zz002dhxb0. A quick review of the latimes6.csv metadata and the DLCS records showed them to be the same, but it's possible there's a minor difference that I didn't catch. This requires more review. It's possible this item was not one of the "pending" items when the original export occurred and that it was edited for a different reason on 11/13/19 (as opposed to the status being changed from pending to completed). 

Current Problems (as of 11/29/21): (documented in APPS-1195 and APPS-1207)
- On both Stage and Prod -- OpenUCLA collection is broken(ish)
- On Stage, items do not update their visibility status 
^^^ Lisa is working with Andy W and Parinita to resolve these problems. I (Lisa) ran some test imports on californica-dev on 12/3 and 12/4 and these imports were designed to have the same problems that I had that resulted in breaking the OpenUCLA collection so that Andy and Parinita could test their potential fix. As far as I can tell the fix did not work. Will bring it to their attention on 12/6/21. OpenUCLA collection does still exist after the bad import, but clicking on it in search results leads to stack trace page. Additionally, the items in the ingest did not update from "private" to "public". 

12/05/21 - Testing on californica-DEV is in progress to deal with the "bad data csv breaks existing collections" problem. Lisa has results to share with Parinita and Andy. ON STAGE - Made another mistake -- accidentally loaded the "bad data csv" to californica-stage when doing the test of dev (just clicked the wrong file to upload into the import csv). Now redoing work on californica-stage by 1) reloading openUCLA collection (done) 2) reloading latimes_pending_batch1.csv. On PROD working on loading latimes_pending batches: now ingesting latimes_pending_batch5.csv. Preparing latimes_pending_batch6.csv
 


12/02/21 - Reloading latimes_pending_batch3.csv into stage (without OpenUCLA collection in Parent ARK column) and Reloading openucla_collection.csv into stage to reestablish it. 

11/24/21 - Reloading latimes_pending_batch3.csv into stage and simultaneously loading into prod. 11/25/21 - Results of test failed. Batch3 loaded again into californica stage but items remained marked as "private". And batch3 into production somehow ruined the OpenUCLA collection. Instead of being listed as "OpenUCLA Collection" it is now "Collection ARK:"

11/24/21 - Testing now with latimes_pending_batch4.csv on stage. Same results as latimes_pending_batch3.csv - items remained marked as private.


To do (written 2021-11-18): 
1. accidentally deleted latimes2-9.csv, so I need to restore from git.
2. Need to request a custom export to capture all pendings
Custom export would be export where collection = la times and status = completed or pending and edit date = Entered APPS team ticket. It won't be looked at until after Thanksgiving, though, so I will proceed with some testing in the meantime.

Edited Items
1 -- tested latimes_edits_2021_11_19.csv -- this was an item that had been edited in DLCS since the CSVs were created. Lisa replicated the edits from the DLCS staff screen into the CSV and loaded the 1 row CSV into stage and production 11/19/21. Will need to develop a plan for going through all of these edits, but for now I'm going to put that off until I get all the items that have status "pending" into the repos. 

Pending Status (Group 1)
2 -- loaded latimes_pending_batch1.csv to californica-stage 11/19/21, ingesting to prod on 11/20/21. This process worked and added the first LA Times item to the OpenUCLA project. the latimes_pending.csv contains all the items that had the status "pending" when the original export from DLCS was performed. I have gone through 11 of these items and all 11 have the same characteristics: in DLCS these items are now marked as 'completed', these items are also not in the latimes_photo_pending.csv. My guess is that these are items that were changed from 'pending' to 'completed' sometime before the latimes_photo_pending csv was created. I created a new latimes_pending_batch2.csv file to contain the next 10 items that I verified are now completed and also verified they are not in the latimes_photo_pending file. 

Workflow
1. select items from latimes_pending.csv (breaking into batches)
2. Add OpenUCLA ARK to Parent ARK column
3. check DLCS to confirm the item is now "completed" and that edit date is not recent (most are showing up as having been edited in November 2019)
4. check the latimes_photo_pending.csv (this file remains a bit of a mystery. Not sure how items are listed as "pending" in my original export and yet not in this "pending" file. probably we weren't tracking the idea of "pending" in (looks like that latimes_photo_pending.csv was added to the eureka repository in the openucla folder (now no longer exists in in_progress) on 01/27/21 by Dawn -- I can't remember the details of what was going on; nor is the commit message very detailed)
4a. When an item has been edited more recently than November 2019, check the new export from ashton of items that are completed and have been edited since 11/1/2019. If in that file then add OpenUCLA ARK to parent ARk field in "from ashton" csv and delete row from pending batch. This will mean we only have that record in one CSV and that it has been marked as part of OpenUCLA, but it will not be updated/published until I get to that larger file.  
5. I am changing the status to "2" and "Completed" only after verifying that row is ready for ingest. (thus I'm leaving a record of where I left off if I can't prep a CSV all at one time).


Additional notes:
As of 11/20/21, the number of "Completed" LA Times items according to DLCS = 19,599; Number of published items in Samvera production = 16,892. Difference of 2,707. Right now I only have 960 rows (across 4 CSV files) that might account for that difference. So clearly, I've got more sleuthing to do. 

Items that have been edited since the data that I have. -- Request export by ARK
21198/zz002cxmn8 - my export is from 2019, but the last edit date was 10/02/20
21198/zz002cxmps - my export is from 2019, but the last edit date was 10/02/20 
21198/zz002cxmsb - my export is from 2019, but the last edit date was 03/11/20 
21198/zz002cxmtv - my export is from 2019, but the last edit date was 03/11/20 

Process:
- festerize on local computer
- ingest newly festerized csv to cal-stage
- run jenkins solr synch on stage 
- check an item for accuracy (QC) (ursus-stage)
- ingest to cal-prod
- run jenkins solr synch on prod (digital)
- check an item for accuracy



* Concerns *

- Accurately completing an update to the LA Times collection. Adding 589 new items from DLCS with status = pending. 


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
latimes5.csv now only contains the files that are "completed". created 3 new files: latimes5_pending.csv, latimes5_needs_review.csv, latimes5_imported.csv
latimes6.csv now only contains the files that are "completed". created 4 new files: latimes6_pending.csv, latimes6_needs_review.csv, latimes6_imported.csv
latimes7.csv now only contains the files that are "completed". created 4 new files: latimes7_pending.csv, latimes7_needs_review.csv, latimes7_in_progress.csv, latimes7_imported.csv
latimes7_failed_new.csv only contains files that are "completed". 
latimes8.csv now only contains files that are "completed". created 1 new file: latimes8_imported.csv

New Subdirectory
latimes_noncompleted: contains merged csvs based on status, each csv contains a new column that identifies what the source csv file was for each item
in_progress.csv created
imported.csv created

Goal -- once I get done separating all the files out I might move the non completed CSVs into a subdirectory. The main idea being that "completed" items should be the latimes1-latimes8 csvs and that they're stable and solid. And then the latimes with different status might need to be combined (maybe with a new column added to state which csv they were originally part of).

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

Accomplishing this "behind the scenes" work served the purpose of catching the LA Times collection back up to our standard workflow, which is ingest CSVs into stage and when verified that that process has worked correctly, ingest into production. With this process, we also have the same data on stage and prod, which makes troubleshooting or reviewing things easier.  Since May 2021, stage has lagged behind production. In late May 2021, Lisa stopped working on LA Times re-ingest because she was waiting for californica-stage to be available for large jobs (it had been slowed down / unusable due to work to delete page images for Armenian manuscripts from the repo). She picked up re-ingest again in October 2021.

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

Tracking Repository of CSVs

On 2021-12-07 I am going to delete the following files from the LA Times eureka repository:
Current location of these files is: eureka/in_progress/lisa/latimes/latimes_noncompleted
- latimes_imported.csv 
- 
Descriptions of files and rationales
latimes_imported.csv and latimes_in_progress.csv include all items from the LA Times collection in DLCS that had the status of "Imported" or "In Progress" respectively when the original export was performed. These items have been ingested into Californica in Stage and Prod, but marked as "Private." These items do not need to be tracked because they will need to be re-exported when they have been edited or completed. This data is either outdated (because metadata has been added to them) or not useful because we don't need to preserve this data for future use because we want it to be updated. 
