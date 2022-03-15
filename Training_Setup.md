# Setup of Hiring and Training

### Hiring

Timelines:
  - Fall: Post mid-July and train mid to late August
  - Spring: Post mid-November and train mid to late January
  - Summer: Post mid-March and train late April to early May

Lars, the Research Aide, and Graduate Assistant review applicants and then meet to discuss final decisions. Once final decisions are made, the following steps are taken to prepare for training the new cohort of Undergraduate Research Assistants.

1. Send out rejection email. bcc all candidates who were not selected with the following (make sure to update the next upcoming application cycle):
```
Dear Applicant,

Thank you for your application to the LDI Replication Lab. We received a lot of applications from talented folks like you. Unfortunately, you were not selected at this time. 

However, our project will be hiring again in the Summer, and we invite you to consult our job posting at that time. We will be posting any updates on the LDI home page at http://www.ilr.cornell.edu/labor-dynamics-institute. 

Although we cannot provide detailed feedback on your application, one of the frequent reasons that students like you are not selected is that we explicitly search for experience with desktop-style statistical programming languages, in particular with Stata or Matlab. If you have not used these before, but are interested in brushing up your skillset, CISER offers free training to Cornell students in all of these. Regardless if you intend to re-apply in the Summer or for your own self-improvement for the job market, we strongly suggest taking one of these. 

Again, thank you for your interest, and please stay in contact.
```
2. Send out hire notification to selected applicants:
```
All,

Thank you for applying to the AEA Replication Project. 

We have reviewed your application, and have identified you as a qualified candidate. We would like have you join us for the training, during which we will present the task at hand, train you in using the tools and procedures you will need, and walk you through an actual replication task. 

Training will take place from Tuesday Jan 18 to Friday Jan 21. Live attendance should be expected on Tuesday and additional meetings will happen on the following days using Zoom, plus some significant self-paced work.

We must note that this is not a confirmation of employment. During the training, HR will be checking your eligibility for employment, which includes being a current Cornell student and residing in the United States; a I-9 may be needed.

Please let us know if you are still interested in the position.  

Thank you,

```
3. Lars, Research Aide, and GRA meet and discuss a training schedule. Research Aide then drafts a schedule for Lars to review and update the [github page](https://github.com/labordynamicsinstitute/replicability-training) for the [website](https://labordynamicsinstitute.github.io/replicability-training/). 
4. Track which students accept the training invitation in the "Replication Project Resumes" spreadsheet.
5. Once training schedule is set and new RA's have accepted the invitation to the Lab, send out invites (LDI Zoom links) to Day 1 of the training and the following peer review sessions. 

### Training Preparation

1. Add new trainees to the Bitbucket `aeaverification` team as "Developers" [here](https://bitbucket.org/account/user/aeaverification/groups/developers/) by pasting their email into the search bar under "Add member", and clicking "Confirm".
2. Add users to Jira
  - log on to Jira as "dataeditor@aeapubs.org"
  - Click on [People](https://aeadataeditors.atlassian.net/jira/people/search). 
  - Click on Manage users
  - Invite users.
    - Email addresses: comma separated (10 at a time)
    - Product roles is defaulted to `User`
    - Group membership: `trainees`, `replicators`, and `jira-software-users`
    - Click "Invite users"
3. Bulk import test cases to Jira:
  - First, modify the existing [CSV file](https://github.com/AEADataEditor/LDI-Research-Aide/tree/main/Training) with the new "email" and "duedate" fields.
  - Remember to create one for Lars for the first Stata case, and one for each of the experienced RAs who are conducting the peer review sessions.
  - Go to the blue "Create" button in Jira, then select "Import issues".
  - Choose the corresponding CSV file and check the "Use an existing configuration file" box to use the [mapping file](https://github.com/AEADataEditor/LDI-Research-Aide/blob/main/Training/jira-import-mapping.txt)
  - Settings: Import to "AEA training" project, file encoding = UTF-8, delimiter = ",", Date format = "MM/dd/yyyy"
  - Mapping:

![mapping](Training/Mapping.png)

  - Start import, then "check issues"

4. The bulk importer does not map the openICPSR number field, nor allow for a link to the manuscript. Choose "bulk edit", select all issues, and bulk "edit" them to include "openICPSR Project Number" and "Manuscript Central identifier" (i.e. AER-0000-1234). Additionally, add a link to the manuscript in the comments ([PDF_Proofs](https://labordynamicsinstitute.github.io/replicability-training-solutions/)).
5. All issues are imported as "Open" and need to be assigned. Choose "bulk edit", select all issues, and bulk "transition" them to "Assigned".
6. Grant RA's access to download ICPSR deposit (students will need to create their accounts with ICPSR first).
7. Send an updated list of hires to HR (Brenda Herling) and fill out student appointment forms for each RA (also sent to ilr_student_empl@cornell.edu). 
8. Create "Placeholder" tickets for each RA in Jira. The best way to do this is through the same bulk process as creating the training cases (a placeholder csv file can be found [here](https://github.com/AEADataEditor/LDI-Research-Aide/tree/main/Training). Be sure to change the "Import to Project" field from "AEA Training" to "AEA Replication - Default". Then convert each issue to a subtask for the Master Placeholder aearep-1407 (unsure if there is a way to bulk convert to subtask).
9. Go to "/Box/Office of AEA Data Editor/Student Employment/Current_Hire-Exit_Checklists" and create a new exit checklist file for each student. This way we can track what has been done when exiting a student in the future.

