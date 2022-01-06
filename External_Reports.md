# AEA: External Reports

Instances that require the use of restricted-access data for a full reproducibility check can occasionally be sent out for an external report. See the AEA [Policy and Protocol on Third-Party Verifications](https://www.aeaweb.org/journals/data/policy-third-party) for more information on who can conduct these external reports, and the steps that they should follow.

## Preparation

Prior to sending out the request for an external reproducibility check there are several steps that should be completed internally.

1. Fill in the `code-check.xlsx` with tables/figures and the corresponding programs so that the third-party replicator can easily complete it.
2. Create a subtask with the subject "Request for External Reproducibility Check" and convert it to a subtask of the original Jira ticket.
3. Flag the subtask with the Jira tick box `External validation` = Yes
4. Also flag the subtask with the Jira field `External party name`. For institutional replicators, re-use as much as possible. For individuals, anonymize (the name of the third-party replicator should NOT be disclosed).
3. Write up to the preliminary report.

## Sending out the Request

The email request should include the `code-check.xlsx` and a `REPLICATION.md` that has been paired down to the following sections: Computing Environment of the Replicator, Replication Steps, Findings, and Classification. Additionally, always attach the manuscript (from the Jira issue) and the README in the email. Once the email has been sent, share the openICPSR deposit with the third party replicator. 

Template email:

```
Dear X,

We would like to request that you assist us in conducting a reproducibility verification for the American Economic Association.

If you are willing, please prepare a reproducibility report (see below) for the following manuscript, code, and data:

Manuscript: Attached

README: Attached

Code and (public) data: link to openICPSR deposit or Dropbox

While you conduct the reproducibility checks, we ask that you not communicate with the authors on this topic. Please let us know if you believe you have any conflicts of interest in this matter which would prevent you from conducting an objective check on the reproducibility of the archive.

Your task is to follow all instructions on how to obtain and extract the data, run the data cleaning/preparation as well as the analysis code. We have already conducted a first assessment, based on our access to the deposit and code, but not data. Attached is a spreadsheet, mapping programs to figures and tables. You should use this to keep track of what works, and what does not work. You should then prepare your report using our template (also attached) (the report is Markdown, but you can send it back as TXT or Word, as is most convenient for you).

Please file your report via reply-all to this email, within the next 3 weeks or as soon as possible.

Thank you very much in advance. Please do not hesitate to ask us any question as you go through this.


Best,
```



## Follow-Ups


## Integrating the External Report







write up the process we use for sending out external report? We have the criteria WHO can do this listed at https://www.aeaweb.org/journals/data/policy-third-party but we don't have the process described in the "handbook" for you and anybody else:

•	write-up the process: 
o	sending out email (including the template email, providing access to openICPSR and what to do when not)
o	tracking in Jira (create subtask, flag the subtask with the Jira tick boxes "External assignment" = Yes, and the label of the replicator. For institutional replicators, re-use as much as possible. For individuals, anonymize (no names, other than the already existing ones, i.e., Vitor)
o	follow-ups (by email, in Jira)
o	integrating (merging into standard report, appending to standard report, or sending a supplementary report after the fact)

There is actually a filter for tracking these, which should show up in the "Assignments"  dashboard in Jira:

https://aeadataeditors.atlassian.net/issues/?filter=10015
