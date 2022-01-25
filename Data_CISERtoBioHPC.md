# Steps for Transferring Data from CISER to BioHPC

If transferring data from your own laptop to BioHPC, FileZilla may be the simplest solution. However, CISER does not have FileZilla installed. Follow the steps below to transfer data from CISER to BioHPC.

1. First, open up a bash shell in the directory that holds the folder which you want to transfer to BioHPC.
2. SFTP into BioHPC ```sftp mjd443@cbsuecco02.biohpc.cornell.edu```. Your password is the same that you use to login to the cbsuecco02 node (or the login node).
3. `cd` into the desired directory on the BioHPC node.
4. You need to first create the directory on BioHPC: ```mkdir data`.
5. Use the put command to place the desired folder (i.e. "data") on BioHPC: ```put -r data/```.
6. If you run into an error along the lines of ```Can't find request for ID 31425```, try zipping up the files and just transferring the zip file. Once transferred, you can unzip on BioHPC () 
6. Give Lars access to my "workdir/mjd443" with ```chmod -R a+rwX /workdir/mjd443``` (this command is not permanent and should be run again after any edits to the directory).

