<script>
    export let arrayAlert;
    import {InlineNotification} from "carbon-components-svelte";
</script>

<section id="alert-section">
    {#each arrayAlert as userAlert}
        <InlineNotification
        title={userAlert.title}
        subtitle={userAlert.message}
        timeout=5000
        />
    {/each}
</section>