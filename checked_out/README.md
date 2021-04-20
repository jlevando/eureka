### Items that are checked out

Project folders and CSVs that are "checked out" are being actively worked outside of the eureka repo, for example in Google sheets. These files MUST not be edits in eureka or we risk merge conflicts and overriding data provided by the editors working outside of eureka.

Procedure:
When a collection or CSV needs to be edited by a person outside of the DLP or not working in GitHub/eureka:
- Move the folder/CSV to the "checked_out" folder in eureka
- Add a README to the folder of the checked out item with info such as the link to the Google spreadsheet, the person editing, and any relevant dates
- Upload the CSV that needs to me edited to the appropriate DLP Google Team Drive location
- Refrain from any edits in the eureka CSV until editing is complete in the Google version.
- Download the Google spreadsheet as a CSV and replace the existing CSV in eureka
- Stage, commit, and push the changes to eureka upstream
- Delete the Google sheet from the Team Drive to prevent further edits
