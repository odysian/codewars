// https://www.codewars.com/kata/55f2b110f61eb01779000053/train/typescript

export function getSum(a: number, b: number): number {
  // Find min and max
  const min = Math.min(a, b);
  const max = Math.max(a, b);

  let total = 0;
  // Loop through and add them up
  for (let i = min; i <= max; i++) {
    total += i;
  }
  return total;
}
