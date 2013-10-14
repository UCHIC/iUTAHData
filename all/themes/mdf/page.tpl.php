<?php

/**
 * @file
 * Default theme implementation to display a single Drupal page.
 *
 * The doctype, html, head and body tags are not in this template. Instead they
 * can be found in the html.tpl.php template in this directory.
 *
 * Available variables:
 *
 * General utility variables:
 * - $base_path: The base URL path of the Drupal installation. At the very
 *   least, this will always default to /.
 * - $directory: The directory the template is located in, e.g. modules/system
 *   or themes/bartik.
 * - $is_front: TRUE if the current page is the front page.
 * - $logged_in: TRUE if the user is registered and signed in.
 * - $is_admin: TRUE if the user has permission to access administration pages.
 *
 * Site identity:
 * - $front_page: The URL of the front page. Use this instead of $base_path,
 *   when linking to the front page. This includes the language domain or
 *   prefix.
 * - $logo: The path to the logo image, as defined in theme configuration.
 * - $site_name: The name of the site, empty when display has been disabled
 *   in theme settings.
 * - $site_slogan: The slogan of the site, empty when display has been disabled
 *   in theme settings.
 *
 * Navigation:
 * - $main_menu (array): An array containing the Main menu links for the
 *   site, if they have been configured.
 * - $secondary_menu (array): An array containing the Secondary menu links for
 *   the site, if they have been configured.
 * - $breadcrumb: The breadcrumb trail for the current page.
 *
 * Page content (in order of occurrence in the default page.tpl.php):
 * - $title_prefix (array): An array containing additional output populated by
 *   modules, intended to be displayed in front of the main title tag that
 *   appears in the template.
 * - $title: The page title, for use in the actual HTML content.
 * - $title_suffix (array): An array containing additional output populated by
 *   modules, intended to be displayed after the main title tag that appears in
 *   the template.
 * - $messages: HTML for status and error messages. Should be displayed
 *   prominently.
 * - $tabs (array): Tabs linking to any sub-pages beneath the current page
 *   (e.g., the view and edit tabs when displaying a node).
 * - $action_links (array): Actions local to the page, such as 'Add menu' on the
 *   menu administration interface.
 * - $feed_icons: A string of all feed icons for the current page.
 * - $node: The node object, if there is an automatically-loaded node
 *   associated with the page, and the node ID is the second argument
 *   in the page's path (e.g. node/12345 and node/12345/revisions, but not
 *   comment/reply/12345).
 *
 * Regions:
 * - $page['help']: Dynamic help text, mostly for admin pages.
 * - $page['highlighted']: Items for the highlighted content region.
 * - $page['content']: The main content of the current page.
 * - $page['sidebar_first']: Items for the first sidebar.
 * - $page['sidebar_second']: Items for the second sidebar.
 * - $page['header']: Items for the header region.
 * - $page['footer']: Items for the footer region.
 *
 * @see template_preprocess()
 * @see template_preprocess_page()
 * @see template_process()
 * @see html.tpl.php
 *
 * @ingroup themeable
 */
?>
  <div id="main">
    <header>
      <div id="logo">
        <img src="http://iutahepscor.org/images/logos_hires/iutah_eu_horz_sm.png" width="194" height="78">
        <div id="logo_text">
            
            <h1><a href="Home">Modeling and Data Federation</a></h1>
          <h2>innovative Urban Transitions and Aridregion Hydro-sustainability</h2>
        </div>
      </div>
      <nav>
        <?php print render($page["main_nav"]); ?>
      </nav>
    </header>

    
    <?php if ($action_links): ?><ul class="action-links"><?php print render($action_links); ?></ul><?php endif; ?>

    <div id="site_content">
    
      <?php if ($tabs && $is_admin): ?>
        <div class="tabs">
		  <?php print render($tabs); ?>
		</div>
	  <?php endif; ?>
    
      <div id="content">
        <h1><?php print render($title) ?></h1>
        <?php print render($page['content']); ?>
      </div>
    </div>
    <footer>
        <div id="footer-left-image">
            <a href="http://utepscor.org/" target="_blank"><img src="http://iutahepscor.org/images/logos_hires/epscor_logo_rgb_sm.jpg" alt="Utah EPSCoR" width="156" height="73"></a>
        </div>
		<div id="footer-text">
            <p>This project is funded through <a href="http://www.nsf.gov/awardsearch/showAward.do?AwardNumber=1208732" target="_blank">EPS - 1208732</a>.  Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.</p>
		</div>
        <aside id="footer-right-image">
            <a href="http://www.nsf.gov/div/index.jsp?div=EPSC" target="_blank">
                <img src="http://iutahepscor.org/images/nsf1.png" alt="National Science Foundation" width="80" height="80">
            </a>
        </aside>
    </footer>
  </div>