# Daily and Weekly Tasks

## Daily Tasks

1. Check Jira if RAs need new cases. They should have at least two main Jira tasks in their queue. Refer to the [Master Replication Project](https://docs.google.com/spreadsheets/d/1Ic4UgBR3gNFvgyFigJ5SAnx0rZwlp9vu_9OV39YoXQQ/edit?pli=1#gid=1902712667) Sheet for skill levels of programs for each RA. Details on [how to assign new cases](https://github.com/AEADataEditor/LDI-Research-Aide/blob/main/Assigning_New_Cases.md).
2. Check the Data Editor email (dataeditor@aeapubs.org). Review the [details here](Data-Editor-Email-Protocol.md).
3. Check unassigned tasks and fill in Jira tickets.


## Check Unassigned Cases

### Basic Instructions

1. Go the unassigned filter in Jira.
2. In the most recent cases, fill out the following info from the DCAF attached:
    - `DCAF_Access_Restrictions`
        - (if "Yes, data can be made available privately", do additional [steps below](https://github.com/AEADataEditor/LDI-Research-Aide/blob/main/Regular_Tasks.md#if-no-manuscript))
    - `DCAF_README_checked`
    - `openICPSR Project Number` 
    - `Software Used` (from openICPSR deposit)

2. When checking the software in the openICPSR deposit, open the README and make sure it exists. If there is no README in the openICPSR deposit, make a short report.
3.  Check if the case is a Revision and mark it as such.
4. Check that there is a manuscript attached, and [add one](https://github.com/AEADataEditor/LDI-Research-Aide/blob/main/Regular_Tasks.md#if-no-manuscript) if not.

### Check if case is a revision:

Check if the case is a Revision by going to the *Other Links* tab and clicking the `JiraSearchMC`. If there are other Jira issues (not subtasks or FYIs), then it is a Revision.

 - Link Revision: Go back to the main Task you were editing, click "Link Revision" > "Is a Revision of" and then input the AEAREP number of the older task.
- Update `MCStatus` to include 'Revision' if it doesn't already have it.
- Update the `bitbucket short name` with the repository name of the previous cases.

### Additional Steps for Restricted Access Data

- Check if the case is a Revision:
    - If yes, check that we haven't already asked for the Restricted Access Data.
        - If yes, link the existing subtask to the most recent revision. If no, continue to next step.
- If not a revision, continue steps listed in [Requesting Restricted Access](Requesting_Restricted_Access_Data.md)


### If no manuscript

1. Go to "Other Links" and click on the MCEntryURL.
2. After logging in, click "Review". Ctrl+F and search for the Manuscript Number.
3. Once you find the manuscript, go to the Action section, "View Proof", download the PDF of the manuscript.
4. Attach the PDF to the Jira ticket.


### Weekly Tasks

1. Timesheet entry