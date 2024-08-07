---
layout: default
title: Daily, Bi-Weekly, and Weekly Tasks
---

## Daily Tasks

1. Check Jira if RAs need new cases. They should have at least two main Jira tasks in their queue. Refer to the [Master Replication Project Sheet](https://docs.google.com/spreadsheets/d/1Ic4UgBR3gNFvgyFigJ5SAnx0rZwlp9vu_9OV39YoXQQ/edit?pli=1#gid=1902712667)  for skill levels of programs for each RA. Details on [how to assign new cases](https://aeadataeditor.github.io/LDI-Research-Aide/procedures/Assigning_New_Cases/)).
2. Check unassigned Jira tickets. Review details [here](https://aeadataeditor.github.io/LDI-Research-Aide/procedures/Check-Unassigned-Cases/).
3. Check the Data Editor email (dataeditor@aeapubs.org). Review the [details here](https://aeadataeditor.github.io/LDI-Research-Aide/emails/Data-Editor-Email-Protocol/).


## Bi-Weekly Tasks

### Attendance

- Take attendance in this [Google Form](https://docs.google.com/spreadsheets/d/1_UeEwNXQqWteKaPNB-aApLlaFqu9SSHOLbBApgC7YT4/edit?usp=sharing) every Monday and Thursday
- Mark "E" for excused when the RA emails their update before the meeting
- After the 11am meeting on Thursday, send an email to the unexcused absences:

> Subject:  LDI Status Update (Response Required)

Examples of emails sent to students:

> Hi [RA],
> We didn't see you at the [Monday/Thursday]. Please email us what cases you're working through and what you plan to get done by the next meeting. In any instance where you can't attend a meeting, please email us an update on what you've been working on. Thank you.

> ​Hi [RA],
> We didn't see you at the Monday meeting. You've had a case in "Assigned" since [date]. Please respond to this email with an update of the cases you've been working on and what you expect to complete this week. Thank you.

## Weekly Tasks

1. Timesheet entry
2. Check or assign urgent Assess/Pending cases


### (1) Timesheets

#### Email reminder

Email `ldi-lab-l@list.cornell.edu` every Wednesday morning (best to have these scheduled in advance)

Remove last line if no non-Cornell students are RAs this semester.

> Subject: Timesheet Reminder

<blockquote>

Here's your weekly reminder:
- submit your timesheets by 5pm tonight
- git push any edits you've made to bitbucket (do this at the end of every work session)
- Move the Jira tickets to the appropriate status (also do this at the end of every work session)


Non-Cornell students, use this timesheet: https://forms.gle/86GpVDjLM9FUgfcp7

</blockquote>

#### Workday

- Log into [Workday](https://www.myworkday.com/cornell/d/home.htmld) every Wednesday afternoon or Thursday by 8am
- Submit your timesheet by going to `Menu` > `Time` > `This Week`
    - Note you cannot work more than 6 hours straight
- Approve the RAs timesheets by going to the `My Tasks` inbox in the top right-hand corner.
- Review hours entered by RAs and make sure they make sense
    - If the hours don't make sense (like an RA submits 10 hours that week but the haven't updated their bitbucket repos in two weeks) email the RA asking for clarification on what they worked on. Timesheets need to be finalized by 11am on Thursday.

#### AEA Hires (Google Sheets)

1. Every other Thursday, open the [AEA Hours Worked](https://docs.google.com/spreadsheets/d/1t78w25fr5a7w7NjnQxsl20q9m_VXw3Hh2c3cy3lI77s/edit#gid=611415739) spreadsheet.

2. Fill in the L column to see the total hours worked per week per student.

3. Using the dataeditor email, send an email to Allison Bridges,  `allison.bridges@vanderbilt.edu` CC-ing Lars and `dataeditor@aeapubs.org` using this template.

4. After the email is sent, enter "Approved" for column M to indicate that the timesheet was sent.

> Subject: AEA RA Hours Worked (Week of [Month] [Day])
<blockquote>

Below are **FirstName LastName** hours worked (at $15.25 per hour)

2/22 - 2/28 -- 2 hours ($30.50)

2/29 - 2/6 -- x hours ($ )

3/7 - 3/13 -- x hours ($ )

-------------------------------------------------------------------------------
Here are **FirstName LastName** hours worked (at $15.25 per hour):

2/22 - 2/28 -- x hours ( $ )

2/29 - 2/6 -- x hours ($ )

3/7 - 3/13 -- x hours ($ )
</blockquote>


### (2) Check Pending and Assess Cases

#### For Pending openICPSR Changes

1. Go on the filter for ["Pending openICPSR Changes"](https://aeadataeditors.atlassian.net/issues/?filter=10022) and sort by Journal Month.

2. Click a Jira ticket. Check the comments to see when the last time we contacted the authors, if at all. If we contacted them recently, stop here.

3. Open the openICPSR deposit. Check if there have been any changes since we requested revisions.

3. If no changes and it's been more than 3 weeks, send the email from the **Revisions Requested** section of [Email Templates](Email-Templates.md)

4. If changes have been made (and it's been more than 3 weeks since they last edited), move the ticket to "*Assess openICPSR Changes*".

#### For Assess openICPSR Changes

1. We currently don't have a filter but you can go to the Pending filter and change it to `status = "Assess openICPSR changes" ORDER BY cf[10106] ASC, created DESC` to filter and order by Journal Issue Month.

2. Look at the tickets issued for the next two months. Our goal is to get them to "Pending Publication" before that month arrives.
    - Ideally we finish July's issues before the end of June and so on. But the earlier the better since we don't know for sure if the authors have made the requested changes.

3. You or an RA must follow the steps of the [manual chapter on Assess cases](https://labordynamicsinstitute.github.io/ldilab-manual/51-openicpsr-monitoring-pending.html#if-changes-have-been-made). 
