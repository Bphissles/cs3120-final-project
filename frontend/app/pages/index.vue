<script setup>
import { ref, reactive, computed } from 'vue'

useHead({ title: 'Home | Student Dropout Risk Predictor' })

// --- State ---
const loading = ref(false)
const error = ref(null)
const success = ref(null)
const predictionResult = ref(null)
const batchResults = ref(null)

// API Base URL - in production this would be an env var
const API_URL = 'http://127.0.0.1:5000/api'

// --- Form Schema ---
// Define all fields expected by the model
const formFields = [
  { name: 'Marital status', type: 'number', default: 1, group: 'Demographic' },
  { name: 'Application mode', type: 'number', default: 17, group: 'Academic' },
  { name: 'Application order', type: 'number', default: 5, group: 'Academic' },
  { name: 'Course', type: 'number', default: 171, group: 'Academic' },
  { name: 'Daytime/evening attendance', type: 'number', default: 1, group: 'Academic' },
  { name: 'Previous qualification', type: 'number', default: 1, group: 'Academic' },
  { name: 'Previous qualification (grade)', type: 'number', step: '0.1', default: 122.0, group: 'Academic' },
  { name: 'Nacionality', type: 'number', default: 1, group: 'Demographic' },
  { name: 'Mother\'s qualification', type: 'number', default: 19, group: 'Socioeconomic' },
  { name: 'Father\'s qualification', type: 'number', default: 12, group: 'Socioeconomic' },
  { name: 'Mother\'s occupation', type: 'number', default: 5, group: 'Socioeconomic' },
  { name: 'Father\'s occupation', type: 'number', default: 9, group: 'Socioeconomic' },
  { name: 'Admission grade', type: 'number', step: '0.1', default: 127.3, group: 'Academic' },
  { name: 'Displaced', type: 'number', default: 1, group: 'Demographic' },
  { name: 'Educational special needs', type: 'number', default: 0, group: 'Demographic' },
  { name: 'Debtor', type: 'number', default: 0, group: 'Socioeconomic' },
  { name: 'Tuition fees up to date', type: 'number', default: 1, group: 'Socioeconomic' },
  { name: 'Gender', type: 'number', default: 1, group: 'Demographic' },
  { name: 'Scholarship holder', type: 'number', default: 0, group: 'Socioeconomic' },
  { name: 'Age at enrollment', type: 'number', default: 20, group: 'Demographic' },
  { name: 'International', type: 'number', default: 0, group: 'Demographic' },
  { name: 'Curricular units 1st sem (credited)', type: 'number', default: 0, group: 'Performance (1st Sem)' },
  { name: 'Curricular units 1st sem (enrolled)', type: 'number', default: 0, group: 'Performance (1st Sem)' },
  { name: 'Curricular units 1st sem (evaluations)', type: 'number', default: 0, group: 'Performance (1st Sem)' },
  { name: 'Curricular units 1st sem (approved)', type: 'number', default: 0, group: 'Performance (1st Sem)' },
  { name: 'Curricular units 1st sem (grade)', type: 'number', step: '0.1', default: 0.0, group: 'Performance (1st Sem)' },
  { name: 'Curricular units 1st sem (without evaluations)', type: 'number', default: 0, group: 'Performance (1st Sem)' },
  { name: 'Curricular units 2nd sem (credited)', type: 'number', default: 0, group: 'Performance (2nd Sem)' },
  { name: 'Curricular units 2nd sem (enrolled)', type: 'number', default: 0, group: 'Performance (2nd Sem)' },
  { name: 'Curricular units 2nd sem (evaluations)', type: 'number', default: 0, group: 'Performance (2nd Sem)' },
  { name: 'Curricular units 2nd sem (approved)', type: 'number', default: 0, group: 'Performance (2nd Sem)' },
  { name: 'Curricular units 2nd sem (grade)', type: 'number', step: '0.1', default: 0.0, group: 'Performance (2nd Sem)' },
  { name: 'Curricular units 2nd sem (without evaluations)', type: 'number', default: 0, group: 'Performance (2nd Sem)' },
  { name: 'Unemployment rate', type: 'number', step: '0.1', default: 10.8, group: 'Macroeconomic' },
  { name: 'Inflation rate', type: 'number', step: '0.1', default: 1.4, group: 'Macroeconomic' },
  { name: 'GDP', type: 'number', step: '0.01', default: 1.74, group: 'Macroeconomic' }
]

