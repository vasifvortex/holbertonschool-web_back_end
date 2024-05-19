/*eslint-disable*/

class HolbertonClass {
  constructor(size, location, teacher) {
    this.size = size;
    this.location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === "string") return this.location;
    if (hint === "number") return this.size;
    return null;
  }
}
export default HolbertonClass;
