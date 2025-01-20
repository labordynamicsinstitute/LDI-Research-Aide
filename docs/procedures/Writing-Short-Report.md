---
layout: default
title: Writing a Short Report
parent: Procedures
---

# Writing a Short Report

When the authors don't provide a README, any code, or the deposit is completely empty* or contains all the replication materials as '.zip' files, you submit a short report to ScholarOne.

{: .warning }
**double-check the openICPSR log history first. They might have uploaded stuff but openICPSR glitches and shows an empty repo.*

- Assign the Jira case to yourself
- Create the bitbucket repository as usual
- Fill out the bitbucket short name
- If deposit is not empty, run the pipeline
- Use the `draft-replication-noncompliant.md` file in the repository and fill in accordingly.
- Move the short report to “REPLICATION.md”
- "Fast track" the Jira ticket to *Writing Report (Part C)*. In the pop-up window, fill out:
    - `Resolution` as "Not able to replicate"
    - `Reason for Failure to be Fully Reproducible` as "Missing README" and anything else relevant.
- Move to Jira ticket to *Under Review* (Report URL should be filled out if it hasn't already)
- Move ticket again to *Pre-approved* (make sure the MCRecommendationV2 field is filled out)
- Tag Lars letting him know a short report has been written.
