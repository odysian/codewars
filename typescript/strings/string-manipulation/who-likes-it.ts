// https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/typescript

export const likes = (a: string[]): string => {
  let n = a.length;

  if (n === 0) {
    return "no one likes this";
  } else if (n === 1) {
    return `${a[0]} likes this`;
  } else if (n === 2) {
    return `${a[0]} and ${a[1]} like this`;
  } else if (n === 3) {
    return `${a[0]}, ${a[1]} and ${a[2]} like this`;
  } else {
    return `${a[0]}, ${a[1]} and ${a.length - 2} others like this`;
  }
};
