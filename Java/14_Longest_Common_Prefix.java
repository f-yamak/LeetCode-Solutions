public class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        int counter = 0;
        for (int i = 0; i < strs[0].length(); i++) {
            for (int j = 1; j < strs.length; j++) {
                if ((counter >= strs[j].length()) || strs[0].charAt(counter)!= strs[j].charAt(counter)) {
                    return prefix;
                }
            }
            prefix += strs[0].charAt(counter);
            counter++;
        }
        
        return prefix;
    }
}