---
layout: default
title:  AEA External Reports
--- 

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


Instances that require the use of restricted-access data for a full reproducibility check can occasionally be sent out for an external report. See the AEA [Policy and Protocol on Third-Party Verifications](https://www.aeaweb.org/journals/data/policy-third-party) for more information on who can conduct these external reports, and the steps that they should follow.

There is actually a filter for tracking these, which should show up in the "Assignments"  dashboard in Jira:

[https://aeadataeditors.atlassian.net/issues/?filter=10015](https://aeadataeditors.atlassian.net/issues/?filter=10015)

## Preparation

Prior to sending out the request for an external reproducibility check there are several steps that should be completed internally.


1. Rename the Part B subtask to *"Request for external reproducibility (Requestee)"* so if we're requesting from CASCAD it'd be *"Request for external reproducibility (CASCAD)"* .
1. Assign Part A to an RA or yourself.
3. Flag the subtask with the Jira tick box `External validation` = Yes
4. Also flag the subtask with the Jira field `External party name`. For institutional replicators, re-use as much as possible. For individuals, anonymize (the name of the third-party replicator should NOT be disclosed).

## Sending out the Request

Send email with subject `"Reproducibility Review Request (AEAREP-xxx)"`
The AEAREP number is the number of the subtask for Part B.

### Cascad


1. The email is sent to both akmansoy@hec.fr and perignon@hec.fr. As always, cc dataeditor@aeapubs.org and dataeditor-queue@aeapubs.org (as well as Lars). 
2. Attach the manuscript to the email. 
3. Paste the OpenICPSR link next to "Code:" and make sure it isn't the admin link (the admin link contains "tenant").
4. Give download access to the replicator(s) (as you would any internal RA).


See [Email template](/LDI-Research-Aide/emails/Email-Templates/#request-for-external-reproducibility-check---cascad).



### Third-Party Replicator (Non-Cascad)

1. The email is sent to the third-party replicator. As always, cc dataeditor@aeapubs.org and dataeditor-queue@aeapubs.org (as well as Lars). 
2. Attach the manuscript and the completed `code-check.xlsx`. 
3. Paste the OpenICPSR link next to "Code:" and make sure it isn't the admin link (the admin link contains "tenant"). 
4. Give download access to the replicator (as you would any internal RA).

See [Email template](/LDI-Research-Aide/emails/Email-Templates/#request-for-external-reproducibility-check---non-cascad).




## Integrating the External Report

**For CASCAD:**

- Never delete section titles from our template report (an RA should have already done the preliminary report). Instead, for sections relevant to the verification, point to the external report with something along the lines of: "Please refer to the external report below."
- Review external report and include bugs and discrepancies in Summary and Findinga (add appropriate Action Item tags)
- Generate a PDF of our internal `REPLICATION.md` and then rename it something along the lines of `REPLICATION_INTERNAL.pdf`. Then append the external report to our internal report and name the final merged report `REPLICATION.pdf`. 

[Example](https://bitbucket.org/aeaverification/aearep-3572/src/master/REPLICATION.md) of formatting for External Report.

**For Non-CASCAD:**

- Integrate the sections after "Stated Requirements" from the `EXTERNAL-REPORT.md` provided by the replicator.


