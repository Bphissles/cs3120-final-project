<script setup>
import { computed } from 'vue'

const props = defineProps({
  results: {
    type: Array,
    default: () => []
  },
  categoricalOptions: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['download'])

const getRiskBadgeClass = (prediction) => {
  if (prediction === 'Dropout') return 'bg-danger'
  if (prediction === 'Enrolled') return 'bg-warning text-dark'
  return 'bg-success'
}

// Chart Data
// Chart structure developed with help from Gemini 3
const chartData = computed(() => {
  if (!props.results || props.results.length === 0) return null
  
  const counts = {
    Dropout: 0,
    Enrolled: 0,
    Graduate: 0
  }
  
  props.results.forEach(r => {
    if (counts[r.prediction] !== undefined) {
      counts[r.prediction]++
    }
  })
  
  return counts
})

// Simple SVG Pie Chart Component logic
const pieChartPaths = computed(() => {
  if (!chartData.value) return []
  
  const total = props.results.length
  if (total === 0) return []
  
  const slices = []
  let cumulativePercent = 0
  
  const colors = {
    Dropout: '#dc3545', // danger
    Enrolled: '#ffc107', // warning
    Graduate: '#198754' // success
  }
  
  // Order: Graduate, Enrolled, Dropout
  const categories = ['Graduate', 'Enrolled', 'Dropout']
  
  categories.forEach(cat => {
    const count = chartData.value[cat]
    if (count > 0) {
      const percent = count / total
      const startPercent = cumulativePercent
      const endPercent = cumulativePercent + percent
      
      // Calculate coordinates
      const x1 = Math.cos(2 * Math.PI * startPercent)
      const y1 = Math.sin(2 * Math.PI * startPercent)
      const x2 = Math.cos(2 * Math.PI * endPercent)
      const y2 = Math.sin(2 * Math.PI * endPercent)
      
      // Large arc flag
      const largeArcFlag = percent > 0.5 ? 1 : 0
      
      // Path command
      // M 0 0 : Move to center
      // L x1 y1 : Line to start point
      // A 1 1 0 largeArcFlag 1 x2 y2 : Arc to end point
      // Z : Close path
      
      // Note: SVG coordinates usually start from 3 o'clock. We want 12 o'clock, so we rotate -90deg in CSS
      const pathData = `M 0 0 L ${x1} ${y1} A 1 1 0 ${largeArcFlag} 1 ${x2} ${y2} Z`
      
      slices.push({
        path: pathData,
        color: colors[cat],
        label: cat,
        count: count,
        percent: (percent * 100).toFixed(1)
      })
      
      cumulativePercent += percent
    }
  })
  
  // If only one category (100%), the arc command fails. Handle full circle.
  if (slices.length === 1 && total > 0) {
    return [{
      path: 'M 0 0 m -1 0 a 1 1 0 1 0 2 0 a 1 1 0 1 0 -2 0', // Full circle
      color: slices[0].color,
      label: slices[0].label,
      count: slices[0].count,
      percent: '100.0'
    }]
  }
  
  return slices
})

</script>

<template>
  <div v-if="results" class="mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3 class="h4 mb-0">Results ({{ results.length }} students)</h3>
      <button class="btn btn-sm btn-success" @click="emit('download')">
        Export Results
      </button>
    </div>

    <!-- Pie Chart Section (Only if > 10 records) -->
    <div v-if="results.length > 10" class="card mb-4 border-0 bg-light">
      <div class="card-body">
        <div class="row align-items-center">
          <div class="col-md-4 text-center">
            <div class="pie-chart-container mx-auto">
              <svg viewBox="-1.1 -1.1 2.2 2.2" class="pie-chart">
                <path 
                  v-for="(slice, index) in pieChartPaths" 
                  :key="index" 
                  :d="slice.path" 
                  :fill="slice.color"
                  stroke="white"
                  stroke-width="0.02"
                />
              </svg>
            </div>
          </div>
          <div class="col-md-8">
            <h5 class="h4 mb-3">Distribution Overview</h5>
            <ul class="list-unstyled">
              <li v-for="(slice, index) in pieChartPaths" :key="index" class="d-flex align-items-center mb-2">
                <span class="legend-dot me-2" :style="{ backgroundColor: slice.color }"></span>
                <span class="fw-bold me-2">{{ slice.label }}:</span>
                <span>{{ slice.count }} students ({{ slice.percent }}%)</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
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
            <th>Area of Study</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(result, index) in results" :key="index">
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
</template>

<style scoped>
.pie-chart-container {
  width: 150px;
  height: 150px;
}
.pie-chart {
  transform: rotate(-90deg); /* Start at 12 o'clock */
}
.legend-dot {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
}
</style>
