impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut count = HashMap::new();
        for &num in &nums {
            *count.entry(num).or_insert(0) += 1;
        }

        let mut arr: Vec<(i32, i32)> = count.into_iter().map(|(num, cnt)| (cnt, num)).collect();
        arr.sort_unstable_by(|a, b| b.0.cmp(&a.0));

        arr.iter().take(k).map(|&(_, num)| num).collect()
    }
}