# Assigning New Cases

Each morning JIRA sends an automated email detailing the current unassigned tasks for choice. 
To view this on JIRA, navigate to the Filters dropdown and choose "Unassigned tasks for choice."

New cases are most commonly indicated by "Rev.0" on the end of the summary while revisions are indicated by a "Rev.1". It can be verified whether or not an issue is a revision by searching the manuscript identifier in JIRA to see if there are any previous issues corresponding to the identifier (Note: After linking previous issue to the revised issue, transition the previous issue to "Done"). Revisions should most often be assigned to the RA that replicated the original request. Any new cases not chosen by RA's will be assigned in the following manner.

Select the issue and take a look at the README. Which software(s) is used by the authors and do they provide the OpenICPSR project number? 

Open the "Replication Project Resumes" spreadsheet and see which RA's have experience with the software used in the paper. Next, open another JIRA tab and navigae to the Dashboards dropdown and choose "Assignments." Here we can take a closer look at how much each RA is working on at the moment. Attempt to choose an assignee who has the bandwith to complete the case in a reasonable time frame and who has the requisite knowledge of the softwares used. 

If the authors have provided the OpenICPSR project number in the README, populate that number in the "OpenICPSR Project Number" field in JIRA. A script automatically alters the Code provenance field to account for the ICPSR link to that project. If the authors have not provided this number in the README, click the link in the Code provenance field on JIRA. This will bring you to the search field on OpenICPSR. Pick out a unique set of words from the title of the manuscript and search for that paper. When the paper is found, click on "ADMIN" to view the project. From there you will find the project number which can be populated in the manner described previously. 

While on the OpenICPSR project page, the next step is to give the RA access to the project. Copy the RA's email from the "Replication Project Resumes" spreadsheat. Click "Share Project" in ICPSR and paste the email. Additionally, choose to allow access to download. This will give the RA permission to view and download the necessary replication materials.

One final step while in OpenICPSR is to check to see if authors have "submitted" the project on openICPSR. If the status is not already "SUBMITTED" then post a note in the Project Communication Log asking them to choose "Change status", then submit.

**Note:** 
For R&R papers ("Invitation to review..."), click on the "Agree" link in the Description (be sure to "open in a new tab"). This sends a notification to the editors that we have agreed to review the manuscript (but generates the acceptance email, which will need to be deleted from "Unassigned").


Finally, transition the issue from "Open" to "Assigned" in JIRA and leave a comment on the project. 



