---
layout: default
title:  Requesting Restricted-Access Data from Authors
--- 

For cases where the author(s) have indicated on the DCAF that they can make restricted-access data available to the Data Editor privately, follow these steps:

1. Create a subtask (issue type: confidential data) in the main Jira task. Title it "Request Restricted Access Data for AEAREP-xxx". This subtask will be aearep-nnnn
1. Navigate to the following [directory](https://cornell.app.box.com/folder/144685329952) in Box: "Box/LDI Replication Lab/Office of AEA Data Editor/Restricted-Access-Data/"
2. Create a new subfolder corresponding to the main Jira issue (`aearep-xxx`). 
3. Create a [file request](https://support.box.com/hc/en-us/articles/360045304813-Using-File-Request-to-get-Content-from-Anyone) within the newly created subfolder (only one file request is permitted per folder).  
4. Copy the file request link.
5. Email the authors to request that they upload the restricted-access data files to Box using the [relevant template](/LDI-Research-Aide/emails/Email-Templates/#request-restricted-access-data)

### Once data is obtained

- Box will email you about changes made to Box folder (set up these notifications)

{: .note-title }
> Special case: Author provides Dropbox or other link to download
>
> Download from the provided link, and upload into Box. Then proceed as usual.

- Download the data in CCSS Cloud at add it to `L:/Restricted-Access-Data` in a folder titled `aearep-xxx-nda_Implicit`

- Go into Jira ticket for AEAREP-xxx, under *Data Info*, edit fields:
    - Agreement signed: `NDA`, `Implicit`
    - Working location of restricted data: `L:\Restricted-Access-Data\aearep-xxx-nda_Implicit`
- Comment in the Jira ticket *"Restricted access data added: L:\Restricted-Access-Data\aearep-xxx-nda_Implicit"* and tag the RA currently assigned to run the code.

### Once case is done

After replication is complete

- case is in *Pending openICPSR Changes* or *Assess openICPSR Changes* and
- there is no post-publication reproducibility check subtask (this is usually confirmed by the Data Editor)

then

- **Delete the data from the L: drive and Box**, disable the File Request Link on Box, and move the `aearep-xxxx` Box folder to "Completed".
- Respond to previous email to author:

>
> Hello Dr. *Author*,
>
> This email is confirm that we have deleted the restricted access data for "[Title]" from our workspaces. Your deposit is being moved along in the publication process.
>


- Check the box on JIRA indicating the data has been deleted (`Data Info tab` > "Was data deleted?")