// Initialize form data with defaults
const formData = reactive({})
formFields.forEach(field => {
  formData[field.name] = field.default
})

// Group fields for display
const fieldGroups = computed(() => {
  const groups = {}
  formFields.forEach(field => {
    if (!groups[field.group]) groups[field.group] = []
    groups[field.group].push(field)
  })
  return groups
})

// --- Actions ---

const handleSinglePredict = async () => {
  loading.value = true
  error.value = null
  predictionResult.value = null
  
  try {
    const response = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })

    const data = await response.json()
    
    if (!response.ok) throw new Error(data.error || 'Prediction failed')
    
    predictionResult.value = data[0]
    success.value = 'Prediction successful!'
    
    // Scroll to result
    setTimeout(() => {
      document.getElementById('prediction-result')?.scrollIntoView({ behavior: 'smooth' })
    }, 100)
    
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

const fileInput = ref(null)

const handleFileUpload = async (event) => {
  const file = event.target.files[0]
  if (!file) return

  loading.value = true
  error.value = null
  batchResults.value = null
  
  const formDataObj = new FormData()
  formDataObj.append('file', file)

  try {
    const response = await fetch(`${API_URL}/predict-file`, {
      method: 'POST',
      body: formDataObj,
    })

    const data = await response.json()
    
    if (!response.ok) throw new Error(data.error || 'Batch processing failed')
    
    batchResults.value = data
    success.value = `Processed ${data.length} records successfully!`
    
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
    // Reset file input
    if (fileInput.value) fileInput.value.value = ''
  }
}

