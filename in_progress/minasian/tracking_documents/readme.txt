Minasian Migration Workflow Readme
Written by Lisa McAulay
Updated 2020-06-11

Principles -- We are starting with the manuscripts that contain information about conceptual works to make sure the workflow for these items is fully worked out. The other manuscripts should not be as complicated. These are only about 40+ of the total digitized manuscripts (circa 322).

Pre-work (that hopefully after 2020-06-20 does not need to be redone)
Take the file from Ashton's script's output named `minasian_digitized_works.csv` and bring it into OpenRefine. Using OpenRefine text facet on the column for description.tableOfContents. Select all rows that are blank, export those rows as minasian_digitized_mss_no_toc.csv. Star all the rows that are blank then facet by star and select only un-starred rows and export those rows as minasian_digitized_mss_with_toc.csv.



1. Start from in_progress\minasian\tracking_documents

2. Open `minasian_digitized_mss_with_toc_2020_06_20`. Select any number of rows for migration working from the top of the document. 

3. Copy the row for each work you plan to migrate into `minasian_digitized_works_ingested_2020_06_20`. This is a CSV for reference only and we may stop using it eventually. 

4. Delete the row you copied from the `minasian_digitized_mss_with_toc_2020_06_09`. This CSV will act as a "To do" list and will get smaller with every batch that is migrated.

5. Record which manuscripts you are including in your batch in the `minasian_batch_log`

6. Create a new batch folder inside \eureka\in_progress\minasian

7. Create a new CSV inside that batch folder named minasian_batchX_works.csv

8. Find all relevant CSVs inside \minasian_processing for the pages of the manuscripts in the batch

9. Copy the files into the batch folder.

10. Enter value in text direction field in the works.csv

11. Move the pages CSVs in the \minasian_processing directory into the \ingested folder

12. Change the Filename path to correct the path (it is wrong in DLCS).

12. Run bucketeer for all the pages.csv files

13. Festerize the works.csv

14. Festerize the pages.csv

15. Upload the works.csv to Californica-stage


`minasian_digitized_works_updated_2020_05_20.csv` was created by Ashton to take all the intellectual works titles from the hierarchy in DLCS and put it into a column for the manuscript volume. She did this work on 2020-05-20.

2. using the `minasian_digitized_works_updated_2020_05_20` select manuscript rows for ingest and cut the rows and put them in `minasian_digitized_works_ingested_2020_05_20`

3. gradually, the first file will have fewer rows and the second file will have more rows. The first file will be rows for manuscript ("works" in californica) to be migrated and the second file will be manuscripts that have been migrated.

 
About the files

minasian_digitized_mss_with_toc_2020_06_09 was generated using Ashton's minasian_processing.csv. Lisa ran the script on her machine on 06-09-20. Then Lisa filtered the output using OpenRefine to export 2 csvs for the digitized manuscripts: one CSV for works that do not have conceptual works metadata and those that do. Separating the works into these two groups made it easier to find digitized manuscripts that had TOC metadata so that we could test the script and QA the workflow. Ashton will be sending Lisa an updated zip with revised output since there was a correction to make on the script after Lisa reviewed on 6/9/20. This CSV lists all the digitized manuscripts that have information about the conceptual works inserted as Description.toc