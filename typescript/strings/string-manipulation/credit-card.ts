// https://www.codewars.com/kata/5412509bd436bd33920011bc/train/typescript

// return masked string
export function maskify(cc: string): string {
  if (cc.length <= 4) {
    return cc;
  }
  // Get length of cc
  const len = cc.length;
  // Build string of #'s and add the last 4 with slice
  return "#".repeat(len - 4) + cc.slice(-4);
}
