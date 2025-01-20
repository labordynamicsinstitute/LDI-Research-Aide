---
title: Request for External Reproducibility Checks
parent: Email templates
---

# Request for External Reproducibility Checks

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


---
title: Request for External Reproducibility Check - non-cascad
parent: Email templates
---

## Request for External Reproducibility Check - non-cascad

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
> 5. Include
