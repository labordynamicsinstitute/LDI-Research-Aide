---
layout: default
title:  Requesting Restricted-Access Data from Authors
parent: Procedures
--- 

# Using Restricted-Access Data 
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Policy and Summary

Cases arise in which authors agree to provide data directly to the Data Editor after both parties sign a Non-Disclosure Agreement (NDA). In these cases, the author provides us with the data and the Data Editor places the files in the LDI Lab's folder on the shared L: drive in a specific folder. 

The policy of the LDI lab is that these replications are done strictly on the L: (`L:\Restricted-Access-Data`) drive. This ensures that none of the data provided under the NDA are moved and the Data Editor can keep track of and subsequently delete the data as per the agreement. 


{: .highlight}
> This process is best done by cloning repository directly to the L: drive (`L:\Restricted-Access-Data\aearep-xxxx\`) folder and then copying the resitricted data into the repository (following any instructions in the README on where the data should be located). Be diligent in ensuring that no restricted access datasets slip through the git ignore into the bitbucket repository.

We may have revisions based on the restricted data which require running additional code. For this reason, the data should be deleted before the issue is moved to "Pending Publication."

## Requesting Restricted Access Data from Authors

For cases where the author(s) have indicated on the DCAF that they can make restricted-access data available to the Data Editor privately, follow these steps:

### Setup

1. Create a subtask (issue type: `Request confidential data`) in the main Jira task. Title it "Request Restricted Access Data for AEAREP-xxx". This subtask will be `aearep-nnnn`.
1. Navigate to the following [directory](https://cornell.app.box.com/folder/144685329952) in Box: "Box/LDI Replication Lab/Office of AEA Data Editor/Restricted-Access-Data/"
2. Create a new subfolder corresponding to the main Jira issue (`aearep-xxx`). 
3. Paste the Box URL into the field `Restricted data info` -> `Restricted data Box folder` of the main Jira task `aearep-xxx`. Alternatively, paste simply the last part of the URL (a long number) into the field `Restricted data info` -> `Restricted data Box ID` of the main Jira task `aearep-xxx`, which will auto-fill the Box URL.

### Sending the request

1. Create a [file request](https://support.box.com/hc/en-us/articles/360045304813-Using-File-Request-to-get-Content-from-Anyone) within the newly created subfolder (only one file request is permitted per folder).  
2. Copy the file request link.
3. Email the authors to request that they upload the restricted-access data files to Box using the [relevant template]({{ '/docs/emails/Request-Restricted-Access-Data.html' | relative_url }}).
4. Move the Jira sub-task `aearep-nnnn` to `Request sent`

### Once data is obtained

- Box will email you about changes made to Box folder (set up these notifications)

{: .note-title }
> Special case: Author provides Dropbox or other link to download
>
> Download from the provided link, and upload into Box. Then proceed as usual.

- Run the following Bitbucket pipeline: `7-download-box-manifest`.
- Download the data in CCSS Cloud at add it to `L:\Restricted-Access-Data` in a folder titled `aearep-xxx`.

- Go into Jira ticket for `AEAREP-xxx`, under *Restricted Data Info*, edit fields:
    - Agreement signed: `NDA`, `Implicit` (or whatever is relevant!)
    - Working location of restricted data: `L:\Restricted-Access-Data\aearep-xxx`
- Move the `aearep-nnnn` subtask to `Restricted Data Received`.
- Comment in the Jira ticket *"Restricted access data added: L:\Restricted-Access-Data\aearep-xxx-"* and tag the RA currently assigned to run the code. (might be automated)

### Once case is done

After replication is complete

- case has been submitted to ScholarOne with either an `Accept` or an `Accept with Changes` AND 
- there is no post-publication reproducibility check subtask (this is usually confirmed by the Data Editor)

then

- **Delete the data from the L: drive**
- Confirm that no data is on **BioHPC**
- on **Box**,
  - Disable the File Request Link on Box
  - [Schedule the data files for expiration](https://support.box.com/hc/en-us/articles/360043696634-Delete-Files-or-Folders) (do NOT delete any agreement documents!)
  - Move the `aearep-xxxx` Box folder to "Completed".
  - Move the Jira sub-task `aearep-nnnn` to `Restricted data deleted`
  - VERIFY: the box on JIRA indicating the data has been deleted (`Restricted Data Info tab` > `Was data deleted?`) should be set to `Yes`.
  

- Respond to previous email to author (cc to `dataeditor-queue@aeapubs.org`, and be sure that the subject line includes the `AEAREP-xxxx` of the subtask).

>
> Hello Dr. *Author*,
>
> This email is confirm that we have deleted the restricted access data for "[Title]" from our workspaces. Your deposit is being moved along in the publication process.
>


- Clean up JIRA:
  - On the main case (the **last** case),
    - tick the box on JIRA indicating the data has been deleted (`Data Info tab` > "Was data deleted?")
    - Verify that the other related boxes are filled out as per the **original** case: `DataAccessReplicationTeam`, `Agreement signed`
  - Also verify that the **sub-task** related to the confidential data request (typically a sub-task of the original JIRA issue)
    - is linked (`relates to`) all the follow-up cases
    - is marked done.
    - has a copy of the email about deletion (may need pasting for old cases, where this process was not followed)
