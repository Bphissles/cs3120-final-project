<script setup>
import { reactive, computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Object,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  },
  categoricalOptions: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['update:modelValue', 'submit'])

const formData = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const handleSubmit = () => {
  emit('submit')
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <div class="row g-3">
      
      <!-- Demographic & Socioeconomic -->
      <div class="col-md-12">
        <h3 class="h4 text-primary border-bottom pb-2">Student Profile</h3>
      </div>
      
      <div class="col-md-6">
        <label for="Course" class="form-label small fw-bold text-muted">Area of Study</label>
        <select id="Course" v-model.number="formData['Course']" class="form-select" required>
          <option v-for="(label, value) in categoricalOptions.course" :key="value" :value="value">{{ label }}</option>
        </select>
        <div class="form-text small fst-italic">The degree program the student is enrolled in.</div>
      </div>
      
      <div class="col-md-3">
        <label for="Age" class="form-label small fw-bold text-muted">Age at enrollment</label>
        <input id="Age" v-model.number="formData['Age at enrollment']" type="number" class="form-control" required>
        <div class="form-text small fst-italic">Age at entry.</div>
      </div>

      <div class="col-md-3">
        <label for="Tuition" class="form-label small fw-bold text-muted">Tuition Up to Date?</label>
        <select id="Tuition" v-model.number="formData['Tuition fees up to date']" class="form-select" required>
          <option v-for="(label, value) in categoricalOptions.yesNo" :key="value" :value="value">{{ label }}</option>
        </select>
        <div class="form-text small fst-italic">Payments current?</div>
      </div>

      <!-- Academic Performance -->
      <div class="col-md-12 mt-4">
        <h3 class="h4 text-primary border-bottom pb-2">Academic Performance</h3>
      </div>

      <!-- 1st Semester -->
      <div class="col-md-6">
        <div class="card bg-light border-0 h-100">
          <div class="card-body">
            <h4 class="card-title text-muted mb-3">1st Semester</h4>
            <div class="row g-3">
              <div class="col-12">
                <label for="evaluations-1st" class="form-label small fw-bold">Evaluations</label>
                <input id="evaluations-1st" v-model.number="formData['Curricular units 1st sem (evaluations)']" type="number" class="form-control form-control-sm">
                <div class="form-text x-small">Total exams & evaluations taken.</div>
              </div>
              <div class="col-6">
                <label for="approved-1st" class="form-label small fw-bold">Approved Units</label>
                <input id="approved-1st" v-model.number="formData['Curricular units 1st sem (approved)']" type="number" class="form-control form-control-sm">
                <div class="form-text x-small">Classes passed.</div>
              </div>
              <div class="col-6">
                <label for="grade-1st" class="form-label small fw-bold">Grade Average</label>
                <input id="grade-1st" v-model.number="formData['Curricular units 1st sem (grade)']" type="number" step="0.1" class="form-control form-control-sm">
                <div class="form-text x-small">Scale 0-20.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2nd Semester -->
      <div class="col-md-6">
        <div class="card bg-light border-0 h-100">
          <div class="card-body">
            <h4 class="card-title text-muted mb-3">2nd Semester</h4>
            <div class="row g-3">
              <div class="col-6">
                <label for="enrolled-2nd" class="form-label small fw-bold">Units Enrolled</label>
                <input id="enrolled-2nd" v-model.number="formData['Curricular units 2nd sem (enrolled)']" type="number" class="form-control form-control-sm">
                <div class="form-text x-small">Classes taken.</div>
              </div>
              <div class="col-6">
                <label for="evaluations-2nd" class="form-label small fw-bold">Evaluations</label>
                <input id="evaluations-2nd" v-model.number="formData['Curricular units 2nd sem (evaluations)']" type="number" class="form-control form-control-sm">
                <div class="form-text x-small">Exams taken.</div>
              </div>
              <div class="col-6">
                <label for="approved-2nd" class="form-label small fw-bold">Approved Units</label>
                <input id="approved-2nd" v-model.number="formData['Curricular units 2nd sem (approved)']" type="number" class="form-control form-control-sm">
                <div class="form-text x-small">Classes passed.</div>
              </div>
              <div class="col-6">
                <label for="grade-2nd" class="form-label small fw-bold">Grade Average</label>
                <input id="grade-2nd" v-model.number="formData['Curricular units 2nd sem (grade)']" type="number" step="0.1" class="form-control form-control-sm">
                <div class="form-text x-small">Scale 0-20.</div>
              </div>
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
</template>

<style scoped>
.x-small {
  font-size: 0.75rem;
}
</style>
