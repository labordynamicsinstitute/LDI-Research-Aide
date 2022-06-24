When a package has not been formally submitted, authors have not chosen a license, nor agreed that they have the rights to publish the data. In most cases, we cannot do that for them. 

Often, the AEA Editorial Office will notice this when attempting to publish a package, because they can't...

In that case, 

- identify the AEAREP number that corresponds to the deposit (via a Jira search, mostly)
- from the manuscript, identify the authors, and their emails, as well as the [TITLE]
- from the deposit, identify who made the last changes (they will be the ones with a login on ICPSR)

Then compose an email, sent to both authors:

Subject line: 

> Action needed for the replication package for your forthcoming [JOURNAL] article "[TITLE]" ([AEAREP-NNNN])

with body

> Dear authors,
>
>we are about to publish the replication package associated with your forthcoming [JOURNAL] article "[TITLE]". Unfortunately, the package still needs to be formally "submitted" to the Data Editor, allowing you to define the license and answering a few additional questions. We cannot proceed until you have done that. Please do so as soon as possible.
>
> Details:
> 
> - Go to https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/[DEPOSITNUM] (last submitting author was [EMAIL])
> - In the top right corner, under "Change Status", select "Submit to AEA".
> - Follow additional guidance explained on [our website](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor).
>
>Please notify us by reply to this email when you have done so.
>
>Many thanks in advance.


Send it to the two authors, cc to `dataeditor-queue@aeapubs.org` and possibly `dataeditor@aeapubs.org`.
