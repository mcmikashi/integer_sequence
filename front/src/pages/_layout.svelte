<script>
    let theme = "g100"; // "white" | "g10" | "g80" | "g90" | "g100"
    $: document.documentElement.setAttribute("theme", theme);
    import Header from "../lib/UI/Header.svelte";
    import Footer  from "../lib/UI/Footer.svelte";
</script>
  
<Header/>

<main class="mini-hv">
    <slot />
</main>

<Footer/>