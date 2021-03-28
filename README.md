# crawler_google_public_pdf

Google has a public pdf api 
link : https://storage.googleapis.com/pub-tools-public-publication-data

You could see some google public research paper like this:
```
https://storage.googleapis.com/pub-tools-public-publication-data/pdf/3c1f67300ee08e332d113c374d1d56b710c0ea2a.pdf
```

It is composed like :

"https://storage.googleapis.com/pub-tools-public-publication-data" + "/pdf/" + "pdf_name.pdf" 

We could parse the xml about  https://storage.googleapis.com/pub-tools-public-publication-data to extract the pdf info list and download them.


### Structure 

```
crawler_google_public_pdf/
└─── README.md
└─── requirements.txt    
└─── pub-tools-public-publication-data.xml // a example about the xml downloaded form google public api
└─── crawler_google_public_pdf.py //script to downloaded pdf
└─── download_pdf/     //a place to saved the results
```

### Setup
Python version: 3.7
```
$ conda install --yes --file requirements.txt
```

### Run the script
```
$ python crawler_google_public_pdf.py
```

### Process with colab
https://colab.research.google.com/drive/1iLf07POad4xDDpF3K1Whe-cn_0ct8_d7?usp=sharing



