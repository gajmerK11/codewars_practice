<?php

/*
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
*/

// Following code works for the small array

function plusOne($arr)
{
    $int = (int) implode('', $arr);
    $plusOne = $int + 1;
    $newArray = [];

    while ($plusOne > 0) {
        $digit = $plusOne % 10;
        $newArray[] = $digit;
        $plusOne = intdiv($plusOne, 10);
    }

    $newArray = array_reverse($newArray);
    return $newArray;
}
print_r(plusOne([9]));
?>


<?php
// For bigger array
function anotherOne($digits)
{
    $n = count($digits);

    // start from last digit
    for ($i = $n - 1; $i >= 0; $i--) {
        if ($digits[$i] < 9) {
            $digits[$i]++;  // just add 1
            return $digits;
        }
        $digits[$i] = 0; // carry over
    }

    // if we are here, all digits were 9 (e.g. 999 -> 1000)
    array_unshift($digits, 1);
    return $digits;
}
?>