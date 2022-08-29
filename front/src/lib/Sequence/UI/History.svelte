<script>
  import { DataTable } from "carbon-components-svelte";
  export let historyArray = [];
</script>

<DataTable
  zebra
  stickyHeader
  sortable
  headers={[
    { key: "index", value: "Index" },
    { key: "result", value: "Result" },
  ]}
  rows={historyArray}
>
  <strong slot="title">History search</strong>
</DataTable>
