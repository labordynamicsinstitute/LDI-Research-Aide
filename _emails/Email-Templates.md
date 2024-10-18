---
layout: default
title:  Email Templates
--- 

# Email Templates
{: .no_toc }

Note that these are mostly just the email templates. If further instructions exist, they will be linked.


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Reminding Students to Submit Timesheet


Email `ldi-lab-l@list.cornell.edu` every Wednesday morning (best to have these scheduled in advance)

Remove last line if no non-Cornell students are RAs this semester.

> Subject: Timesheet Reminder

{: .highlight}
> Here's your weekly reminder:
>
> - submit your timesheets by 5pm tonight
> - git push any edits you've made to bitbucket (do this at the end of every work session)
> - Move the Jira tickets to the appropriate status (also do this at the end of every work session)
> 
> Non-Cornell students, use this timesheet: [https://forms.gle/86GpVDjLM9FUgfcp7](https://forms.gle/86GpVDjLM9FUgfcp7)


## Revisions Requested

When a case is stuck at *Pending openICPSR Changes* because the author hasn't edited the deposit:

```
Revisions Requested for Manuscript NumberXX (AEAREP-xxx)
```

```
Dear authors,
Please make the revisions requested to the openICPSR deposit https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/[000000] so that we may move forward with publication of the deposit.

See our full report from [date] for details. I've also attached the report for ease of access. Feel free to contact us directly at dataeditor@aeapubs.org with any questions.

Once you're done, please "Change Status" -> Re-submit to AEA"

Many thanks in advance.
```
Check the Jira comments to make sure the case has not already been revised. If it has, edit the email above to refer to the previously posted remaining items instead of attaching the report.

## Restricted Deposit


When the open ICPSR deposit is labelled "Restricted" and/or they answered "Yes" to any of the [submission questions](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submission-questions). 
- IMPORTANT: **Remove** the line about "If you nevertheless think that access to the data should be restricted," if access is NOT, in fact, restricted.

Subject Line:

```
Action Needed for your open ICPSR Deposit (AEAREP-xxx)
```

{: .highlight }
> Dear Dr. [Author],
>
> We're reviewing your open ICPSR deposit for "[Title]" (MC Number) and noticed you answered "Yes" for one or both submission questions on sensitive data and risks. We are checking in with you to verify that those responses are correct.
> 
> Please answer these questions in regards to the data that are part of the deposit you are submitting. The answer should not consider any other data that may have been used as part of the manuscript’s analysis, but that are not present in this particular deposit. For most deposits, the correct answer to both questions is "No".
> 
> Please review your deposit, and your answers to these questions.
> 
> If the answers are correct as currently provided, please confirm by return email. If you need to modify the answers, you can do so by simply [recalling](https://aeadataeditor.github.io/aea-de-guidance/FAQ.html#you-can-recall-the-submission) the package, and then [re-submitting to the Data Editor](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor)
> 
> If you nevertheless think that access to the data should be restricted, please contact us immediately to discuss. 
> 
> More information can be found in our instructions on submitting to openICPSR: https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submission-questions
> 
> I hope this helps and please let us know if you have any questions. 
>
> Thank you.



## Reminder to Submit

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

## Reminder to Submit When Authors cannot access

In February 2024, ICPSR restructured it's access and identity management system. Every author who last had contact before Feb 15, 2024, and hasn't accessed the deposit since March 1, 2024 (check the logs!) will not be able to access the link sent above.

Either in response to their inquiry, or when known ahead of time (check the logs!), the following paragraph should be sent. If known, add in the email they used according to the logs.

```
In February 2024, ICPSR restructured its access mechanism. If you have not logged onto ICPSR since then, please do the following:

- Create a new account with the SAME email you previously used. This will recover access to all deposits associated with that email.
- Then log on to the system again, using the URL we have provided. You should now be able to make changes and submit.

We apologize for the inconvenience and the terse feedback provided by the system, which unfortunately is outside of our control.
```

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

{: .highlight }
> Dear Dr. *Author*,
> 
> thank you for your inquiry, and for your willingness to share the data with us privately.
> 
> In order to share the data securely, submit your manuscript materials and publishable component of the replication package (all code, and any data that can be published) as usual, via the editorial office.
> 
> In doing so, you will be asked to fill out the [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability). On that form, you can signal to us that you have data that can be shared privately.
> 
> Once the editorial office has assigned the paper to our team, we will reach out to you to discuss possible secure transfer methods. We offer a secure Box.com upload folder, but if your data use agreement requires something else, we are flexible.
> 
> At the end of the reproducibility checks, we will confirm to you the deletion of the data thus provided.
> 
> Please let us know if you have any other questions.

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

## Request for Externa Reproducibility Check - non-cascad


{: .highlight }
> Dear X,
> 
> We would like to request that you assist us in conducting a reproducibility verification for the American Economic Association.
> 
> If you are willing, please prepare a reproducibility report (see below) for the following manuscript, code, and data:
> 
> Manuscript: Attached
> 
> README: In the ICPSR repository
> 
> Code and (public) data: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/123456
> 
> While you conduct the reproducibility checks, we ask that you not communicate with the authors on this topic. Please let us know if you believe you have any conflicts of interest in this matter which would prevent you from conducting an objective check on the reproducibility of the archive.
> 
> Your task is to follow all instructions on how to obtain and extract the data, run the data cleaning/preparation as well as the analysis code. We have already conducted a first assessment, based on our access to the deposit and code, but not data. Attached is a spreadsheet, mapping programs to figures and tables. You should use this to keep track of what works, and what does not work. You should then prepare your report using our [template](https://github.com/AEADataEditor/replication-template/blob/master/EXTERNAL-REPORT.md) ([same in Word format](https://github.com/AEADataEditor/replication-template/blob/master/EXTERNAL-REPORT.docx)).
> 
> Additionally, we find it is useful to include our [template-config.do](https://github.com/AEADataEditor/replication-template/blob/master/template-config.do) in Stata code. The file itself has instructions on how it should be utilized. In sum:
> 
> 1. Save the file in the same directory as the `master.do` file (or whatever it may be called). In this case, the simplest solution may be to create a master.do (in the "Code" directory) which calls the necessary programs.
> 2. Rename the file from "template-config.do" to "config.do".
> 3. Set the local "scenario" according to the file structure.
> 4. Add any necessary packages (as identified by the authors in their README) to the local "ssc_packages"
> 5. Include the config.do in the master file with the following line: `include "config.do"`
> 6. If on a Windows OS, execute the program by right clicking on the `master.do` file and selecting "Execute(do)"
>
> Please file your report via reply-all to this email, within the next 3 weeks or as soon as possible.
> 
> Thank you very much in advance. Please do not hesitate to ask us any question as you go through this.
> 
> Best,


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
