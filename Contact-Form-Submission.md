# Contact Form Submission

When you get a Jira ticket titled `"Contact form submission (researcher@university.edu, FirstName LastName)"`, often these are in reference to openICPSR deposit that have already been published. The message is from someone reviewing the deposit and found something concerning, like a missing code file or potential PII.

- Review the message in the `Primary Info Section`.
- Using the DOI or article titled provided, search for the Manuscript Identifier
- Fill out the `Journal` field and the `Manuscript Central Identifer` field
- Mark the `MCStatus` as Update and fill out the `Update Type` (under Other Links) as the appropriate label, depending on who is contacting us.
- Depending on what the email says, you may have to contact the authors of the original deposit or Kyrani for technical issues.

**These email templates are specific examples. Please edit the content to match the issue in question.**

Here is an email templates for the author of the package in question

> Action needed for your published replication package "Title" (AEAREP-xxx)

<blockquote>

Hello Dr. Bai,
We were contacted by a researcher about your replication package for "Title" (https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/[000000]). Due to a bug in openICPSR, the file [code/01_simulation/archive_functions.R] is empty. Could you please update the replication package with the necessary code?

These are the directions on how to update an already published replication package.
https://aeadataeditor.github.io/aea-de-guidance/FAQ.html#i-was-wondering-whether-and-how-i-can-update-the-published-repository-for-our-paper-i-was-contacted-by-a-researcher-who-is-doing-a-replication--couple-of-minor-issues--forgotten-to-include-two-auxiliary-datasets-in-the-repository-without-which-one-of-the-programs-does-not-run-successfully

Thank you so much. Please let us know if you have any questions and notify us once the changes are made.
</blockquote>




Here are some email templates for the person who submitted the contact form.

> Subject: Contact Form Submission Response (AEAREP-xxx)

<blockquote>

Thank you for contacting us about the replication package for the article [MC Number] “Title”.

We have contacted the authors and they've uploaded the file [code/01_simulation/archive_functions.R] to the deposit. The deposit still needs to be published again for you to view it, but I've attached the code in the meantime.

Hope this helps. Let us know if you have any other questions.
</blockquote>

Once the issue has been resolved, move the Jira ticket to `Done`.
