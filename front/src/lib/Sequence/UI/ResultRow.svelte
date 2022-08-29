<script>
    import {
        CodeSnippet,
        Row,
        Column,
    } from "carbon-components-svelte";
    export let index; 
    export let result;
</script>
<Row>
    <Column sm={4} md={2}>
        <CodeSnippet code="{index}"/>
    </Column>
    <Column sm={4} md={6}>
        {#if result === null}
            <CodeSnippet skeleton/>
        {:else}
            <CodeSnippet code="{result}"/>
        {/if}
    </Column>
</Row>