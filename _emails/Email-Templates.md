---
layout: default
title:  Email Templates
--- 

Note that these are mostly just the email templates. If further instructions exist, they will be linked.



## Reminding Students to Submit Timesheet


Email `ldi-lab-l@list.cornell.edu` every Wednesday morning (best to have these scheduled in advance)

Remove last line if no non-Cornell students are RAs this semester.

> Subject: Timesheet Reminder

```
Here's your weekly reminder:
- submit your timesheets by 5pm tonight
- git push any edits you've made to bitbucket (do this at the end of every work session)
- Move the Jira tickets to the appropriate status (also do this at the end of every work session)


Non-Cornell students, use this timesheet: https://forms.gle/86GpVDjLM9FUgfcp7

```

## Revisions Requested

When a case is stuck at *Pending openICPSR Changes* because the author hasn't edited the deposit:

```
Revisions Requested for MCNumberXX (AEAREP-xxx)
```

```
Dear authors,
Please make the revisions requested to the openICPSR deposit https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/[000000] so that we may move forward with publication of the deposit.

See our full report from [date] for details. I've also attached the report for ease of access. Feel free to contact us directly at dataeditor@aeapubs.org with any questions.

Once you're done, please "Change Status" -> Re-submit to AEA"

Many thanks in advance.
```



## Restricted Deposit


When the open ICPSR deposit is labelled "Restricted" and/or they answered "Yes" to any of the [submission questions](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submission-questions). 
- IMPORTANT: **Remove** the line about "If you nevertheless think that access to the data should be restricted," if access is NOT, in fact, restricted.

Subject Line:

```
Action Needed for your open ICPSR Deposit (AEAREP-xxx)
```

```
Dear Dr. [Author],

We're reviewing your open ICPSR deposit for "[Title]" (MC Number) and noticed you answered "Yes" for one or both submission questions on sensitive data and risks. We are checking in with you to verify that those responses are correct.

Please answer these questions in regards to the data that are part of the deposit you are submitting. The answer should not consider any other data that may have been used as part of the manuscript’s analysis, but that are not present in this particular deposit. For most deposits, the correct answer to both questions is "No".

Please review your deposit, and your answers to these questions.

If the answers are correct as currently provided, please confirm by return email. If you need to modify the answers, you can do so by simply [recalling](https://aeadataeditor.github.io/aea-de-guidance/FAQ.html#you-can-recall-the-submission) the package, and then [re-submitting to the Data Editor](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor)

If you nevertheless think that access to the data should be restricted, please contact us immediately to discuss. 

More information can be found in our instructions on submitting to openICPSR: https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submission-questions

I hope this helps and please let us know if you have any questions. 

Thank you.
```

### Early contact

Sometimes, authors contact us prior to submitting, on how they can share the data. Here's the email response one should send.



## Reminder to Submit

When a package has not been formally submitted, authors have not chosen a license, nor agreed that they have the rights to publish the data. In most cases, we cannot do that for them.

- identify the AEAREP number that corresponds to the deposit (via a Jira search, mostly)
- from the manuscript, identify the authors, and their emails, as well as the [TITLE]
- from the deposit, identify who made the last changes (they will be the ones with a login on ICPSR)

Then compose an email, sent to both authors:

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

Send it to the two authors, cc to `dataeditor-queue@aeapubs.org` and  `dataeditor@aeapubs.org`.

## Request Restricted Access Data


### Initiating contact

This is just the email template. For further instructions, refer to [Requesting Restricted-Access Data from Authors](Requesting_Restricted_Access_Data.md)

---

Subject Line:
```
Request for Restricted Access Data (AEAREP-xxx)
```

Send it to authors, cc to `dataeditor-queue@aeapubs.org` and  `dataeditor@aeapubs.org`.

