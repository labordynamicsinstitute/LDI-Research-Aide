---
layout: default
title:  Running author-provided check cases
parent: Procedures
--- 


# Running author-provided check cases
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>



## Requesting Author-provide replication check

- Select cases that are single-software (double-check!), for now only Stata or R.
- Mark these under `Repl. info` -> `Eligibility for author-generated reproducibility check` as `Yes`. When assigning the case, this should automatically generate a subtask of type `Author-Generated Reproducibility Check`.
- Send an email to the author, see [email template]({{ '/emails/Request-author-verification' | relative_url }})
- Move subtask to `In progress`.

## When reply is received

- Reply should be recorded in the main task.
- Run pipelines again.
- Check with the guidelines at <https://aeadataeditor.github.io/aea-de-guidance/preparing-replication-package.html>


### If the author deviates from the protocol ...

Check:
  - author did not run Docker, **Step 5**
  - does master file have the required code (Stata environment, R environment, installation of code, no absolute paths)? (**Step 2 and 3**) Part of this is in `generated/file-paths-summary.md`. 
  - did the author provide a log file? (**Requirement**)
  - did the author fail to confirm independent run (alternative to **Step 5**)?
- If any of the above are true (the author failed to follow protocol), then 
  - move subtask to `Done`, and mark the resolution `Won't do`.
  - Create a new (regular) subtask for `Part B` manually, and assign to a replicator.

### If the author followed the protocol ...

- If author provides a TRO from SIVACOR, the replication check is accepted, no code needs to be run.
- If author confirms that Docker was used, 
  - if code runs in less than 2 hours as per README, then run the `z-run-any-big` pipeline.
    - if code runs in more than 2 hours as per README, then upload the full openICPSR ZIP file to <https://submit.sivacor.org/> and request a TRO from SIVACOR.

## Confirm with authors

Depending on the type of conversation with authors,
- Confirm that protocol was followed, and that the author-generated SIVACOR TRO was accepted. 
  - Mark the subtask as `Done`, resolution `Replicated`.
  - Mark the `Computing environment` as `SIVACOR`
- Confirm that protocol was followed, and that the accelerated check in our automated system succeeded. 
  - Mark the subtask as `Done`, resolution `Replicated`.
  - Mark the `Computing environment` as `Bitbucket`.
- If the author did not follow protocol, and a regular replication is needed, respond to author, mentioning the item that failed the check, and confirm that the replication package has been assigned to the regular queue. 
  - Move subtask to `Done`, resolution `Won't do`.
  - Create a new (regular) subtask for `Part B` manually, and assign to a replicator.
