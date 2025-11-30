<script setup>
useHead({ title: 'Presentation | Student Dropout Risk Predictor' })
</script>

<template>
  <div class="container py-5">
    <div class="row mb-5">
      <div class="col-lg-10 mx-auto text-center">
        <h1 class="display-4 fw-bold mb-3">Student Dropout Risk Predictor</h1>
        <p class="lead text-muted">Option C: Machine Learning Final Project</p>
        <p class="fw-bold">Benjamin Hislop: 900896194</p>
      </div>
    </div>

    <div class="row mb-5">
      <div class="col-lg-8 mx-auto">
        <div class="card shadow-sm mb-4">
          <div class="card-header bg-primary text-white">
            <h2 class="h4 mb-0">Project Overview</h2>
          </div>
          <div class="card-body">
            <p>
              The goal of this project is to predict student dropout risk based on various demographic, 
              socioeconomic, and academic factors. By identifying students at high risk early, 
              institutions can intervene and provide necessary support.
            </p>
            <p>
              This application uses a <strong>Random Forest Classifier</strong> to sort students into distinct categories:
              Dropout, Enrolled, or Graduate.
            </p>
          </div>
        </div>

        <div class="card shadow-sm mb-4">
          <div class="card-header bg-secondary text-white">
            <h2 class="h4 mb-0">Data Source</h2>
          </div>
          <div class="card-body">
            <p>
              <strong>Dataset:</strong> <a href="https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success" target="_blank">Predict Students' Dropout and Academic Success</a> (UCI Machine Learning Repository)
            </p>
            <ul>
              <li><strong>Total Features:</strong> 36 (Demographic, Socioeconomic, Macroeconomic, Academic)</li>
              <li><strong>Records:</strong> 4424 students</li>
            </ul>
            <p class="mb-0">
              Key features include Marital Status, Course, Qualifications (Mother/Father), 
              GDP, Unemployment Rate, Tuition Fees status, and Age at enrollment.
            </p>
          </div>
        </div>

        <div class="card shadow-sm mb-4">
          <div class="card-header bg-info text-white">
            <h2 class="h4 mb-0">Model Architecture</h2>
          </div>
          <div class="card-body">
            <h5 class="card-title">Random Forest Classifier</h5>
            <p>
              We chose Random Forest because:
            </p>
            <ul>
              <li>It effectively captures complex non-linear interactions between features.</li>
              <li>It is robust against overfitting compared to decision trees.</li>
              <li>It handles tabular data with categorical features well.</li>
            </ul>
            <p>
              <strong>Performance:</strong> The model achieves ~81% accuracy on the test set, with a strong ability 
              to distinguish between Dropouts and Graduates.
            </p>
          </div>
        </div>

        <div class="card shadow-sm mb-4">
          <div class="card-header bg-success text-white">
            <h2 class="h4 mb-0">App Functionality</h2>
          </div>
          <div class="card-body">
            <p>The web application provides two main modes of interaction:</p>
            
            <div class="d-flex align-items-start mb-3">
              <div class="me-3 text-success">
                <i class="bi bi-person-fill fs-3"></i>
              </div>
              <div>
                <h5 class="fw-bold">Single Student Prediction</h5>
                <p class="mb-0">
                  Fill out a form with a student's details to get an immediate risk assessment.
                  Input validation ensures data quality before processing.
                </p>
              </div>
            </div>

            <div class="d-flex align-items-start">
              <div class="me-3 text-success">
                <i class="bi bi-file-earmark-spreadsheet-fill fs-3"></i>
              </div>
              <div>
                <h5 class="fw-bold">Batch CSV Processing</h5>
                <p class="mb-0">
                  Upload a CSV file containing data for multiple students. The app will:
                </p>
                <ul class="mb-0">
                  <li>Validate the file format and columns.</li>
                  <li>Process all records using the trained model.</li>
                  <li>Return a ranked list of students, sorted by dropout risk.</li>
                  <li>Allow exporting the results for further analysis.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div class="text-center mt-5">
          <NuxtLink to="/" class="btn btn-primary btn-lg px-5">Try the App</NuxtLink>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
.card-header h2 {
  font-size: 1.25rem;
}
</style>
