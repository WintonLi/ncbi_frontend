<template>
  <div class="charts">
    <va-card>
      <va-content style="padding-left: 20px">
        <div class="row">
          <div class="flex md4 sm6 xs12">
            <va-input v-model="disease" placeholder="Input Disease" @keyup.enter="onSearch">
              <template #append>
                <va-button style="margin-right: 0" small @click="onSearch"> Search </va-button>
              </template>
            </va-input>
          </div>
        </div>
        <div class="row">
          <div class="flex md4 sm6 xs12">
            <div class="title title--warning mb-3">Years</div>
            <va-slider
              pins
              :step="1"
              :min="1990"
              :max="2022"
              track-label-visible
              v-model="years"
              @drag-end="onSearch"
              range
            >
            </va-slider>
          </div>
        </div>
      </va-content>
    </va-card>
    <div class="row">
      <div class="flex md12 xs12">
        <va-card v-if="lineChartDataGenerated" class="chart-widget">
          <va-card-title>{{ t('charts.lineChart') }}</va-card-title>
          <va-card-content>
            <va-chart :data="lineChartDataGenerated" type="line" />
          </va-card-content>
        </va-card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import bkClient from '../../../shared/backend-client'
  import { useI18n } from 'vue-i18n'
  import VaChart from '../../../components/va-charts/VaChart.vue'
  import { ref } from 'vue'
  const disease = ref('')
  const lineChartDataGenerated = ref({
    datasets: [{ label: 'Nothing to display yet', backgroundColor: 'hsla(220,80%,42%,0.7)', data: [] }],
    labels: [],
  })
  const years = ref([2015, 2022])
  const onSearch = () => {
    if (!disease.value) {
      return
    }
    console.log(`searching disease: ${disease.value}`)
    return bkClient
      .get('trend', { params: { disease: disease.value, min_yr: years.value[0], max_yr: years.value[1] } })
      .then((res) => {
        const data = res.data.map((d) => d.nPub)
        const range = res.data.map((d) => d.year)
        const label = `Number of publications mentioning ${disease.value}`
        lineChartDataGenerated.value = {
          datasets: [{ label: label, backgroundColor: 'hsla(220,80%,42%,0.7)', data: data }],
          labels: range,
        }
      })
  }

  // const lineChartDataGenerated = useChartData(lineChartData, 0.7)
  const { t } = useI18n()
</script>

<style lang="scss">
  .chart-widget {
    .va-card__content {
      height: 450px;
    }
  }
</style>
