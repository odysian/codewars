// https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/typescript

export class Kata {
  static dnaStrand(dna: string) {
    const comp: Record<string, string> = {
      A: "T",
      T: "A",
      C: "G",
      G: "C",
    };
    let result = "";

    for (let d of dna) {
      result += comp[d];
    }
    return result;
  }
}
