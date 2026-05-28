class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Stack<Double> stack = new Stack<>();

        NavigableMap<Integer, Integer> map = new TreeMap<>();

        for(int i = 0; i < position.length; i++) {
            map.put(position[i], speed[i]);
        }

        
        for (Map.Entry<Integer, Integer> entry : map.descendingMap().entrySet()) {
            double time = (double)(target - entry.getKey()) / entry.getValue();

            if(stack.isEmpty() || time > stack.peek()) {
                stack.push(time);
            }
        }

        return stack.size();
    }
}