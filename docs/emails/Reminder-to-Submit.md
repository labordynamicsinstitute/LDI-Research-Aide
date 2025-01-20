---
title: Reminder to Submit
parent: Email templates
---

# Reminder to Submit

When a package has not been formally submitted, authors have not chosen a license, nor agreed that they have the rights to publish the data. In most cases, we cannot do that for them.

- identify the AEAREP number that corresponds to the deposit (via a Jira search, mostly)
- from the manuscript, identify the authors, and their emails, as well as the [TITLE]
- from the deposit, identify who made the last changes (they will be the ones with a login on ICPSR)

Then compose an email, sent to all emails associated with the authors.

Subject line: 

```
Action needed for the replication package "[TITLE]" (AEAREP-NNNN)
```

with body

```
 Dear authors,

 We are about to publish the replication package associated with your forthcoming [JOURNAL] article "[TITLE]". Unfortunately, the package still needs to be formally "submitted" to the Data Editor, allowing you to define the license and answering a few additional questions. We cannot proceed until you have done that. Please do so as soon as possible.

 Details:
 
 - Go to https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/[DEPOSITNUM]
 - In the top right corner, under "Change Status", select "Submit to AEA".
 - Follow additional guidance explained on [our website](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor).

Please notify us by reply to this email when you have done so.

Many thanks in advance.
```

- Update the **[TITLE]** (both in subject and in  body), **[AEAREP-NNNN]**, **[JOURNAL]**, and **[DEPOSITNUM]** in the link under details.

Send it to the  authors, cc to `dataeditor-queue@aeapubs.org` and  `dataeditor@aeapubs.org`.
