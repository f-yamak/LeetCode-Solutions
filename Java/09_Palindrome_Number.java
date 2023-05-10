public class Solution {
    public boolean isPalindrome(int x) {
        String st = String.valueOf(x);
        int last  = st.length()-1;
        
        for (int i = 0; i < st.length()/2; i++) {
            if (st.charAt(i) != st.charAt(last)) 
                return false;
            last--;
        }
        
        return true;
    }
    
}