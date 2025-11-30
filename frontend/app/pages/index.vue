<script setup>
import { ref, reactive, computed } from 'vue'

useHead({ title: 'Home | Student Dropout Risk Predictor' })

// --- State ---
const loading = ref(false)
const error = ref(null)
const success = ref(null)
const predictionResult = ref(null)
const batchResults = ref(null)

// Get runtime config
const config = useRuntimeConfig()
const API_URL = config.public.apiBase

// --- Categorical Options ---
const categoricalOptions = {
  maritalStatus: {
    1: 'Single', 2: 'Married', 3: 'Widower', 4: 'Divorced', 5: 'Facto union', 6: 'Legally separated'
  },
  applicationMode: {
    1: '1st phase - general contingent', 2: 'Ordinance No. 612/93', 5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses', 10: 'Ordinance No. 854-B/99', 15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)', 17: '2nd phase - general contingent',
    18: '3rd phase - general contingent', 26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)', 39: 'Over 23 years old', 42: 'Transfer',
    43: 'Change of course', 44: 'Technological specialization diploma holders', 51: 'Change of institution/course',
    53: 'Short cycle diploma holders', 57: 'Change of institution/course (International)'
  },
  course: {
    33: 'Biofuel Production Technologies', 171: 'Animation and Multimedia Design', 8014: 'Social Service (evening attendance)',
    9003: 'Agronomy', 9070: 'Communication Design', 9085: 'Veterinary Nursing', 9119: 'Informatics Engineering',
    9130: 'Equinculture', 9147: 'Management', 9238: 'Social Service', 9254: 'Tourism', 9500: 'Nursing',
    9556: 'Oral Hygiene', 9670: 'Advertising and Marketing Management', 9773: 'Journalism and Communication',
    9853: 'Basic Education', 9991: 'Management (evening attendance)'
  },
  daytimeEvening: {
    1: 'Daytime', 0: 'Evening'
  },
  qualification: {
    1: 'Secondary education', 2: 'Higher education - bachelor\'s degree', 3: 'Higher education - degree',
    4: 'Higher education - master\'s', 5: 'Higher education - doctorate', 6: 'Frequency of higher education',
    9: '12th year of schooling - not completed', 10: '11th year of schooling - not completed',
    12: 'Other - 11th year of schooling', 14: '10th year of schooling', 15: '10th year of schooling - not completed',
    19: 'Basic education 3rd cycle (9th/10th/11th year) or equiv.', 38: 'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
    39: 'Technological specialization course', 40: 'Higher education - degree (1st cycle)',
    42: 'Professional higher technical course', 43: 'Higher education - master (2nd cycle)'
  },
  nationality: {
    1: 'Portuguese', 2: 'German', 6: 'Spanish', 11: 'Italian', 13: 'Dutch', 14: 'English', 17: 'Lithuanian',
    21: 'Angolan', 22: 'Cape Verdean', 24: 'Guinean', 25: 'Mozambican', 26: 'Santomean', 32: 'Turkish',
    41: 'Brazilian', 62: 'Romanian', 100: 'Moldova (Republic of)', 101: 'Mexican', 103: 'Ukrainian',
    105: 'Russian', 108: 'Cuban', 109: 'Colombian'
  },
  parentQualification: {
    1: 'Secondary Education - 12th Year of Schooling or Eq.', 2: 'Higher Education - Bachelor\'s Degree',
    3: 'Higher Education - Degree', 4: 'Higher Education - Master\'s', 5: 'Higher Education - Doctorate',
    6: 'Frequency of Higher Education', 9: '12th Year of Schooling - Not Completed',
    10: '11th Year of Schooling - Not Completed', 11: '7th Year (Old)', 12: 'Other - 11th Year of Schooling',
    13: '2nd year complementary high school course', 14: '10th Year of Schooling', 18: 'General commerce course',
    19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 20: 'Complementary High School Course',
    22: 'Technical-professional course', 25: 'Complementary High School Course - not concluded',
    26: '7th year of schooling', 27: '2nd cycle of the general high school course',
    29: '9th Year of Schooling - Not Completed', 30: '8th year of schooling',
    31: 'General Course of Administration and Commerce', 33: 'Supplementary Accounting and Administration',
    34: 'Unknown', 35: 'Can\'t read or write', 36: 'Can read without having a 4th year of schooling',
    37: 'Basic education 1st cycle (4th/5th year) or equiv.', 38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
    39: 'Technological specialization course', 40: 'Higher education - degree (1st cycle)',
    41: 'Specialized higher studies course', 42: 'Professional higher technical course',
    43: 'Higher Education - Master (2nd cycle)', 44: 'Higher Education - Doctorate (3rd cycle)'
  },
  occupation: {
    0: 'Student',
    1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    2: 'Specialists in Intellectual and Scientific Activities', 3: 'Intermediate Level Technicians and Professions',
    4: 'Administrative staff', 5: 'Personal Services, Security and Safety Workers and Sellers',
    6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    7: 'Skilled Workers in Industry, Construction and Craftsmen',
    8: 'Installation and Machine Operators and Assembly Workers', 9: 'Unskilled Workers',
    10: 'Armed Forces Professions', 90: 'Other Situation', 99: '(blank)',
    101: 'Armed Forces Officers', 102: 'Armed Forces Sergeants', 103: 'Other Armed Forces personnel',
    112: 'Directors of administrative and commercial services', 114: 'Hotel, catering, trade and other services directors',
    121: 'Specialists in the physical sciences, mathematics, engineering and related techniques',
    122: 'Health professionals', 123: 'teachers', 124: 'Specialists in finance, accounting, administrative organization, public and commercial relations',
    125: 'Specialists in information and communication technologies (ICT)',
    131: 'Intermediate level science and engineering technicians and professions',
    132: 'Technicians and professionals, of intermediate level of health',
    134: 'Intermediate level technicians from legal, social, sports, cultural and similar services',
    135: 'Information and communication technology technicians',
    141: 'Office workers, secretaries in general and data processing operators',
    143: 'Data, accounting, statistical, financial services and registry-related operators',
    144: 'Other administrative support staff', 151: 'personal service workers', 152: 'sellers',
    153: 'Personal care workers and the like', 154: 'Protection and security services personnel',
    161: 'Market-oriented farmers and skilled agricultural and animal production workers',
    163: 'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
    171: 'Skilled construction workers and the like, except electricians',
    172: 'Skilled workers in metallurgy, metalworking and similar',
    173: 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like',
    174: 'Skilled workers in electricity and electronics',
    175: 'Workers in food processing, woodworking, clothing and other industries and crafts',
    181: 'Fixed plant and machine operators', 182: 'assembly workers',
    183: 'Vehicle drivers and mobile equipment operators', 191: 'cleaning workers',
    192: 'Unskilled workers in agriculture, animal production, fisheries and forestry',
    193: 'Unskilled workers in extractive industry, construction, manufacturing and transport',
    194: 'Meal preparation assistants', 195: 'Street vendors (except food) and street service providers'
  },
  yesNo: {
    1: 'Yes', 0: 'No'
  },
  gender: {
    1: 'Male', 0: 'Female'
  }
}

