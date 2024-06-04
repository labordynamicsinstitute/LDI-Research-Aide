# [MCNUMBER] ["Title"] Validation and Replication results

## SUMMARY

Thank you for submitting the replication package. At this time, the deposit is not compliant, and we have not made an assessment. 

 We provide guidance on how to make a compliant deposit, in line with the [Official Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code), the required  [Template README](https://social-science-data-editors.github.io/template_README/). We provide extensive [Step by step guidance](https://aeadataeditor.github.io/aea-de-guidance/), which we suggest you consult.


## General

- [ ] Data Availability and Provenance Statements
  - [ ] Statement about Rights
  - [ ] License for Data
  - [ ] Details on each Data Source
- [ ] Dataset list
- [ ] Computational requirements
  - [ ] Software Requirements
  - [ ] Controlled Randomness
  - [ ] Memory and Runtime Requirements
- [ ] Description of programs/code
  - [ ] (Optional, but recommended) License for Code
- [ ] Instructions to Replicators
  - [ ] Details
- [ ] List of tables and programs
- [ ] References

We found no README in the deposit. The README should have all the above elements in order to be compliant.

> [REQUIRED] As specified in the [Policy](https://www.aeaweb.org/journals/data/data-code-policy) and the [DCAF](https://www.aeaweb.org/journals/forms/data-code-availability), the README shall follow the schema provided by the [Social Science Data Editors' template README](https://social-science-data-editors.github.io/guidance/template-README.html).



### Requirements

- [ ] README is in TXT, MD, PDF format
- [ ] Deposit has no ZIP files
- [ ] Title conforms to guidance (starts with "Data and Code for:" or "Code for:", is properly capitalized)
- [ ] Authors (with affiliations) are listed in the same order as on the paper

> [REQUIRED] Please ensure that a ASCII (txt), Markdown (md), or PDF version of the README are available in the data and code deposit.

> [REQUIRED] Deposit should not have ZIP files visible. 
  - on openICPSR: ZIP files should be uploaded to openICPSR via "Import from ZIP" instead of "Upload Files". Please delete the ZIP files, and re-upload using the "Import from ZIP" function.
  - on other platforms: Please consult with your repository helpdesk how to "import from ZIP".

> [REQUIRED] Please review the title of the deposit as per our guidelines (below).

> [REQUIRED] Please review authors and affiliations on the deposit. In general, they are the same, and in the same order, as for the manuscript; however, authors can deviate from that order.


> Detailed guidance is at [https://aeadataeditor.github.io/aea-de-guidance/](https://aeadataeditor.github.io/aea-de-guidance/), for non-ICPSR deposits, check out [this guidance](https://aeadataeditor.github.io/aea-de-guidance/guidelines-other-repositories).


### Deposit Metadata


- [ ] JEL Classification (required)
- [ ] Manuscript Number (required)



For additional guidance, see [https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html).

## Classification

>
> Full reproduction can include a small number of apparently insignificant changes in the numbers in the table. Full reproduction also applies when changes to the programs needed to be made, but were successfully implemented.
>
> Partial reproduction means that a significant number (>25%) of programs and/or numbers are different.
>
> Note that if some data is confidential and not available, then a partial reproduction applies. This should be noted in the Reasons.
>
> Note that when all data is confidential, it is unlikely that this exercise should have been attempted.
>
> Failure to reproduce: only a small number of programs ran successfully, or only a small number of numbers were successfully generated (<25%). This also applies when all data is restricted-access and none of the **main** tables/figures are run.

- [ ] full reproduction
- [ ] full reproduction with minor issues
- [ ] partial reproduction (see above)
- [x] not able to reproduce most or all of the results (reasons see above)

### Reason for incomplete reproducibility

- [ ] `Discrepancy in output` (either figures or numbers in tables or text differ)
- [ ] `Bugs in code`  that  were fixable by the replicator (but should be fixed in the final deposit)
- [ ] `Code missing`, in particular if it  prevented the replicator from completing the reproducibility check
  - [ ] `Data preparation code missing` should be checked if the code missing seems to be data preparation code
- [ ] `Code not functional` is more severe than a simple bug: it  prevented the replicator from completing the reproducibility check
- [ ] `Software not available to replicator`  may happen for a variety of reasons, but in particular (a) when the software is commercial, and the replicator does not have access to a licensed copy, or (b) the software is open-source, but a specific version required to conduct the reproducibility check is not available.
- [ ] `Insufficient time available to replicator` is applicable when (a) running the code would take weeks or more (b) running the code might take less time if sufficient compute resources were to be brought to bear, but no such resources can be accessed in a timely fashion (c) the replication package is very complex, and following all (manual and scripted) steps would take too long.
- [ ] `Data missing` is marked when data *should* be available, but was erroneously not provided, or is not accessible via the procedures described in the replication package
- [ ] `Data not available` is marked when data requires additional access steps, for instance purchase or application procedure.
- [x] `Missing README` is marked if there is no README to guide the replicator.