Minasian Migration Progress and Workflow Readme
Written by Lisa McAulay
Updated 2021-12-21

** Current Status **
Lisa is re-orienting herself to the Minasian workflow and status. 

Reviewing tickets from student workers who were reviewing previous bathes. Next ticket for review (ideally on 12/22/21 (to keep at it everyday)): https://jira.library.ucla.edu/browse/LEG-310

See notes in "Previous Status" which reference that I was picking up work again in June 2021. I seemed determined to get back into the swing of things, but then I clearly stopped for another 6 months. I remember during some of the DLCS migration meetings that I decided that I could only work on one migration project at a time because each challenge that remained took my full daily attention to keep moving it forward and getting help from others. And if I switched which challenge I was working on, then I would get disoriented and the "switching cost" of remembering where I left off was too great. 

** Previous Status **
Last updated 2021-06-09
Lisa is preparing Batch 12

I took a long hiatus from working on this collection from October 2020 until June 2021. I am really curious why I stopped working on Minasian. I assume I just got fed up or distracted or out of practice. Or something came up that interrupted me, and I thought I would get back to it and did not. I will try to prevent that from happening again. 

I returned to the work because a patron had an inquiry about a manuscript that I had already migrated and I noticed that the entire TOC was not displaying. I realized I needed to re-ingest the CSV into californica because I had used |~| to separate TOC instead of <br/><br/>

See also 'tracking_documents/minasian_status.txt'



** Principles **
We are starting with the manuscripts that contain information about conceptual works to make sure the workflow for these items is fully worked out. The other manuscripts should not be as complicated. These TOC-containing manuscripts are only about 40+ of the total digitized manuscripts (circa 322).

Pre-work -- Completed already. IMPORTANT, this work would have to be REDONE if you want to start from the source export files -- I hope we do not have to do that.

Here is the pre-work that I did:
Take the file from Ashton's script's output named `minasian_digitized_works.csv` and bring it into OpenRefine. Using OpenRefine text facet on the column for description.tableOfContents. Select all rows that are blank, export those rows as minasian_digitized_mss_no_toc.csv. Star all the rows that are blank then facet by star and select only un-starred rows and export those rows as minasian_digitized_mss_with_toc.csv.

---- CURRENT WORKFLOW (ASSUMES PRE-WORK REMAINS INTACT)


1. Create a new batch folder inside \eureka\in_progress\minasian and name it with the next increment for the batch number.

2. Create a new CSV inside that batch folder named minasian_batchX_works.csv. Copy a header row from a previous batch and paste into this new csv.

3. Select manuscripts for the batch and update the tracking documents. Look in  eureka\in_progress\lisa\minasian\tracking_documents and open `minasian_digitized_mss_with_toc_2020_06_20`. Select any number of rows for migration working from the top of the document. 

4. Copy the row for each work you plan to migrate into `minasian_digitized_works_ingested_2020_06_20`. This is a CSV for reference only and we may stop using it eventually. 

5. Copy all the work rows that you selected in step 3 into this file. 

6. Delete the rows you copied from the `minasian_digitized_mss_with_toc_2020_06_09`. This CSV acts as a "To do" list and will get smaller with every batch that is migrated.

7. Record which manuscripts you are including in your batch in the `minasian_batch_log`.

8. Find all relevant CSVs inside \minasian_pages for the pages of the manuscripts in the batch

9. Copy the files into the batch folder.

10. Delete the pages CSVs from the \minasian_pages (on Lisa's local machine (not shared in GitHub because it is too big and breaks the system) directory after copying to the batch directory (we don't need to keep 2 copies)

11. Enter value in text direction field in the works.csv (note on 1/21/21, this may already be correct now? Double check)

12. Change the Filename path in each of the pages CSVs to correct the path (it is wrong in DLCS). You need to change "Minasian" at the beginning of the path to "minasian" lower case. You need to convert the 1147_#### to use the new file hierarchy. Example: "minasian/masters/1147_0160/0160_0001.tif" should be edited to "minasian/masters/0160/0160_0001.tif"

13. In the description.tableOfContents column, change ****|~| to <br/><br/>****** (we changed the way Californica ingests table of contents field after Ashton wrote her script; now we use break tags instead of multi-values)

