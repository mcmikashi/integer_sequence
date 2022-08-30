<script>
  import fetch from "cross-fetch";
  import Form from "./UI/Form.svelte";
  import Current from "./UI/Current.svelte";
  import History from "./UI/History.svelte";
  import Alert from "./UI/Alert.svelte";
  export let sequence_type = "fibonacci";
  let currentIndex = null;
  let currentResult = null;
  let historyArray = [];
  let arrayAlert = [];

  function setCurrentIndex(event) {
    updateHistory();
    currentIndex = event.detail.index;
    currentResult = null;
    getResultOfIndex(currentIndex);
  }

  function updateHistory() {
    let newID = new Date().getTime();
    if (currentIndex != null) {
      historyArray = [
        ...historyArray,
        { id: newID, index: currentIndex, result: currentResult },
      ];
    }
  }

  async function getResultOfIndex(index) {
    try {
      const res = await fetch(
        `${
          import.meta.env.VITE_REST_API_URL
        }sequence/api/${sequence_type}/${index}`
      );
      const jsonResponse = await res.json();
      if (res.ok) {
        currentResult = jsonResponse.result;
      } else {
        throw new Error(jsonResponse);
      }
    } catch (error) {
      currentIndex = null;
      let newID = new Date().getTime();
      arrayAlert = [
        ...arrayAlert,
        {
          id: newID,
          title: "Error",
          message: "The server is not responding correctly.",
        },
      ];
    }
  }
</script>

<h1 class="text-upper text-center">{sequence_type} sequence</h1>
<section id="alert-section">
  {#if arrayAlert.length != 0}
    <Alert {arrayAlert} />
  {/if}
</section>
<Form on:index={setCurrentIndex} />
{#if currentIndex != null}
  <Current bind:currentIndex bind:currentResult />
{/if}
{#if historyArray.length != 0}
  <History bind:historyArray />
{/if}