```
Dear Dr. *Author*,

We received a request to conduct the AEA reproducibility check for your manuscript entitled "X." On the Data and Code Availability form which you submitted it was indicated that the data can be made available to the Data Editor privately. Would it be possible for you to provide the restricted-access data so that we may proceed to verify the reproducibility of the entire replication package? The data would not be published, and would be deleted by us once we have completed our process. Our preferred sharing method is a Box File Request (specific to your manuscript), the link for which can be found below, but can alternatively happen via Dropbox or similar means, and should be compliant with your data use agreement.

Box File Request (navigate to the link below and upload the file(s)):
[Insert Box File Request Link Here]

We note that all data sharing with the Data Editor should be in compliance with all applicable data use agreements. Please check before sharing.

Please note that the replicator will ignore any code or public data sent via Box. For more information on what to share with the Data Editor:
https://www.aeaweb.org/journals/data/faq#confidential
https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit.html#structure-in-the-presence-of-confidential-unpublished-data

For more guidance on how to legally and practically share restricted data with the Data Editor:
 https://aeadataeditor.github.io/aea-de-guidance/sharing-restricted-data.html

If you have any questions please do not hesitate to ask.
Thank you!
```

### After completion of all rounds of reproducibility checks

After all checks are complete (case is in *Pending openICPSR Changes* or *Assess openICPSR Changes* and there's no post-publication reproducibility check), respond to previous email:

```

Dear Dr. *Author*,

This email is confirm that we have deleted the restricted access data for "[Title]" from our workspaces. Your deposit is being moved along in the replication process.
```

### Early contact 

Sometimes, authors contact us to learn how to share the data. Here's an email response, adjust as necessary:

```
Dear Dr. *Author*,

thank you for your inquiry, and for your willingness to share the data with us privately.

In order to share the data securely, submit your manuscript materials and publishable component of the replication package (all code, and any data that can be published) as usual, via the editorial office.

In doing so, you will be asked to fill out the [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability). On that form, you can signal to us that you have data that can be shared privately.

Once the editorial office has assigned the paper to our team, we will reach out to you to discuss possible secure transfer methods. We offer a secure Box.com upload folder, but if your data use agreement requires something else, we are flexible.

At the end of the reproducibility checks, we will confirm to you the deletion of the data thus provided.

Please let us know if you have any other questions.
```

---

## Request for External Reproducibility Check - cascad

We sometimes request reproducibility checks from cascad (and possibly others). Email is sent to Olivier AKMANSOY <akmansoy@hec.fr>; Christophe PERIGNON <perignon@hec.fr>, with cc to dataeditor-queue and dataeditor. Note that the replicators should get access to openICPSR, but do not have access to JIRA. They usually prepare only a Part B - so Part A still needs to be assigned to a regular RA.

### Prep

Share the openICPSR deposit with akmansoy@hec.fr

### Email

Adjust the AEAREP and openICPSR numbers (xxxx)

Subject Line:
```
External Reproducibility Check (AEAREP-xxx)
```

```
Dear Olivier, Christophe,

I would like to ask if you are able to review another manuscript for us.

If you are able to conduct the reproducibility check, please prepare a reproducibility report for the following manuscript, code, and data:

- Manuscript: Attached.
- README: In the ICPSR repository.
- Code: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/xxxxxxx

Please let me know if you can do this, and when.

Thank you!
```

---

Note that the email to a different replicator might be a bit more formal.

## Email timesheet for AEA RAs


```
Below are FirstName LastName hours worked (at $15.25 per hour)

2/22 - 2/28 -- 2 hours ($30.50)

2/29 - 2/6 -- x hours ($ )

3/7 - 3/13 -- x hours ($ )

-------------------------------------------------------------------------------
Here are FirstName LastName hours worked (at $15.25 per hour):

2/22 - 2/28 -- x hours ( $ )

2/29 - 2/6 -- x hours ($ )

3/7 - 3/13 -- x hours ($ )
```

## Giving open ICPSR Admin Access to RAs

Email Kyrani (karsimon@umich.edu) from the data editor account.

```
Hi Kyrani,
Can you remove admin access for FirstName LastName (ab123@cornell.edu)
Can you also give admin access to FirstName LastName (xx123@cornell.edu) ? Thank you.

```
