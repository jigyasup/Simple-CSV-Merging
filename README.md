yipl-problem
The following project is done to solve the problem provided by  Young Innovation Prv Ltd 
The details about problem is 
You have two sets of csv files - one containing the contracts data and the other containing the awarded contracts. Your task is to combine the two csv files using the common field (contractName) and compute the total amount of closed awarded contracts. The combined csv should also include one more field - latlon which contains the geocoded value of the contract location, if available. Use the API (from google, osm, or others) to geocode the location.

There are problems with the data, which means there are closed contracts which have not been awarded yet.

The data are not real data and presented for this problem only. The data fields and real data are available at http://www.edolidar.gov.np/tenders.php

The first contract file contains the following fields

    contractname
    status
    bidPurchaseDeadline
    bidSubmissionDeadline
    bidOpeningDate
    tenderid
    publicationDate
    publishedIn

The second award file contains the following fields

    contractName
    contractDate
    completionDate
    awardee
    awardeeLocation
    Amount

The output file will contain the fields from both files (blank values if the contract is not awarded yet)

    contractname
    status
    bidPurchaseDeadline
    bidSubmissionDeadline
    bidOpeningDate
    tenderid
    publicationDate
    publishedIn
    contractDate
    completionDate
    awardee
    awardeeLocation
    latlon
    Amount

After the file is created, read the output file and show the total amount of awarded contracts which have been closed. 700,000 in our case.

The solution of the problem is done in Python and using Pandas package. 


To run the script you should have python 2.7 installed in your machine. Along with Python your machine should have pandas package installed.
To install Python on your machine 
1. For ubuntu and mac user you have already python installed in your machine . No worries for python. :D 
2. For Windows user go to https://www.python.org/downloads/ 

To install Pandas 
http://pandas.pydata.org/pandas-docs/stable/install.html


The solution should be up
To run the script
  i)  open your terminal
  ii) type "python solution.py "