// --- Form Schema ---
// Reduced to Top 10 most predictive features
const formFields = [
  { name: 'Course', type: 'select', options: categoricalOptions.course, default: 171, group: 'Academic' },
  { name: 'Age at enrollment', type: 'number', default: 20, group: 'Demographic', description: 'Age of student at enrollment' },
  { name: 'Tuition fees up to date', type: 'select', options: categoricalOptions.yesNo, default: 1, group: 'Socioeconomic', description: 'Are tuition fees paid up to date?' },
  
  // 1st Semester Performance
  { name: 'Curricular units 1st sem (evaluations)', type: 'number', default: 0, group: 'Performance (1st Sem)', description: 'Number of evaluations to curricular units in the 1st semester' },
  { name: 'Curricular units 1st sem (approved)', type: 'number', default: 0, group: 'Performance (1st Sem)', description: 'Number of curricular units approved in the 1st semester' },
  { name: 'Curricular units 1st sem (grade)', type: 'number', step: '0.1', default: 0.0, group: 'Performance (1st Sem)', description: 'Grade average in the 1st semester (between 0 and 20)' },

  // 2nd Semester Performance
  { name: 'Curricular units 2nd sem (enrolled)', type: 'number', default: 0, group: 'Performance (2nd Sem)', description: 'Number of curricular units enrolled in the 2nd semester' },
  { name: 'Curricular units 2nd sem (evaluations)', type: 'number', default: 0, group: 'Performance (2nd Sem)', description: 'Number of evaluations to curricular units in the 2nd semester' },
  { name: 'Curricular units 2nd sem (approved)', type: 'number', default: 0, group: 'Performance (2nd Sem)', description: 'Number of curricular units approved in the 2nd semester' },
  { name: 'Curricular units 2nd sem (grade)', type: 'number', step: '0.1', default: 0.0, group: 'Performance (2nd Sem)', description: 'Grade average in the 2nd semester (between 0 and 20)' }
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
      let val = row[header]
      
      // Special formatting for probabilities column
      if (header === 'probabilities' && row.prediction && row.confidence) {
        return `${row.prediction}: ${(row.confidence * 100).toFixed(0)}%`
      }
      
      // Handle objects (like probabilities if prediction/confidence missing)
      if (typeof val === 'object' && val !== null) {
        val = JSON.stringify(val).replace(/"/g, "'") // Simplify for CSV
      }
      
      // Handle values that might contain commas
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
                  <th>
                    Confidence 
                    <span class="text-muted small" title="The probability percentage that the model assigns to its top prediction." style="cursor: help;">
                      <i class="bi bi-question-circle"></i>
                    </span>
                  </th>
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
                  <td>
                    {{ categoricalOptions.course[result.Course] || result.Course }}
                  </td>
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
                  
                  <!-- Render Select for Categorical -->
                  <select
                    v-if="field.type === 'select'"
                    :id="field.name"
                    v-model.number="formData[field.name]"
                    class="form-select form-select-sm"
                    required
                  >
                    <option v-for="(label, value) in field.options" :key="value" :value="value">
                      {{ label }}
                    </option>
                  </select>

                  <!-- Render Input for Numeric -->
                  <input 
                    v-else
                    :id="field.name"
                    v-model.number="formData[field.name]" 
                    :type="field.type" 
                    :step="field.step || '1'"
                    class="form-control form-control-sm"
                    required
                  >
                  
                  <!-- Description/Tooltip -->
                  <div v-if="field.description" class="form-text text-muted small fst-italic">
                    {{ field.description }}
                  </div>
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
