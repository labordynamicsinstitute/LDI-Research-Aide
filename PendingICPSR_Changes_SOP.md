# AEA: Pending openICPSR Changes

## Background

Many cases which we review end up with a recommendation (`MCRecommendationV2` on Jira) of "Accept - with Changes." In short, what this means is that the changes which we are requesting do not constitute a complete revision from the authors. So, instead of having a complete revision added to our queue, the authors will make any necessary changes to the deposit on ICPSR. Separately, any changes to the manuscript/appendix will be made at the copyediting stage and handled by the editorial office, which is something that we in the lab are not involved in. 

It is important to understand how the submission process works once we have finished reviewing a manuscript and Lars has approved the final report. The RA's responsible for this process are following these [instructions](https://labordynamicsinstitute.github.io/replicability-training-curriculum/aea-interfacing-with-the-journal-management-system.html). It will be very helpful to review them. Cases that are designated as "Accept - with Changes" will have our report submitted to manuscript central (MC), the Jira ticket will be moved into "Pending openICPSR changes," and the ICPSR deposit will be unlocked so that the authors can make changes. 

Once the submission process is complete, we wait for the authors to make the requested changes to the deposit. When it is clear that edits have been made to the deposit, we need to verify that all of our [REQUIRED] tags have been completed. You can review the required changes both in the full report on bitbucket and in the Project Communication Log in ICPSR. 

The evaluation process does **NOT** require running any code. In most cases, these are minor changes, such as adding software dependencies or data access instructions to the README. Some cases will involve minor debugging issues, for which we are only checking to see that edits to the code have been made. We do not need to go back and re-verify that the code runs. 

## Process

### ICPSR View Log

- A good place to start in this process is to open ICPSR and click "View Log" under "Share Project" and "Change Owner." 
- This log will tell you all the changes that have been made to the deposit and when. From here we can tell whether or not the authors have made any changes since we originally requested the revisions. 
- Additionally, this is a great resource for checking which program files the authors have made changes to. 

### Verify Requested Changes

- If you have verified that all the required changes have been made, move forward with the acceptance process. This simply means following step **13.5.2 FOR ACCEPT** from the submission [instructions](https://labordynamicsinstitute.github.io/replicability-training-curriculum/aea-interfacing-with-the-journal-management-system.html). 
- ICPSR does not always successfully send out a notification email for the posting of the comment. If you don't receive the email, as a last resort, simply copy and paste your ICPSR comment into the Jira ticket so that we have a record.

### Insufficient Changes

- If, in your review, you find that not all changes have been made, or it is unclear whether or not certain changes are acceptable/sufficient, please reach out to Lars and Michael with a comment on the Jira ticket outlining your question. 
- These cases are not always cut and dry, and we would prefer that you ask us questions before making a final acceptance decision on the deposit.

### No Changes
- If no changes have been made to the deposit since requesting revisions, start a message in the Communication log:

    - with subject line: `AEAREP-xxx Data and Code Deposit Revisions Reminder` (replace with appropriate numbers)
    - with body
```{block, type="bbox"}
Authors,

Please make the revisions requested to the ICPSR deposit so that we may move forward with publication of the deposit.

See our previous comment above and our full report for details. Feel free to contact us directly at dataeditor@aeapubs.org with any questions.

Thanks!
```


## Notes

- **A note on [SUGGESTED] items**. We, of course, attempt to get authors to make their deposit as reproducible as possible. Which means suggesting improvements such as creating a `master.do` or including code to automatically export results. However, they are only suggestions. In other words, they do not impede reproducibility and thus we do not require that the authors make those changes. If the only changes not made to the deposit were [SUGGESTED], move forward with acceptance. 

- **A note on deposit status**. When an ICPSR deposit has a status of "Submitted" it is locked. This means that the authors will not be able to make any changes. If the deposit status is "Deposit in Progress" or "Revisions Requested" the deposit unlocked and changes may be made. Review the submission instructions above for information on how to unlock a deposit. 

- When authors ask if they need to re-submit the updated manuscript to ScholarOne/Manuscript Central. Paste the following within the acceptance (or reminder) post on ICPSR:
> At this stage, any changes to the manuscript are handled directly with editorial office – another submission to Scholar One is not necessary. If you are not already in contact with the editorial office, please reach out to Lucia Giordano at l.giordano@aeapubs.org.

## Giving open ICPSR Admin Access to RAs

Email Kyrani (kreneau@umich.edu) from the data editor account.

```
Hi Kyrani,
Can you remove admin access for FirstName LastName (ab123@cornell.edu)
Can you also give admin access to FirstName LastName (xx123@cornell.edu) ? Thank you.

```
