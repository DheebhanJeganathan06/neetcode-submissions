class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = 0;
        for (int pile : piles) {
            r = Math.max(r, pile);
        }

        while (l < r) {
            int i = l + (r - l) / 2; // Integer overflow consideration!
            if (canEatAll(piles, h, i)) {
                r = i;
            } else {
                l = i + 1;
            }
        }
        return l;
    }

    private boolean canEatAll(int[] piles, int h, int speed) {
        int hours = 0;
        for (int pile : piles) {
            hours += (pile + speed - 1) / speed;
        }
        return hours <= h;
    }
}