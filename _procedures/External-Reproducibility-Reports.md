---
layout: default
title:  AEA External Reports
--- 

Instances that require the use of restricted-access data for a full reproducibility check can occasionally be sent out for an external report. See the AEA [Policy and Protocol on Third-Party Verifications](https://www.aeaweb.org/journals/data/policy-third-party) for more information on who can conduct these external reports, and the steps that they should follow.

There is actually a filter for tracking these, which should show up in the "Assignments"  dashboard in Jira:

https://aeadataeditors.atlassian.net/issues/?filter=10015

## Preparation

Prior to sending out the request for an external reproducibility check there are several steps that should be completed internally.


1. Rename the Part B subtask to *"Request for external reproducibility (Requestee)"* so if we're requesting from CASCAD it'd be *"Request for external reproducibility (CASCAD)"* .
1. Assign Part A to an RA or yourself.
3. Flag the subtask with the Jira tick box `External validation` = Yes
4. Also flag the subtask with the Jira field `External party name`. For institutional replicators, re-use as much as possible. For individuals, anonymize (the name of the third-party replicator should NOT be disclosed).

## Sending out the Request

### Cascad

Send email with header `"Reproducibility Review Request (aearep-xxx)"`
The AEAREP number being the number of the subtask for Part B.

1. The email is sent to both akmansoy@hec.fr and perignon@hec.fr. As always, cc dataeditor@aeapubs.org and dataeditor-queue@aeapubs.org (as well as Lars). 
2. Attach the manuscript to the email. 
3. Paste the OpenICPSR link next to "Code:" and make sure it isn't the admin link (the admin link contains "tenant").
4. Give download access to the replicator(s) (as you would any internal RA).

Email Template:

<blockquote>

Dear Olivier, Christophe,

I would like to ask if you are able to review another manuscript for us.

If you are able to conduct the reproducibility check, please prepare a reproducibility report for the following manuscript, code, and data:

Manuscript: Attached.

README: In the ICPSR repository.

Code: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/123456

Please file your report via reply-all to this email, within the next 10 days or as soon as possible.

Thank you!
</blockquote>



### Third-Party Replicator (Non-Cascad)

1. The email is sent to the third-party replicator. As always, cc dataeditor@aeapubs.org and dataeditor-queue@aeapubs.org (as well as Lars). 
2. Attach the manuscript, `template-config.do`, and the completed `code-check.xlsx`. 
3. Paste the OpenICPSR link next to "Code:" and make sure it isn't the admin link (the admin link contains "tenant"). 
4. Give download access to the replicator (as you would any internal RA).

Email Template:

<blockquote>
Dear X,

We would like to request that you assist us in conducting a reproducibility verification for the American Economic Association.

If you are willing, please prepare a reproducibility report (see below) for the following manuscript, code, and data:

Manuscript: Attached

README: In the ICPSR repository

Code and (public) data: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/123456

While you conduct the reproducibility checks, we ask that you not communicate with the authors on this topic. Please let us know if you believe you have any conflicts of interest in this matter which would prevent you from conducting an objective check on the reproducibility of the archive.

Your task is to follow all instructions on how to obtain and extract the data, run the data cleaning/preparation as well as the analysis code. We have already conducted a first assessment, based on our access to the deposit and code, but not data. Attached is a spreadsheet, mapping programs to figures and tables. You should use this to keep track of what works, and what does not work. You should then prepare your report using our [template](https://raw.githubusercontent.com/AEADataEditor/replication-template/master/REPLICATION.md), though you only need to start at the section "Computing Environment of the Replicator" (the report is Markdown, but you can send it back as TXT or Word, as is most convenient for you).

Additionally, we have attached a "template-config.do". The file itself has instructions on how it should be utilized. In sum:

1. Save the file in the same directory as the master.do file. In this case, the simplest solution may be to create a master.do (in the "Code" directory) which calls the necessary programs.
2. Rename the file from "template-config.do" to "config.do".
3. Set the local "scenario" according to the file structure.
4. Add any necessary packages to the local "ssc_packages"
5. Include the config.do in the master file with the following line: `include "config.do"`
6. If on a Windows OS, execute the program by right clicking on the file and selecting "Execute(do)"

Please file your report via reply-all to this email, within the next 3 weeks or as soon as possible.

Thank you very much in advance. Please do not hesitate to ask us any question as you go through this.

Best,
</blockquote>




## Integrating the External Report

**For CASCAD:**

- Never delete section titles from our template report (an RA should have already done the preliminary report). Instead, for sections relevant to the verification, point to the external report with something along the lines of: "Please refer to the external report below."
- Review external report and include bugs and discrepancies in Summary and Findinga (add appropriate Action Item tags)
- Generate a PDF of our internal `REPLICATION.md` and then rename it something along the lines of `REPLICATION_INTERNAL.pdf`. Then append the external report to our internal report and name the final merged report `REPLICATION.pdf`. 

[Example](https://bitbucket.org/aeaverification/aearep-3572/src/master/REPLICATION.md) of formatting for External Report.

**For Non-CASCAD:**

- Integrate the sections after "Stated Requirements" from the `REPLICATION.md` provided by the replicator.


