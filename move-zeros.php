
<?php
/*

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

*/

function moveZeros(&$nums)
{
    $pos = 0; // position for next non-zero element

    // Move non-zeros forward
    foreach ($nums as $num) {
        if ($num !== 0) {
            $nums[$pos] = $num;
            $pos++;
        }
    }

    // Fill remaining with zeros
    while ($pos < count($nums)) {
        $nums[$pos] = 0;
        $pos++;
    }
}

$nums = [0,1,0,3,12];
moveZeros($nums);
print_r($nums); // [1,3,12,0,0]
