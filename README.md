# MLSA-Certificate-Generator

This repo simply use a template certificate docx file and generates certificates in
both docx and pdf.

##  For Windows and Mac users.

### Use ```python main_certificate.py``` to run your code

## Run these commands in your terminal

```
git clone https://github.com/Sarita-021/MLSA-Certificate-Generator/
cd MLSA-Certificate-Generator
```

## Customization and Generation

### Step 1 : Adding list of participants

- Now Copy the name of Participants of your event and paste their names in the file  `Event Participants.csv` present in the folder `Templates`.
- Save the changes
- No additional field required only name of participants can work.

### Step 2 : Modifying your event details

- Open the file `main_certificate.py`
- Move to line 54 and Write your name instead of "Your Name"
- Move to line 57 and Write your name instead of "Your Event Name"
- Move to line 60 and Write your name instead of "Your Event Date"
- Save the changes.

### Step 3 : Open Terminal

### ```For Mac Users```

```
pip3 install -r requirements.txt
python3 main_certificate.py
```

### ```For Windows Users```

```
pip install -r requirements.txt
python main_certificate.py
```

### Step 4 : Certificates

- Search for Output Folder in "MLSA-Certificate-Generator" folder in your pc
- There you find 2 separate folders namely "Doc" and "PDF" with your certificates ready
- Extract the certificates and share with your participants


## Well Done!!! You Did It.
## Thank You
