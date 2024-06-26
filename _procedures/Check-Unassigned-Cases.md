# Check Unassigned Cases

## Basic Instructions

1. Go the unassigned filter in Jira (*Dashboards* > *Admin Dashboard* > *AEA tasks by Assignee* section > scroll down to "*Unassigned*").
2. In the most recent cases, fill out the following info from the DCAF attached:
    - `DCAF_Access_Restrictions`
        - if "Yes, data can be made available privately", do additional [steps](Requesting_Restricted_Access_Data.md)
    - `DCAF_README_checked`
    - `openICPSR Project Number` 
    - `Software Used` (from openICPSR deposit)

2. When checking the software in the openICPSR deposit, open the README and make sure it exists. If there is no README in the openICPSR deposit or the deposit is empty, make a [short report](Writing-Short-Report.md).
3.  Check if the case is a Revision and mark it as such.
4. Check that there is a manuscript attached, and add one if not (instructions at the bottom of this page).

**Note:** 
For R&R papers ("Invitation to review...")

- Go to `MCEntryURL` in the ""Other Links" section
- Log in to ScholarOne and click Review.
- Navigate to the link that says "Invitations"
- Click "Accept invitation and continue review" (I actually don't remember the exact wording. We currently don't have any invitations. Edit later)
- Then close out the tab.

## Non-standard unassigned cases

- Jira ticket titled ["Contact form submission"](Contact-Form-Submission.md)

## Check if case is a revision:

Check if the case is a Revision by going to the *Other Links* tab and clicking the `JiraSearchMC`. If there are other Jira issues (not subtasks or FYIs), then it is a Revision.

 - Link Revision: Go back to the main Task you were editing, click "Link issue" > "Is a Revision of" and then input the AEAREP number of the older task.
- Update `MCStatus` to include 'Revision' if it doesn't already have it.
- Update the `bitbucket short name` with the repository name of the previous cases.

Check if the older Jira ticket had restricted access data (i.e. `Working location of restricted data` was filled out). If yes:

- Link Issue, select type "relates to" and add the aearep-xxx for the subtask "Request Restricted Access Data for AEAREP-nnn"
- Fill out `Working location of restricted data`with the same L drive path
- Fill out `Agreement Signed` to match the older Jira ticket

## Additional Steps for Restricted Access Data

- Check if the case is a Revision:
    - If yes, check that we haven't already asked for the Restricted Access Data.
        - If yes, link the existing subtask to the most recent revision.
        - If no, continue to next step.
- If not a revision, continue steps listed in [Requesting Restricted Access](Requesting_Restricted_Access_Data.md)


## If no manuscript in Jira ticket

1. Go to "Other Links" and click on the MCEntryURL.
2. After logging in, click "Review". Ctrl+F and search for the Manuscript Number.
3. Once you find the manuscript, go to the Action section, "View Proof", download the PDF of the manuscript.
4. Attach the PDF to the Jira ticket.