<script>
  import { onMount } from "svelte";
  import fetch from "cross-fetch";
  import { Grid, Row, Column } from "carbon-components-svelte";
  import Fact from "./UI/Fact.svelte";
  const FACTSTYPES = ["trivia", "math", "date", "year"];
  const DEFAULTFACTS = [
    "44 is the number of candles in a box of Hanukkah candles.",
    "44 is a tribonacci number, a happy number, an octahedral number and a palindromic number.",
    "February 13th is the day in 1934 that the Soviet steamship Cheliuskin sinks in the Arctic Ocean.",
    "44 is the year that Pomponius Mela writes De situ orbis, a geography of the Earth.",
  ];
  let factsArray = [];

  onMount(async () => {
    for (let index = 0; index < FACTSTYPES.length; index++) {
      try {
        const res = await fetch(
          `http://numbersapi.com/random/${FACTSTYPES[index]}`
        );
        const textResponse = await res.text();
        if (res.ok) {
          factsArray = [
            ...factsArray,
            { facttype: FACTSTYPES[index], fact: textResponse },
          ];
        } else {
          throw new Error(textResponse);
        }
      } catch (error) {
        factsArray = [
          ...factsArray,
          { facttype: FACTSTYPES[index], fact: DEFAULTFACTS[index] },
        ];
      }
    }
  });
</script>

<Grid>
  <Row>
    {#if factsArray}
      {#each factsArray as facstItem}
        <Column>
          <Fact factsType={facstItem.facttype} facts={facstItem.fact} />
        </Column>
      {/each}
    {/if}
  </Row>
</Grid>
