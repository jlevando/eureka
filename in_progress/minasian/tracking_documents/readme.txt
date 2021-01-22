Minasian Migration Workflow Readme
Written by Lisa McAulay
Updated 2021-01-21

Principles -- We are starting with the manuscripts that contain information about conceptual works to make sure the workflow for these items is fully worked out. The other manuscripts should not be as complicated. These are only about 40+ of the total digitized manuscripts (circa 322).

Pre-work -- Completed already. IMPORTANT, this work would have to be redone if you want to start from the source export files -- I hope we do not have to do that.

Take the file from Ashton's script's output named `minasian_digitized_works.csv` and bring it into OpenRefine. Using OpenRefine text facet on the column for description.tableOfContents. Select all rows that are blank, export those rows as minasian_digitized_mss_no_toc.csv. Star all the rows that are blank then facet by star and select only un-starred rows and export those rows as minasian_digitized_mss_with_toc.csv.



1. Start from in_progress\minasian\tracking_documents

2. Open `minasian_digitized_mss_with_toc_2020_06_20`. Select any number of rows for migration working from the top of the document. 

3. Copy the row for each work you plan to migrate into `minasian_digitized_works_ingested_2020_06_20`. This is a CSV for reference only and we may stop using it eventually. 

4. Delete the row you copied from the `minasian_digitized_mss_with_toc_2020_06_09`. This CSV will act as a "To do" list and will get smaller with every batch that is migrated.

5. Record which manuscripts you are including in your batch in the `minasian_batch_log`

6. Create a new batch folder inside \eureka\in_progress\minasian

7. Create a new CSV inside that batch folder named minasian_batchX_works.csv. Copy a header row from a previous batch, and then copy all the rows that you selected in step 3 into this file. 

8. Find all relevant CSVs inside \minasian_pages for the pages of the manuscripts in the batch

9. Copy the files into the batch folder.

10. Delete the pages CSVs from the \minasian_pages (on Lisa's local machine (not shared in GitHub because it is too big and breaks the system) directory after copying to the batch directory (we don't need to keep 2 copies)

11. Enter value in text direction field in the works.csv (note on 1/21/21, this may already be correct now? Double check)

12. Change the Filename path to correct the path (it is wrong in DLCS). You need to change "Minasian" at the beginning of the path to "minasian" lower case. You need to convert the 1147_#### to use the new file hierarchy. Example: "minasian/masters/1147_0160/0160_0001.tif" should be edited to "minasian/masters/0160/0160_0001.tif"

13. In the description.tableOfContents column, change |~| to <br/><br/> (we changed the way Californica ingests table of contents field after Ashton wrote her script; now we use break tags instead of multi-values)

14. Run bucketeer for all the pages.csv files (You have to be on VPN, go https://bucketeer.library.ucla.edu/ and select the menu item at the top "CSV Upload")

15. Festerize the works.csv. Once you have festerize 

16. Festerize the pages.csv

17. Upload the works.csv to Californica-stage

18. Review each work on ursus-stage and select a representative image to serve as the thumbnail. open the pages CSV to retrieve the IIIF Access URL for that image.

19. Add a column in the works.csv names "IIIF Access URL" (note : if you try to festerize this csv again after adding this column it will fail. you will need to make an edit to the name of the column and then rerun the festerize script. then before uploading the new works csv, change the column header back)

20. Most (if not all) of the Minasian manuscripts start on the inside cover, which throws off the 2-up view in teh manuscript viewer because it expects to start on a single recto image (either the cover or an inside recto page). 

----------------------------

`minasian_digitized_works_updated_2020_05_20.csv` was created by Ashton to take all the intellectual works titles from the hierarchy in DLCS and put it into a column for the manuscript volume. She did this work on 2020-05-20.

2. using the `minasian_digitized_works_updated_2020_05_20` select manuscript rows for ingest and cut the rows and put them in `minasian_digitized_works_ingested_2020_05_20`

3. gradually, the first file will have fewer rows and the second file will have more rows. The first file will be rows for manuscript ("works" in californica) to be migrated and the second file will be manuscripts that have been migrated.


Strange things I've found along the way

1. A Pages Csv with no data (21198zz000stfd3) - not sure why. It turned out to be an item with no children (either conceptual works or pages, so it shouldn't have qualified to be in my workflow. I kicked it out of the batch and moved on. 
 
About the files

minasian_digitized_mss_with_toc_2020_06_09 was generated using Ashton's minasian_processing.csv. Lisa ran the script on her machine on 06-09-20. Then Lisa filtered the output using OpenRefine to export 2 csvs for the digitized manuscripts: one CSV for works that do not have conceptual works metadata and those that do. Separating the works into these two groups made it easier to find digitized manuscripts that had TOC metadata so that we could test the script and QA the workflow. Ashton will be sending Lisa an updated zip with revised output since there was a correction to make on the script after Lisa reviewed on 6/9/20. This CSV lists all the digitized manuscripts that have information about the conceptual works inserted as Description.toc