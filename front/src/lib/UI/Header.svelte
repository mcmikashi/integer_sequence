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
  
<Header company="MA"  platformName="Integer Sequence" bind:isSideNavOpen bind:expandedByDefault>
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
  <HeaderNav>
    <HeaderNavMenu text="Sequence">
      <HeaderNavItem href="/fibonacci" text="Fibonacci" />
      <HeaderNavItem href="/tribonacci" text="Tribonacci" />
      <HeaderNavItem href="/lucas" text="Lucas" />
      <HeaderNavItem href="/rabbit" text="Rabbits" />
    </HeaderNavMenu>
  </HeaderNav>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavMenu text="Sequence">
      <SideNavMenuItem href="/fibonacci" text="Fibonacci" />
      <SideNavMenuItem href="/tribonacci" text="Tribonacci" />
      <SideNavMenuItem href="/lucas" text="Lucas" />
      <SideNavMenuItem href="/rabbit" text="Rabbits" />
    </SideNavMenu>
  </SideNavItems>
</SideNav>
