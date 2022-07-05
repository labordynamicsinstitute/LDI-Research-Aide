# Template Request for External Reproducibility Check 

## Cascad

Email Template:

```
Dear Olivier, Christophe,

I would like to ask if you are able to review another manuscript for us.

If you are able to conduct the reproducibility check, please prepare a reproducibility report for the following manuscript, code, and data:

Manuscript: Attached.

README: In the ICPSR repository.

Code: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/123456

Please file your report via reply-all to this email, within the next 10 days or as soon as possible.

Thank you!
```

1. The email is sent to both akmansoy@hec.fr and perignon@hec.fr. As always, cc dataeditor@aeapubs.org and dataeditor-queue@aeapubs.org (as well as Lars). 
2. Attach the manuscript to the email. 
3. Paste the OpenICPSR link next to "Code:" and make sure it isn't the admin link (the admin link contains "tenant").

## Third-Party Replicator (Non-Cascad)

Email Template:

```
Dear X,

We would like to request that you assist us in conducting a reproducibility verification for the American Economic Association.

If you are willing, please prepare a reproducibility report (see below) for the following manuscript, code, and data:

Manuscript: Attached

README: In the ICPSR repository

Code and (public) data: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/123456

While you conduct the reproducibility checks, we ask that you not communicate with the authors on this topic. Please let us know if you believe you have any conflicts of interest in this matter which would prevent you from conducting an objective check on the reproducibility of the archive.

Your task is to follow all instructions on how to obtain and extract the data, run the data cleaning/preparation as well as the analysis code. We have already conducted a first assessment, based on our access to the deposit and code, but not data. Attached is a spreadsheet, mapping programs to figures and tables. You should use this to keep track of what works, and what does not work. You should then prepare your report using our template<https://raw.githubusercontent.com/AEADataEditor/replication-template/master/REPLICATION.md>, though you only need to start at the section "Computing Environment of the Replicator" (the report is Markdown, but you can send it back as TXT or Word, as is most convenient for you).

Additionally, we have attached a "template-config.do". The file itself has instructions on how it should be utilized. In sum:
1. Save the file in the same directory as the master.do file. In this case, the simplest solution may be to create a master.do (in the "Code" directory) which calls the necessary programs.
2. Rename the file from "template-config.do" to "config.do".
3. Set the local "scenario" according to the file structure.
4. Add any necessary packages to the local "ssc_packages"
5. Include the config.do in the master file with the following line: `include "config.do"`
6. If on a Windows OS, execute the program by right clicking on the file and selecting "Execute(do)"

Please file your report via reply-all to this email, within the next 10 days or as soon as possible.

Thank you very much in advance. Please do not hesitate to ask us any question as you go through this.

Best,
```

1. The email is sent to the third-party replicator. As always, cc dataeditor@aeapubs.org and dataeditor-queue@aeapubs.org (as well as Lars). 
2. Attach the manuscript, `template-config.do`, and the completed `code-check.xlsx`. 
3. Paste the OpenICPSR link next to "Code:" and make sure it isn't the admin link (the admin link contains "tenant").
