<script>
  import { Tile } from "carbon-components-svelte";
  export let factsType = "trivia";
  export let facts;
</script>

<h2>{factsType}</h2>

<Tile light class="fact-tile">
  {facts}
</Tile>

<style>
  h2 {
    text-align: center;
    text-transform: uppercase;
  }
</style>
