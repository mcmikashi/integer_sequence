<script>
    import {
      Header,
      HeaderNav,
      HeaderNavItem,
      HeaderNavMenu,
      SideNav,
      SideNavItems,
      SideNavMenu,
      SideNavMenuItem,
      SkipToContent,
    } from "carbon-components-svelte";
  
    let isSideNavOpen = false;
    let expandedByDefault = false;
</script>
  
<Header company="MA"  platformName="Integer Sequence" bind:isSideNavOpen bind:expandedByDefault href="/index">
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
  <HeaderNav>
    <HeaderNavMenu text="Sequence">
      <HeaderNavItem href="/sequence/fibonacci" text="Fibonacci" />
      <HeaderNavItem href="/sequence/tribonacci" text="Tribonacci" />
      <HeaderNavItem href="/sequence/lucas" text="Lucas" />
      <HeaderNavItem href="/sequence/rabbits" text="Rabbits" />
    </HeaderNavMenu>
  </HeaderNav>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavMenu text="Sequence">
      <SideNavMenuItem href="/sequence/fibonacci" text="Fibonacci" />
      <SideNavMenuItem href="/sequence/tribonacci" text="Tribonacci" />
      <SideNavMenuItem href="/sequence/lucas" text="Lucas" />
      <SideNavMenuItem href="/sequence/rabbits" text="Rabbits" />
    </SideNavMenu>
  </SideNavItems>
</SideNav>
