<script>
  import Facts from "../lib/Facts/Facts.svelte";
</script>

<h3>It's a small app around numbers</h3>
<p>What is a numbers ?</p>
<blockquote>
  A number is a mathematical object used to count, measure, and label. The
  original examples are the natural numbers 1, 2, 3, 4, and so forth. Numbers
  can be represented in language with number words. More universally, individual
  numbers can be represented by symbols, called numerals; for example, "5" is a
  numeral that represents the number five.
  <p class="source-blockquote">
    source : 
    <cite>
        <a href="https://en.wikipedia.org/wiki/Number" target="_blank" rel="noopener noreferrer">
        https://en.wikipedia.org/wiki/Number
        </a>
    </cite>
  </p>
</blockquote>
<p>Now let's see four random facts about numbers.</p>
<Facts />
<p class="source-blockquote">
  source : 
    <cite>
        <a href="http://numbersapi.com/" target="_blank" rel="noopener noreferrer">
            http://numbersapi.com/
        </a>
    </cite>
</p>

<style>
  p {
    margin: 25px 0px;
  }
  blockquote {
    font-size: larger;
    margin: 15px 0px;
  }
  .source-blockquote {
    text-align: right;
    margin: 10px 0px;
  }
</style>
