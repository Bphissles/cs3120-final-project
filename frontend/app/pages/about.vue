<script setup>
useHead({ title: 'About | Student Dropout Risk Predictor' })
</script>

<template>
    <div class="container py-5">
    <div class="row align-items-center mb-5">

      <h1 class="display-5 fw-bold mb-3 px-2">What it is</h1>
      <p class="lead px-2">
        This application predicts student dropout risk using a supervised machine learning model
        and provides an interface for single-student form input or batch CSV uploads. Results are
        sorted by predicted risk and can be exported as a CSV. The initial approach uses a Random Forest classifier to capture non-linear relationships
        and interactions across categorical and numerical features. 
      </p>

      <hr class="mb-4">

      <div class="card shadow-sm mb-4">
        <div class="card-body">
          <h2 class="h4">Dataset</h2>
          <p class="mb-2">
            Source: <a href="https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success" target="_blank" rel="noopener">UCI ML Repository — Predict Students Dropout and Academic Success</a>
          </p>
          <ul class="list-group list-group-flush">
            <li class="list-group-item px-0"><strong>Rows:</strong> 4,424</li>
            <li class="list-group-item px-0"><strong>Total Features:</strong> 36</li>
            <li class="list-group-item px-0"><strong>Preliminarily Relevant Features:</strong> ~19</li>
            <li class="list-group-item px-0"><strong>Type:</strong> Tabular</li>
          </ul>

          <div class="accordion mt-3" id="featuresAccordion">
            <div class="accordion-item">
              <h2 class="accordion-header" id="headingFeatures">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFeatures" aria-expanded="false" aria-controls="collapseFeatures">
                  Example features
                </button>
              </h2>
              <div id="collapseFeatures" class="accordion-collapse collapse" aria-labelledby="headingFeatures" data-bs-parent="#featuresAccordion">
                <div class="accordion-body">
                  <ul class="mb-0">
                    <li>Marital status, Course, Previous qualification, GDP</li>
                    <li>Daytime/evening attendance, Mother’s qualification, Target, International</li>
                    <li>Nationality, Father’s qualification, Displaced, Unemployment rate</li>
                    <li>Educational special needs, Debtor, Gender, Inflation rate</li>
                    <li>Tuition fees up to date, Scholarship holder, Age at enrollment</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card shadow-sm mb-4">
        <div class="card-body">
          <h2 class="h4">App Functionality</h2>
          <ul class="mb-3">
            <li><strong>Single-student form:</strong> Client-side validation with clear messaging.</li>
            <li><strong>Batch CSV upload:</strong> Errors listed in a table with guidance per-row.</li>
            <li><strong>Results:</strong> Sorted by predicted dropout risk (highest first); optional pie chart.</li>
            <li><strong>Export:</strong> Download processed results as CSV.</li>
          </ul>

          <h3 class="h5">Explicit Features</h3>
          <div class="row g-2">
            <div class="col-sm-6 col-lg-3">
              <div class="badge bg-primary-subtle border border-primary text-primary w-100 py-2">Form processing</div>
            </div>
            <div class="col-sm-6 col-lg-3">
              <div class="badge bg-success-subtle border border-success text-success w-100 py-2">CSV processing</div>
            </div>
            <div class="col-sm-6 col-lg-3">
              <div class="badge bg-warning-subtle border border-warning text-warning w-100 py-2">Error validation</div>
            </div>
            <div class="col-sm-6 col-lg-3">
              <div class="badge bg-info-subtle border border-info text-info w-100 py-2">Data exporting</div>
            </div>
          </div>
        </div>
      </div>

      <div class="card shadow-sm">
        <div class="card-body">
          <h2 class="h4">Tools & Technologies</h2>
          <div class="row">
            <div class="col-md-6">
              <ul class="list-group list-group-flush">
                <li class="list-group-item px-0"><strong>Frontend:</strong> Nuxt.js (Vue, HTML, CSS, JS)</li>
                <li class="list-group-item px-0"><strong>Backend:</strong> Flask</li>
              </ul>
            </div>
            <div class="col-md-6">
              <ul class="list-group list-group-flush">
                <li class="list-group-item px-0"><strong>SSR/Process Manager:</strong> pm2</li>
                <li class="list-group-item px-0"><strong>Hosting:</strong> Netlify (frontend) and Render (backend)</li>
              </ul>
            </div>
          </div>
          <div class="text-muted small mt-3">Author: Benjamin Hislop (900896194)</div>
        </div>
      </div>
    </div>
  </div>
</template>

<!-- <style scoped>
h1, .h1, .h2, .h3, .h4, .h5 {
  scroll-margin-top: 6rem;
}
</style> -->