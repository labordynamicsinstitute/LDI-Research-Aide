---
layout: default
title:  Using Data Under NDA
--- 

Cases arise in which authors agree to provide data directly to the Data Editor after both parties sign a Non-Disclosure Agreement (NDA). In these cases, the author provides us with the data and the Data Editor places the files in the LDI Lab's folder on the shared S: drive ("S:\LDILab\.."). 

The policy of the LDI lab is that these replications are done strictly on the S: drive. This ensures that none of the data provided under the NDA are moved and the Data Editor can keep track of and subsequently delete the data as per the agreement. 

This process is best done by cloning repository directly to the CISER S: drive "S:\LDILab\aearep-xxxx\" folder and then copying the resitricted data into the repository (following any instructions in the README on where the data should be located). Be diligent in ensuring that no restricted access datasets slip through the git ignore into the bitbucket repository.

We may have revisions based on the restricted data which require running additional code. For this reason, the data should be deleted before the issue is moved to "Pending Publication."