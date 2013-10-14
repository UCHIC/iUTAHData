<?php

function mdf_links($variables) {
  if (array_key_exists('id', $variables['attributes']) && $variables['attributes']['id'] == 'main-menu-links') {
      $pid = variable_get('menu_main_links_source', 'main-menu');
    $tree = menu_tree($pid);
    return drupal_render($tree);
  }
  return theme_links($variables);
}

//drupal_add_js('jQuery.extend(Drupal.settings, { "pathToTheme": "/' . path_to_theme() . '" });', 'inline');
//drupal_add_js(drupal_get_path('theme', 'iutah') .'/highlights.js');