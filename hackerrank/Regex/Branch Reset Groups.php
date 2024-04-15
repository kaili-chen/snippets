// php 
// Branch reset group is supported by Perl, PHP, Delphi and R.

// TASK
// rite a regex which will match test string S, with following condition(s):
// S consists of 8 digits.
// S must have "---", "-", "." or ":" separator such that string  gets divided in parts, with each part having exactly two digits.
// S string must have exactly one kind of separator.
// Separators must have integers on both sides.

<?php

$Regex_Pattern = '/^\d{2}(?|(---)|(-)|(\.)|(:))\d{2}\1\d{2}\1\d{2}$/'; //Do not delete '/'. Replace __________ with your regex.

$handle = fopen ("php://stdin","r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print ("true");
} else {
    print ("false");
}

fclose($handle);
?>
