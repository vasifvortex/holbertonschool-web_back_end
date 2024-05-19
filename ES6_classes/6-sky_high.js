/* eslint-disable */
import Building from "./5-building.js";

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }
  get sqft() {
    return this._sqft;
  }
  get floors() {
    return this._floors;
  }
  set floors(newFloors) {
    if (typeof newFloors !== "number") {
      throw TypeError("must be number");
    }
    this._floors = newFloors;
  }
  set sqft(newSqft) {
    if (typeof newSqft !== "number") {
      throw TypeError("must be number");
    }
    this._sqft = newSqft;
  }
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}

export default SkyHighBuilding;
