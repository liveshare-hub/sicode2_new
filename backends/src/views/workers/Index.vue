<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-8">
        <router-link
          :to="{ name: 'workers.create' }"
          class="btn btn-primary btn-sm rounded shadow mb-3"
          >Add</router-link
        >

        <div class="card rounded shadow">
          <div class="card-header">List Perusahaan</div>
          <div class="card-body">
            <table class="table">
              <thead>
                <tr>
                  <th>NPP</th>
                  <th>NAMA PERUSAHAAN</th>
                  <th>ACTION</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(data, index) in data1" :key="index">
                  <td>{{ data.npp }}</td>
                  <td>{{ data.nama }}</td>
                  <td>
                    <div class="btn-group">
                      <router-link
                        :to="{ name: 'workers.edit', params: { id: index } }"
                        class="btn btn-outline-info btn-sm"
                        >Edit</router-link
                      >
                      <button class="btn btn-sm btn-outline-danger">
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { onMounted, ref } from "vue";

export default {
  data() {
    return {
      data1: "",
    };
  },
  mounted() {
    axios
      .post("http://localhost:8000/api/graphql", {
        query: "{allCompanies{npp nama}}",
      })
      .then((response) => (this.data1 = response.data.data.allCompanies))
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
};
</script>