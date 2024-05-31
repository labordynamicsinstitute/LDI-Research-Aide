# Requesting Restricted-Access Data from Authors

For cases where the author(s) have indicated on the DCAF that they can make restricted-access data available to the Data Editor privately, follow these steps:

1. Create a subtask (issue type: confidential data) in the main Jira task. Title it "Request Restricted Access Data for AEAREP-xxx". This subtask will be aearep-nnnn
1. Navigate to the following [directory](https://cornell.app.box.com/folder/144685329952) in Box: "Box/LDI Replication Lab/Office of AEA Data Editor/Restricted-Access-Data/"
2. Create a new subfolder corresponding to the main Jira issue (`aearep-xxx`). 
3. Create a [file request](https://support.box.com/hc/en-us/articles/360045304813-Using-File-Request-to-get-Content-from-Anyone) within the newly created subfolder (only one file request is permitted per folder).  
4. Copy the file request link.
5. Email the authors to request that they upload the restricted-access data files to Box using the template below.

Subject Line:
> Request for Restricted Access Data (AEAREP-nnn)

Send it to authors, cc to `dataeditor-queue@aeapubs.org` and  `dataeditor@aeapubs.org`.

> Dr. *Author*,
> 
> We received a request to conduct the AEA reproducibility check for your manuscript entitled "X." On the Data and Code Availability form which you submitted it was indicated that the data can be made available to the Data Editor privately. Would it be possible for you to provide the restricted-access data so that we may proceed to verify the reproducibility of the entire replication package? The data would not be published, and would be deleted by us once we have completed our process. Our preferred sharing method is a Box File Request (specific to your manuscript), the link for which can be found below, but can alternatively happen via Dropbox or similar means, and should be compliant with your data use agreement.
> 
> Box File Request (navigate to the link below and upload the file(s)):
> [Insert Box File Request Link Here]
>
> We note that all data sharing with the Data Editor should be in compliance with all applicable data use agreements. Please check before sharing.
> 
> Please note that the replicator will ignore any code or public data sent via Box. For more information on what to share with the Data Editor:
https://www.aeaweb.org/journals/data/faq#confidential
https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit.html#structure-in-the-presence-of-confidential-unpublished-data
> 
> For more guidance on how to legally and practically share restricted data with the Data Editor:
> 
> https://aeadataeditor.github.io/aea-de-guidance/sharing-restricted-data.html
> 
> If you have any questions please do not hesitate to ask.
> Thank you!

### Once data is obtained

- Box will email you about changes made to Box folder (set up these notifications)

- Download the data in CCSS Cloud at add it to `L:/Restricted-Access-Data` in a folder titled `aearep-xxx-nda_Implicit`

- Go into Jira ticket for AEAREP-xxx, under *Data Info*, edit fields:
    - Agreement signed: `NDA`, `Implicit`
    - Working location of restricted data: `L:\Restricted-Access-Data\aearep-xxx-nda_Implicit`
- Comment in the Jira ticket *"Restricted access data added: L:\Restricted-Access-Data\aearep-xxx-nda_Implicit"* and tag the RA currently assigned to run the code.

### Once case is done

After replication is complete (case is in *Pending openICPSR Changes* or *Assess openICPSR Changes* and there's no post-publication reproducibility check subtask),

- Delete the data from the L: drive and Box and then reply to the author that the data has been deleted.
- Respond to previous email to author:

>
> Hello Dr. *Author*,
>
> This email is confirm that we have deleted the restricted access data for "[Title]" from our workspaces. Your deposit is being moved along in the publication process.
>



- Check the box on JIRA indicating the data has been deleted (Data Info tab > "Was data deleted?")