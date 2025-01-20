---
layout: default
title:  Unpublication of Deposit with Special Reference to PSID
--- 

# Unpublication of Deposit with Special Reference to PSID

Deposits may need to be unpublished due to a very small number of reasons:

- infringement of terms of use (provision of data that is not allowed)
- publication of inappropriate PII

{: .highlight }
> An example is when we received notification about an infringement of PSID terms of use.

## Step 1: Determine relevance

Verify that the data in question is indeed present in the openICPSR deposit, and that the request (from PSID, others) is reasonably motivated.

- Depending on the urgency, the existing deposit may need to be unpublished at this stage. Otherwise, it can be unpublished once the corrected deposit is available.

## Step 2: Create a Case

Typically, the request will come in via email to the Data Editor, not to Jira.

- Locate the original AEAREP number (if any) for the deposit in question, and code it in the Jira Metadata. [WHAT DO YOU MEAN, be precise]
- Forward the email identifying the infringement to the `dataeditor-queue` email to initiate processing.
- Fill out all relevant JIRA fields, in particular
  - any previous AEAREP number
  - `MCStatus` = `Update`
  - `Update_type` as appropriate
  - `Non-compliant`  is ticked.
  - Add `https://email` to `Report URL` manually only when no prior AEAREP number exists.

- Create repositories for each case, if not already existing. 
- Run the pipeline scripts to generate a pre-change list of files.

{: .highlight }
> Assign the JIRA case to the RAide and move it `Assigned`.

## Step 3: Communicate as necessary with Authors

- If the authors do not already own the deposit (which will be the case for any manuscripts prior to 2019), **share the associated ICPSR deposit with the authors** and ensure all the necessary permission boxes are checked. 
- Respond to the author, confirming that they now have the rights to make the required changes to the deposit. 
  - ensure that the subject line includes the AEAREP number  
  - ensure that <dataeditor-queue@aeapubs.org> is copied. 
  - Include general guidance post at <https://aeadataeditor.github.io/posts/2024-11-01-psid-requests> for reference. 
  - Include links to the revision policy <https://www.aeaweb.org/journals/data/revisions-policy> for reference.

{: .highlight }
> Move the case to `In Progress`.

(While this strictly only requires `Pending openICPSR changes`, given the importance, we leave this in `In Progress`).

## Step 4: Check for compliance

Once the author has made the required changes and **re-submitted** the package, verify compliance with the request and the [AEA Revision Policy](https://www.aeaweb.org/journals/data/revisions-policy)

{: .highlight }
> Move the case to "Pending openICPSR Changes" if the author has made changes but not submitted the deposit.

- Communicate with the author to request submission. Remember to cc `dataeditor-queue` and to include the AEAREP number in the subject line.

{: .highlight }
> Move the case to `Assess openICPSR Changes` if the deposit has been submitted.

- Verify that the infringing data has been removed from the existing deposit in the openICPSR AEA Repository.
- (if PSID) Verify that the link to the DOI of the new PSID deposit containing the infringing data is in related publications is there (if not, add it)
- Check that the README has been updated and that a  CHANGES.txt file is present in the repository.
   - The CHANGES.txt should include lines such as the following two lines: 

    ```
    V1: Original version
    V2: PSID data removed from replication package and deposited at (NEW DOI).
    ```

- Re-run the pipeline to capture the updated contents of the deposit.

Update the JIRA ticket with the following information:

- `Resolution` = `Done` if the deposit has been modified: (unpublishing the V1 and publishing the V2 has been completed).
- `Resolution` = `Evaluation Only` if no action was undertaken and the deposit was found to be compliant as is.

## Step 5: Resolution

Once the deposit is in compliance, 


{: .highlight }
> Move the case to `Pending publication` and assign it back to the Research Aide.

- Unpublish the original deposit (`V1`)
- Publish the new deposit (`V2`).

No updates to the Journal landing page for the article are usually necessary. The link will still point to the `V1` deposit, but the `V2` deposit will be available for download.
