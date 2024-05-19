/* eslint-disable */
export default class Building{
    constructor(sqft){
        this._sqft = sqft
        this.evacuationWarningMessage()
    }
    get sqft(){
        return this._sqft
    }
    set sqft(newSqft){
        if (typeof newSqft !== "number"){
            throw TypeError("must be number")
        }
        this.sqft = newSqft
    }
    evacuationWarningMessage(){
        if (this.constructor !== Building){
            throw new Error("Class extending Building must override evacuationWarningMessage");
        }
    }
    
}