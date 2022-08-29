<script>
    import {
        Grid,
    } from "carbon-components-svelte";
    import ResultRow from "./ResultRow.svelte";
    export let  currentIndex; 
    export let currentResult;
</script>

<h2>Current search</h2>
<Grid padding>
    <ResultRow bind:index={currentIndex} bind:result={currentResult}/>
</Grid>