const downloadCSV = (data) => {
  if (!data || !data.length) return
  
  // Get headers
  const headers = Object.keys(data[0])
  const csvContent = [
    headers.join(','),
    ...data.map(row => headers.map(header => {
      // Handle values that might contain commas
      const val = row[header]
      return typeof val === 'string' && val.includes(',') ? `"${val}"` : val
    }).join(','))
  ].join('\n')
  
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.setAttribute('href', url)
  link.setAttribute('download', 'predictions.csv')
  link.style.visibility = 'hidden'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const getRiskBadgeClass = (prediction) => {
  if (prediction === 'Dropout') return 'bg-danger'
  if (prediction === 'Enrolled') return 'bg-warning text-dark'
  return 'bg-success'
}
</script>

<template>
  <div class="container py-5">
    <div class="row align-items-center mb-5">
      <div class="col-lg-8">
        <h1 class="display-5 fw-bold mb-3">Predict Student Dropout Risk</h1>
        <p class="lead mb-4">
          Utilize our Random Forest model to identify students at risk. 
          Choose between single-student prediction or batch processing via CSV.
        </p>
        <div class="d-flex gap-2 flex-wrap">
          <a href="#single-prediction" class="btn btn-primary">Start Prediction</a>
          <a href="/student_template.csv" download class="btn btn-outline-secondary">
            <i class="bi bi-download me-1"></i> Download Template CSV
          </a>
        </div>
      </div>
    </div>

    <!-- Alerts -->
    <div v-if="error" class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error }}
      <button type="button" class="btn-close" @click="error = null"></button>
    </div>
    <div v-if="success" class="alert alert-success alert-dismissible fade show" role="alert">
      {{ success }}
      <button type="button" class="btn-close" @click="success = null"></button>
    </div>

    <!-- Batch Upload Section -->
    <div class="card shadow-sm mb-5">
      <div class="card-header bg-light">
        <h3 class="h5 mb-0">Batch CSV Upload</h3>
      </div>
      <div class="card-body">
        <div class="row align-items-center">
          <div class="col-md-8">
            <p class="mb-0 text-muted">
              Upload a CSV file containing student data. The file should follow the template format.
              Results will be displayed below and can be exported.
            </p>
          </div>
          <div class="col-md-4 text-end">
             <input 
              type="file" 
              ref="fileInput"
              class="form-control" 
              accept=".csv"
              @change="handleFileUpload"
              :disabled="loading"
            >
          </div>
        </div>

        <!-- Batch Results Table -->
        <div v-if="batchResults" class="mt-4">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 class="h6 mb-0">Results ({{ batchResults.length }} students)</h4>
            <button class="btn btn-sm btn-success" @click="downloadCSV(batchResults)">
              Export Results
            </button>
          </div>
          <div class="table-responsive" style="max-height: 400px;">
            <table class="table table-sm table-hover table-bordered">
              <thead class="table-light sticky-top">
                <tr>
                  <th>ID</th>
                  <th>Prediction</th>
                  <th>Confidence</th>
                  <th>Dropout Risk</th>
                  <th>Course</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(result, index) in batchResults" :key="index">
                  <td>{{ index + 1 }}</td>
                  <td>
                    <span class="badge" :class="getRiskBadgeClass(result.prediction)">
                      {{ result.prediction }}
                    </span>
                  </td>
                  <td>{{ (result.confidence * 100).toFixed(1) }}%</td>
                  <td>
                    <div class="progress" style="height: 20px;">
                      <div 
                        class="progress-bar bg-danger" 
                        role="progressbar" 
                        :style="{ width: (result.probabilities?.Dropout || 0) * 100 + '%' }"
                        :aria-valuenow="(result.probabilities?.Dropout || 0) * 100" 
                        aria-valuemin="0" 
                        aria-valuemax="100"
                      >
                        {{ ((result.probabilities?.Dropout || 0) * 100).toFixed(0) }}%
                      </div>
                    </div>
                  </td>
                  <td>{{ result.Course }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <hr class="my-5">

    <!-- Single Prediction Form -->
    <div id="single-prediction" class="card shadow-sm mb-4">
      <div class="card-header bg-primary text-white">
        <h3 class="h5 mb-0">Single Student Prediction</h3>
      </div>
      <div class="card-body">
        <form @submit.prevent="handleSinglePredict">
          <div class="row g-3">
            
            <div v-for="(fields, groupName) in fieldGroups" :key="groupName" class="col-12">
              <h4 class="h6 text-primary border-bottom pb-2 mt-3">{{ groupName }}</h4>
              <div class="row g-3">
                <div v-for="field in fields" :key="field.name" class="col-md-6 col-lg-4">
                  <label :for="field.name" class="form-label small fw-bold text-muted">{{ field.name }}</label>
                  <input 
                    :id="field.name"
                    v-model.number="formData[field.name]" 
                    :type="field.type" 
                    :step="field.step || '1'"
                    class="form-control form-control-sm"
                    required
                  >
                </div>
              </div>
            </div>

            <div class="col-12 mt-4 text-center">
              <button type="submit" class="btn btn-primary btn-lg px-5" :disabled="loading">
                <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                {{ loading ? 'Processing...' : 'Predict Dropout Risk' }}
              </button>
            </div>
          </div>
        </form>

        <!-- Single Result Display -->
        <div v-if="predictionResult" id="prediction-result" class="mt-5 p-4 bg-light border rounded text-center animate__animated animate__fadeIn">
          <h4 class="mb-3">Prediction Result</h4>
          <div class="display-1 mb-3">
            <span class="badge rounded-pill" :class="getRiskBadgeClass(predictionResult.prediction)">
              {{ predictionResult.prediction }}
            </span>
          </div>
          <p class="lead">
            Confidence: <strong>{{ (predictionResult.confidence * 100).toFixed(1) }}%</strong>
          </p>
          
          <div class="row justify-content-center mt-4">
            <div class="col-md-6">
              <h5 class="h6">Probability Distribution</h5>
              <div v-for="(prob, label) in predictionResult.probabilities" :key="label" class="mb-2">
                <div class="d-flex justify-content-between small mb-1">
                  <span>{{ label }}</span>
                  <span>{{ (prob * 100).toFixed(1) }}%</span>
                </div>
                <div class="progress" style="height: 10px;">
                  <div 
                    class="progress-bar" 
                    :class="getRiskBadgeClass(label)" 
                    role="progressbar" 
                    :style="{ width: prob * 100 + '%' }"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
    
  </div>
</template>
