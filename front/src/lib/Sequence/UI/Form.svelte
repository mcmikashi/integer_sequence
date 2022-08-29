<script>
    import { createEventDispatcher } from 'svelte';
    import {
      Form,
      NumberInput,
      Button,
      Grid,
      Row,
      Column,
    } from "carbon-components-svelte";
    let value = 0; 
    const dispatch = createEventDispatcher();
</script>

<Form on:submit={(e) => {
    e.preventDefault();
    dispatch('index', {
        index: value});

  }}>
    <Grid padding>
        <Row class="align-item-center">
            <Column>
                <NumberInput
                min={0}
                max={1000}
                bind:value
                invalidText="Number must be between 0 and 1000."
                helperText="The index number of the desired value."
                label="Index (0 min, 1000 max)"
                name="desired_index"
                />
            </Column>
            <Column>
                <Button size="field" type="submit" >Submit</Button>
            </Column>
        </Row>
    </Grid>
</Form>