---
layout: default
title:  Replications on CRADC
parent: Probably outdated pages
--- 

> INSTRUCTIONS:
> - Develop updated procedures on how to run replication checks on CRADC.
> - Transfer of code (and other data) in, process to transfer reports out.
> - There's no git on the system, but there is VS Code.
> - What does it take to get students on?

#### Getting Students On

- Students must be part of the relevant DUA with the data provider to be given access to the project on CRADC. The level of access to the data then depends on the agreement between Cornell and the data provider. In the case of Kilts Nielsen, only Lars can access the original copies of the data on CRADC. RA's can access the Project directory and copies of the data.

- CRADC grants access to individual projects. If granted access, your username and password will be specific to that particular project. 
- Logging in is very similar to CISER (**dead link as of 2026-07-08**, page no longer exists: `https://ciser.cornell.edu/computing/computing-help/how-to-login/` — needs a current replacement or removal). 

### Replication Materials

Normally, replication materials can be git cloned onto whichever workspace you are working. This is not the case on CRADC. Any files necessary for the replication must be transferred to CRADC through a secure file transfer. For this reason, the simplest way forward is to download the zip file directly from ICPSR and request that it be transferred to CRADC (there may be differences in how this is requested based on whether or not the file is greater than 5GB). 

- Work with CRADC (Elena) to get the repo copied to CRADC, into the S:\XXXXXX\Projects folder:
    1. Git clone the project as usual to CISER (not CRADC).
    2. Download any data not included in the ICPSR deposit.
    3. Zip up the entire "aearep-xxxx" directory.
    4. Request transfer to the above directory using the CRADC system (**dead link as of 2026-07-08**, domain no longer resolves: `https://cisermgmt.cornell.edu/go/PHPs/SecureDataServicesFileTransfer.php` — needs a current replacement or removal). If the file is larger than 5GB, contact CISER Secure Data Services at cradc@cornell.edu for assistance.

### Verification

Conducting the verification will be almost no different than what you might do on CISER. The interface is the same, and the tools you will need are on the server. 