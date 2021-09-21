<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-8">
        <router-link
          :to="{ name: 'workers.index' }"
          class="btn btn-info btn-sm rounded shadow mb-3"
          >Back</router-link
        >

        <div class="card rounded shadow">
          <div class="card-header">Tambah Perusahaan</div>
          <div class="card-body">
            <form>
              <div class="mb-3">
                <label for="npp">NPP</label>
                <input
                  type="text"
                  class="form-control"
                  id="npp"
                  placeholder="Input NPP"
                />
                <div class="text-danger">Validation Message</div>
              </div>
              <div class="mb-3">
                <label for="nama">NAMA</label>
                <input
                  type="text"
                  class="form-control"
                  id="nama"
                  placeholder="Input Nama Perusahaan"
                />
                <div class="text-danger">Validation Message</div>
              </div>
              <div class="mt-2">
                <button class="btn btn-outline-primary">Submit</button>
              </div>
            </form>
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