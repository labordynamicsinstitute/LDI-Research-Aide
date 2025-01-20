---
layout: default
title:  Training Setup
parent: Procedures
--- 


# Training Setup
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Onboarding

### Add students to various lists

- Track which students accept the training invitation in the "Replication Project Resumes" spreadsheet.
- Once training schedule is set and new RA's have accepted the invitation to the Lab, send out invites (LDI Zoom links) to Day 1 of the training and the following peer review sessions. Also send out this [Google Form](https://docs.google.com/forms/d/1H-L9MommkysuIGc9HO2hZweWB7q1cjixg4oCSBYjIxo/edit) which asks training participants for their dietary restrictions. 
- Add students to [listserv](https://www.list.cornell.edu).
- Go to "[/Box/LDI Replication Lab/Office of AEA Data Editor/Student Employment/Current_Hire-Exit_Checklists](https://cornell.app.box.com/folder/136503467872)" and create a new exit checklist file for each student. This way we can track what has been done when exiting a student in the future.

### After training

Students who fail to show up for the training need to be removed from various lists, so some of these steps will only be done after they have shown up and completed training.

After training:

- Copy the new RAs into the Live sheet.
- Update the columns for *"Start Date"* (column AB) and *"WD End Date (last updated mm/dd/yy)"*
- When students are officially hired, in the Live sheet, update the "Currently Employed" column to "Y" and the "Team" column to Blue/Green, which will automatically add the students to the "Current" tab.

## Training Preparation

### CCSS Cloud (or other)

Students needed to be added to our computer systems.

- For CCSS Cloud (any Cornell student), send an email with the student's NetID and email to `ccss-researchsupport@cornell.edu`, requesting their addition to the Cloud server "Lars' Group". 
- For RedCloud (non-Cornell students), the process is more complicated and not described here.

### Bitbucket 

1. Add new trainees to the Bitbucket `aeaverification` team as "Developers" [here](https://bitbucket.org/account/user/aeaverification/groups/developers/) by pasting their email into the search bar under "Add member", and clicking "Confirm".
2. Pre-approver link: https://aeadataeditors.atlassian.net/plugins/servlet/project-config/AEAREP/people

### Jira

3. Add users to Jira
  - log on to Jira as "dataeditor@aeapubs.org"
  - Click on [People](https://aeadataeditors.atlassian.net/jira/people/search). 
  - Click on Manage users
  - Invite users.
    - Email addresses: comma separated (it used to be limited to 10 at a time, but they're updating this)
    - Product roles is defaulted to `User`
    - Group membership: `trainees`, `replicator`, `replicators`, and `jira-software-users`
    - Click "Invite users"

### Setup training cases

4. Bulk import test cases to Jira:
  - First, modify the existing [CSV file](https://github.com/AEADataEditor/LDI-Research-Aide/tree/main/Training) with the new "email" and "duedate" fields.
  - Remember to create one for Lars for the first Stata case, and one for each of the experienced RAs who are conducting the peer review sessions.
  - On the "[Search page](https://aeadataeditors.atlassian.net/issues/?jql=order%20by%20created%20DESC)", go to the  "..." menu, then select "Import issues". **Be sure to import into the "Training 2024" (TRAIN) project!**
  - Choose the corresponding CSV file and check the "Use an existing configuration file" box to use the [mapping file](https://github.com/AEADataEditor/LDI-Research-Aide/blob/main/Training/jira-import-mapping.txt)
  - Verify the settings.

![Settings]({{ '/Training/Settings.png' | relative_url }})

  - Mapping:

![mapping]({{ '/Training/Mapping.png' | relative_url }})

  - Use the `Validate` button to check for errors.

![Validation]({{ '/Training/Validate.png' | relative_url }})

  - If all is fine, `Begin Import`, then `Check issues`.

5. From the "..." at the top right corner, choose "bulk change all x issue(s)", select all issues, and select "Transition Issues"
6. bulk "transition" them from "Open" to "Assigned". You should then be presented the "Bulk Edit Screen" (if not you can just repeat these steps to get to the "Edit Issues" option of the bulk action screen). If you have to edit any fields, do it here. 
7. Grant RA's access to download ICPSR deposit (students will need to create their accounts with ICPSR first).
  - Go to each case's openICPSR deposit.
  - Remove previous trainees' access.
  - Add new trainees' access.
  - Trick: use Excel to concatenate the email addresses with `, ` (`=concatenate(A1,", ")`), then copy-paste the new column into the `Share` field with download permissions.
8. Create "Placeholder" tickets for each RA in Jira. The best way to do this is through the same bulk process as creating the training cases (a placeholder csv file can be found [here](https://github.com/AEADataEditor/LDI-Research-Aide/tree/main/Training)), except:
  - Change the "Import to Project" field from "AEA Training" to "AEA Replication - Default". 
  - Then individually convert each issue to a subtask for the Master Placeholder `aearep-1407` (unsure if there is a way to bulk convert to subtask).

### Announce training

The training schedule should have been announced, but check that everything is in order: <https://labordynamicsinstitute.github.io/replicability-training/>

### Training feedback

9. After training, grade reports using https://github.com/labordynamicsinstitute/replicability-training-solutions as a reference


