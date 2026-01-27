// https://www.codewars.com/kata/5264d2b162488dc400000001/train/typescript

export function spinWords(words: string): string {
  const word_list: string[] = words.split(" ");

  const res: string[] = [];

  for (let word of word_list) {
    if (word.length >= 5) {
      res.push(word.split("").reverse().join(""));
    } else {
      res.push(word);
    }
  }
  return res.join(" ");
}

export function spinWords1(words: string): string {
  return words
    .split(" ")
    .map((word) => {
      if (word.length >= 5) {
        return word.split("").reverse().join("");
      }
      return word;
    })
    .join(" ");
}
