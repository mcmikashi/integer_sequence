<script>
    import { metatags } from '@roxi/routify'
    let theme = "g100"; // "white" | "g10" | "g80" | "g90" | "g100"
    $: document.documentElement.setAttribute("theme", theme);
    metatags.title = 'My Routify app'
    metatags.description = 'Description coming soon...'
    import {
      Header,
      HeaderNav,
      HeaderNavItem,
      HeaderNavMenu,
      SideNav,
      SideNavItems,
      SideNavLink,
      SideNavDivider,
      SideNavMenu,
      SideNavMenuItem,
      SkipToContent,
      Content,
      Grid,
      Row,
      Column,
    } from "carbon-components-svelte";
  
    let isSideNavOpen = false;
    let expandedByDefault = false;
</script>
  
<Header company="IBM" platformName="Carbon Svelte" bind:isSideNavOpen bind:expandedByDefault>
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
  <HeaderNav>
    <HeaderNavItem href="/" text="Link 1" />
    <HeaderNavItem href="/" text="Link 2" />
    <HeaderNavItem href="/" text="Link 3" />
    <HeaderNavMenu text="Menu">
      <HeaderNavItem href="/" text="Link 1" />
      <HeaderNavItem href="/" text="Link 2" />
      <HeaderNavItem href="/" text="Link 3" />
    </HeaderNavMenu>
    <HeaderNavItem href="/" text="Link 4" />
  </HeaderNav>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavLink text="Link 1" />
    <SideNavLink text="Link 2" />
    <SideNavLink text="Link 3" />
    <SideNavMenu text="Menu">
      <SideNavMenuItem href="/" text="Link 1" />
      <SideNavMenuItem href="/" text="Link 2" />
      <SideNavMenuItem href="/" text="Link 3" />
    </SideNavMenu>
    <SideNavDivider />
    <SideNavLink text="Link 4" />
  </SideNavItems>
</SideNav>

<Content>
<Grid>
    <Row>
    <Column>
        <h1>Routify Starter Template</h1>

        <p>
            To see an example app that shows off a lot of Routify's features, go to <a href="/default">/example</a>
        </p>
        
        <p>
            This template is ready to be used in production! just delete the example app at: src/pages/example
        </p>
    </Column>
    </Row>
</Grid>
</Content>
