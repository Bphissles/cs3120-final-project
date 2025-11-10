<script setup>
useHead({ title: 'Home | Student Dropout Risk Predictor' })
</script>

<template>
  <div class="container py-5">
    <div class="row align-items-center mb-4">
      <div class="col-lg-8">
        <h1 class="display-5 fw-bold mb-3">Predict Student Dropout Risk</h1>
        <p class="lead mb-4">
          Enter a single student's details or upload a CSV to predict dropout risk. Results are
          ranked by risk and can be exported for follow-up.
        </p>
        <div class="d-flex gap-2 flex-wrap">
          <NuxtLink to="/about" class="btn btn-primary">Learn about the project</NuxtLink>
          <a href="https://github.com/Bphissles/cs3120-final-project" class="btn btn-secondary" target="_blank">View notebook on GitHub</a>
          <button class="btn btn-outline-secondary" type="button" disabled aria-disabled="true" title="Coming soon">
            Upload CSV (coming soon)
          </button>
        </div>
      </div>
    </div>
    <hr class="mb-4">

    <div class="row g-3 mb-4">
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h2 class="h5 mb-2">Single-student form</h2>
            <p class="mb-0">Validate inputs and get an immediate risk prediction.</p>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h2 class="h5 mb-2">CSV batch upload</h2>
            <p class="mb-0">Process multiple students at once with row-level error feedback.</p>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h2 class="h5 mb-2">Ranked results</h2>
            <p class="mb-0">See highest-risk students first to prioritize intervention.</p>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h2 class="h5 mb-2">Export</h2>
            <p class="mb-0">Download predictions as CSV for sharing or analysis.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="card shadow-sm mb-4">
      <div class="card-body">
        <h2 class="h4">How it will work</h2>
        <ol class="mt-2 mb-0 ps-3">
          <li>Choose: fill a form for one student or upload a CSV template.</li>
          <li>Validate inputs; fix any highlighted errors.</li>
          <li>Submit to get predictions ranked by dropout risk.</li>
          <li>Export the results as CSV for your records.</li>
        </ol>
      </div>
    </div>

    <div class="card shadow-sm mb-4">
      <div class="card-body">
        <h2 class="h4 mb-2">Whats going on under the hood (Kind of)</h2>
<pre>
  param_dist = {
    'n_estimators': randint(100, 500),
    'max_depth': randint(3, 15),
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 5)
  }


  # Create a random forest classifier
  rf = RandomForestClassifier(random_state=42, n_jobs=-1)

  # Use random search to find the best hyperparameters
  rand_search = RandomizedSearchCV(
    rf, param_distributions=param_dist,
    n_iter=10, cv=5, scoring='accuracy',
    n_jobs=-1, random_state=42

</pre>
      </div>
    </div>

  </div>
</template>