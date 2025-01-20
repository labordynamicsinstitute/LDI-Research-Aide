---
layout: default
title:  Instructions for PSID cases
--- 

Upon receiving a notification about a PSID data violation, the first step is to verify that the data in question is indeed included in the openICPSR Repository and that it violates PSID Conditions of Use (check the provided DOI). 

Next, locate the corresponding AEAREP number for the deposit in question, and code it in the Jira Metadata. 

After identifying the AEAREP number, forward the original email detailing the PSID violation to the relevant queue to initiate processing. Share the associated ICPSR deposit with the authors and ensure all the necessary permission boxes are checked. Respond to the author, confirming that they now have the rights to make the required changes to the deposit.

    In your email to the author, update the subject line to include the AEAREP number and ensure that dataeditor-queue@aeapubs.org is copied. Include general guidance post at https://aeadataeditor.github.io/posts/2024-11-01-psid-requests for reference. 

Once the author has made the required changes and re-submitted the package:

Check for compliance: 

1. Verify that the PSID data has been removed from the existing deposit in the openICPSR AEA Repository.

2. Verify that the link to the PSID deposit is in related publications is there (if not, add it)

3. Check that the README has been updated and that a  CHANGES.txt file is present in the repository.
    The CHANGES.txt should inlcude the following two lines: 

    ```
    V1: Original version
    V2: PSID data removed from replication package and deposited at (NEW DOI).
    ```
4. Check that the package has been officially resubmitted. Until the package is submitted, the old, non-compliant deposit will still be visible.

Once the deposit is in compliance, publish the V2. 

Moving through the workflow: 

Create repositories for all PSID-related cases upfront. Run the pipeline scripts to generate a pre-change list of files, then re-run the pipeline for a normal assessment workflow to ensure proper tracking and compliance.

1. Add https://emailinto the Report URL manually
2. Move the package to "Bypass repository" and set it to "In Progress".
3. Since this is an update, it will allow you to move the ticket to "Pending openICPSR Chages", and from there, you can move it to "Assess". 

The resolution status will depend: 

- Resolution = Done if the deposit has been modified: (unpublishing the V1 and publishing the V2 has been completed).
- Resolution = Evaluation Only if no action was undertaken and the deposit was found to be compliant as is.
