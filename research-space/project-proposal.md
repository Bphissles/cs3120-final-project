<style>
html body {
  font-size: 14px;
}
html body table td, html body table th {
    padding: 6px 9px;
}
html body h1,
html body h2,
html body h3,
html body h4,
html body h5,
html body h6 {
  margin-bottom: 0 ;
}
html body hr {
  margin-top: 20px;
  margin-bottom: 0;
}
</style>

### Option C: Student Dropout Risk Predictor - <small>Benjamin Hislop: 900896194</small>

---
#### Model Overview

This will likely be a random forest classifier since the objective is to sort students into distinct categories. Something like a linear regression or logistic regression would not be appropriate for this task since it may not effectively capture the complex interactions between features that I hope to uncover.

---
#### Dataset Source<br><small>https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success</small><br><br>


**Total Features:** 36 | **Preliminary relevant features:** 19 | **Data Characteristics:** Tabular, 4424 rows

|feature list| feature list| feature list| feature list|
|---|---|---|--|
|Marital status| Course| Previous qualification| GDP|
|Daytime/evening attendance| Mother's qualification|Target|International|  
|Nationality| Father's qualification| Displaced| Unemployment rate|
|Educational special needs| Debtor| Gender| Inflation rate|
|Tuition fees up to date|Scholarship holder| Age at enrollment|
  

---
#### App Functionality

**User Interaction:** on site entry the user will have the opportunity to select how many students they would like to predict dropout for. Either by filling out a form for an individual student to process, or by uploading a csv file of student data to process multiple students at once. A blank csv will be available for download to fill out and upload. 
  - for the form processing, validation will be handled like a standard form interface.
  - for the csv processing, errors will be listed in a table below the upload button to show which rows have issues, and gentle guidance on how to fix them.

After processing, the app will output a list of students and their predicted dropout risk. The list will be sorted by predicted dropout risk, with the highest risk students at the top. There may also be a pie chart, with only three potential outcomes though it may not warrant additional visualization. There will be an option to download the list as a new csv file.

**Explicit Additional Features:** 
- Form processing
- CSV processing
- Error validation
- Data exporting

---
#### Tools and Technologies

The frontend will be built with Nuxt.js(html + css + js + vue.js), and pm2 will be used to manage server side rendering. The backend will be built using flask. Hosting will be managed between Netlify and Render.