14. Run bucketeer for all the pages.csv files (You have to be on VPN, go https://bucketeer.library.ucla.edu/ and select the menu item at the top "CSV Upload")

15. Festerize the works.csv. Once you have festerize 

16. Festerize the pages.csv

17. Upload the works.csv to Californica-stage

18. Run Jenkins job to synch solr from californica-stage to Ursus-stage

19. Review each work on ursus-stage and select a representative image to serve as the thumbnail. open the pages CSV to retrieve the IIIF Access URL for that image.

20. Add a column in the works.csv names "IIIF Access URL" (note : if you try to festerize this csv again after adding this column it will fail. you will need to make an edit to the name of the column and then rerun the festerize script. then before uploading the new works csv, change the column header back)

21. Most (if not all) of the Minasian manuscripts start on the inside cover, which throws off the 2-up view in teh manuscript viewer because it expects to start on a single recto image (either the cover or an inside recto page). 

----------------------------

1. `minasian_digitized_works_updated_2020_05_20.csv` was created by Ashton to take all the intellectual works' titles from the hierarchy in DLCS and put it into a column for the manuscript volume. She did this work on 2020-05-20.

2. using the `minasian_digitized_works_updated_2020_05_20` select manuscript rows for ingest and cut the rows and put them in `minasian_digitized_works_ingested_2020_05_20`

3. gradually, the first file will have fewer rows and the second file will have more rows. The first file will be rows for manuscript ("works" in californica) to be migrated and the second file will be manuscripts that have been migrated.


Strange things I've found along the way

1. A Pages Csv with no data (21198zz000stfd3) - was not sure why at first. It turned out to be an item with no children (either conceptual works or pages, so it shouldn't have qualified to be in my workflow. I kicked it out of the batch and moved on. 

2. I included Manuscript 151 in Batch 10 based on believing that it had a table of contents, but in the current instance it does not (06/09/21). I assume I discovered a data error when i was working on this in September 2020, but I did not make notes about what corrections I made. I will assume that I did the correct thing and this manuscript initially appeared to have table of contents metadata, but in the end did not. I kept it in Batch 10. I see that Batch 11 has a similar discrepancy. I am assuming that there was a data error in the DLCS records (a data entry person selected "work" instead of "page" when creating a page record (i could be wrong)). 
 
*Status*
2021-06-08 - Batch 7 - updated item spearators within Table of Contents from "|~|" to "<br/><br/>"
2021-06-09 - Note to self -- looks like Batch 1 has an item that uses table of contents, Batches 2-6 do not have manuscripts with Tables of Contents, Batches 7 through 9 do; Batch 10 has toc for 4 of 5 manuscripts; Batch 11 has toc for 6 out of 10 manuscripts. 

About the files

minasian_digitized_mss_with_toc_2020_06_09 was generated using Ashton's minasian_processing.csv. Lisa ran the script on her machine on 06-09-20. Then Lisa filtered the output using OpenRefine to export 2 csvs for the digitized manuscripts: one CSV for works that do not have conceptual works metadata and those that do. Separating the works into these two groups made it easier to find digitized manuscripts that had TOC metadata so that we could test the script and QA the workflow. Ashton will be sending Lisa an updated zip with revised output since there was a correction to make on the script after Lisa reviewed on 6/9/20. This CSV lists all the digitized manuscripts that have information about the conceptual works inserted as Description.toc

Manuscript-Level Notes

*Mss 151, (ark:/21198/zz000stfvt), batch 10* - (Revision completed 2021-12-21)
Notes on this Jira ticket from Patricia helped me go back and make revisions to the manuscript pages: https://jira.library.ucla.edu/browse/LEG-309.

On 12-21-2021, I removed the rows from the pages csv for this manuscript for pages with the filenames 1147_0151_0317.tif 1147_0151_0318.tif because they were nearly the same as 1147_0151_0318.tif and 1147_0151_0319.tif. Please note that all four images are unsatisfactory. All four are sections of a piece of paper, but not the entirety. writing clearly is cut off and no other images show the matching pieces. I suspect maybe auto-cropping to separate page spreads resulted in a mistake. These erroneous images should be replaced with better images when time allows. These pages do seem to be tipped in notes that are not contemporary to the rest of the document. 

Additionally, I placed the inside front cover image at the end of the manuscript so that the book-viewer option shows a page spread. 

Batch 10 (https://jira.library.ucla.edu/browse/LEG-309) 
Mss 151 (ark:/21198/zz000stfvt) -- has some weird images at the end. Patricia reviewed and thought they were duplicates. Lisa working on fixing now by moving the cover image to the end and removing duplicates from the pages CSV and then refesterizing and reingesting. (12/21/21) Mistakenly thought I needed to reingest into Californica, but with no edits to the manuscript metadata there was no need. The refesterization updated the content available to the Universal Viewer in both stage and prod. 


